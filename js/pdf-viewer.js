// PDF Viewer shared module
// Injects a Bootstrap modal into the page (once) and exposes behavior for opening PDFs.
(function () {
  if (window.__pdfViewerInitialized) return;
  window.__pdfViewerInitialized = true;

  const modalHtml = `
  <div class="modal fade" id="pdfModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-fullscreen">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="pdfModalLabel">Document Viewer</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body p-0 position-relative">
          <div id="pdfSpinner" class="position-absolute top-50 start-50 translate-middle" style="z-index:1051; display:none;">
            <div class="spinner-border text-secondary" role="status"><span class="visually-hidden">Loading...</span></div>
          </div>
          <div class="ratio ratio-16x9" id="pdfModalContainer">
            <iframe id="pdfModalIframe" class="w-100 h-100" src="" title="PDF viewer" frameborder="0"></iframe>
          </div>
        </div>
      </div>
    </div>
  </div>
  `;

  // Append modal to body
  document.addEventListener('DOMContentLoaded', () => {
    const wrapper = document.createElement('div');
    wrapper.innerHTML = modalHtml;
    document.body.appendChild(wrapper);

  const modalEl = document.getElementById('pdfModal');
  const modalLabel = document.getElementById('pdfModalLabel');
  const iframe = document.getElementById('pdfModalIframe');
  const spinner = document.getElementById('pdfSpinner');

    const bsModal = new bootstrap.Modal(modalEl, { keyboard: true });

    function showSpinner(show) {
      if (!spinner) return;
      spinner.style.display = show ? 'block' : 'none';
    }

    function loadPdf(src, title) {
      if (!iframe || !modalEl) return;
      modalLabel.textContent = title || 'Document Viewer';
      iframe.src = encodeURI(src);
      showSpinner(true);
    }

    function openPdf(src, title) {
      loadPdf(src, title);
      bsModal.show();
    }

    function closePdf() {
      if (!iframe) return;
      iframe.src = '';
      showSpinner(false);
    }

    modalEl.addEventListener('show.bs.modal', function (event) {
      const button = event.relatedTarget;
      if (!button) return;
      const card = button.closest('.sample-card');
      if (card) {
        const pdf = card.getAttribute('data-pdf');
        const title = (card.querySelector('.card-title') || {}).textContent || '';
        if (pdf) {
          loadPdf(pdf, title.trim());
        }
      }
    });

    // Hide spinner when iframe finishes loading.
    iframe.addEventListener('load', () => {
      showSpinner(false);
    });

    modalEl.addEventListener('hidden.bs.modal', () => {
      closePdf();
    });

    // Attach click/keyboard listeners to sample-card elements
    const sampleCards = Array.from(document.querySelectorAll('.sample-card'));

    // Inject styles for preview overlay and canvas
    (function injectPreviewStyles() {
      const css = `
      .preview-wrapper { position: relative; }
      .preview-overlay { position: absolute; inset: 0; display:flex; align-items:center; justify-content:center; pointer-events:none; }
      .preview-overlay .icon { width:48px; height:48px; background: rgba(0,0,0,0.5); border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; }
      .preview-canvas { width:100%; height:100%; display:block; }
      `;
      const s = document.createElement('style');
      s.setAttribute('data-generated', 'pdf-preview-styles');
      s.appendChild(document.createTextNode(css));
      document.head.appendChild(s);
    })();

    // Dynamically load PDF.js if needed
    function loadPdfJs() {
      return new Promise((resolve, reject) => {
        if (window.pdfjsLib) return resolve(window.pdfjsLib);
        const urlBase = 'https://cdn.jsdelivr.net/npm/pdfjs-dist@3.9.179/build/';
        const script = document.createElement('script');
        script.src = urlBase + 'pdf.min.js';
        script.onload = () => {
          if (window.pdfjsLib) {
            window.pdfjsLib.GlobalWorkerOptions.workerSrc = urlBase + 'pdf.worker.min.js';
            resolve(window.pdfjsLib);
          } else {
            reject(new Error('pdfjs failed to load'));
          }
        };
        script.onerror = () => reject(new Error('Failed to load pdfjs script'));
        document.head.appendChild(script);
      });
    }

    // Render a page-1 preview into canvas using pdf.js
    async function renderPreviewCanvas(previewWrapper, pdfUrl) {
      try {
        if (!window.pdfjsLib) await loadPdfJs();
        const canvas = document.createElement('canvas');
        canvas.className = 'preview-canvas';
        canvas.style.display = 'none';
        previewWrapper.appendChild(canvas);

        // fetch and render first page
        const loadingTask = window.pdfjsLib.getDocument({
          url: encodeURI(pdfUrl),
          cMapUrl: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@3.9.179/cmaps/',
          cMapPacked: true,
          standardFontDataUrl: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@3.9.179/standard_fonts/',
          disableFontFace: true
        });
        const pdf = await loadingTask.promise;
        const page = await pdf.getPage(1);
        const rect = previewWrapper.getBoundingClientRect();
        const scale = (rect.width * window.devicePixelRatio) / page.getViewport({ scale: 1 }).width;
        const viewport = page.getViewport({ scale });
        canvas.width = Math.round(viewport.width);
        canvas.height = Math.round(viewport.height);
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.style.objectFit = 'cover';
        canvas.style.objectPosition = 'top';
        const ctx = canvas.getContext('2d');
        const renderContext = { canvasContext: ctx, viewport };
        await page.render(renderContext).promise;
  // show canvas and hide original thumbnail (.card-img-top) if present
  canvas.style.display = 'block';
  const thumb = previewWrapper.nextElementSibling && previewWrapper.nextElementSibling.matches && previewWrapper.nextElementSibling.matches('.card-img-top') ? previewWrapper.nextElementSibling : null;
  if (thumb) thumb.style.display = 'none';
        return true;
      } catch (e) {
        console.warn('PDF preview render failed', e);
        // fallback: if this is a file:// environment or pdf.js can't fetch the file,
        // insert an iframe preview that points to the local PDF URL (many browsers will render it).
        try {
          const isLocal = location.protocol === 'file:';
          // Some environments disallow pdf.js from fetching file:// paths. Use iframe fallback when local.
          if (isLocal) {
            const iframe = document.createElement('iframe');
            iframe.className = 'w-100 h-100 rounded-1';
            iframe.style.border = '0';
            iframe.style.display = 'block';
            // Ensure proper encoding of spaces in file paths
            iframe.src = encodeURI(pdfUrl);
            previewWrapper.appendChild(iframe);
            // hide the thumbnail
            const thumb = previewWrapper.nextElementSibling && previewWrapper.nextElementSibling.matches && previewWrapper.nextElementSibling.matches('.card-img-top') ? previewWrapper.nextElementSibling : null;
            if (thumb) thumb.style.display = 'none';
            return true;
          }
        } catch (e2) {
          console.warn('iframe fallback failed', e2);
        }
        // leave existing thumbnail as fallback
        return false;
      }
    }

    // IntersectionObserver to lazy-render previews (supports PDFs and external link previews)
    const previewObserver = ('IntersectionObserver' in window) ? new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const wrapper = entry.target;
        const pdfUrl = wrapper.dataset.pdf;
        const hrefUrl = wrapper.dataset.href;
        if (pdfUrl) {
          // attempt to render preview and stop observing
          renderPreviewCanvas(wrapper, pdfUrl).then(() => obs.unobserve(wrapper)).catch(() => obs.unobserve(wrapper));
        } else if (hrefUrl) {
          // lazy-load an iframe preview for the external link
          const iframe = wrapper.querySelector('iframe[data-src]');
          if (iframe && !iframe.src) {
            try {
              iframe.src = iframe.dataset.src;
              iframe.style.display = 'block';
              const thumb = wrapper.nextElementSibling && wrapper.nextElementSibling.matches && wrapper.nextElementSibling.matches('.card-img-top') ? wrapper.nextElementSibling : null;
              if (thumb) thumb.style.display = 'none';
            } catch (e) {
              console.warn('failed to load link preview iframe', e);
            }
          }
          obs.unobserve(wrapper);
        } else {
          obs.unobserve(wrapper);
        }
      });
    }, { root: null, rootMargin: '300px 0px', threshold: 0.01 }) : null;

    // Replace broken mobile iframes with PDF.js canvas previews
    const isMobile = window.innerWidth <= 768 || /Mobi|Android/i.test(navigator.userAgent);
    if (isMobile) {
      document.querySelectorAll('iframe[src$=".pdf"]').forEach(iframe => {
        const parent = iframe.parentNode;
        iframe.style.display = 'none'; // hide the native iframe
        parent.dataset.pdf = iframe.src; // mark for intersection observer
        parent.classList.add('preview-wrapper');
        // overlay icon to indicate it's tappable
        const overlay = document.createElement('div');
        overlay.className = 'preview-overlay';
        overlay.innerHTML = '<div class="icon" aria-hidden="true">🔍</div>';
        parent.appendChild(overlay);
        if (previewObserver) previewObserver.observe(parent);
      });
    }

    sampleCards.forEach(card => {
      console.log('Processing card:', card);
      const pdf = card.getAttribute('data-pdf');
      const href = card.getAttribute('data-href');
      const title = (card.querySelector('.card-title') || {}).textContent || '';

  // If the card has a thumbnail (img/svg/other .card-img-top) and a pdf, insert a preview wrapper
  const thumb = card.querySelector('.card-img-top');
      console.log('Found thumb:', thumb);
      console.log('Found pdf:', pdf);
      if (thumb && pdf) {
        try {
          const previewWrapper = document.createElement('div');
          previewWrapper.className = 'ratio ratio-4x3 mb-3 preview-wrapper';
          // store pdf url as data attribute for the observer
          previewWrapper.dataset.pdf = pdf;
          // overlay icon
          const overlay = document.createElement('div');
          overlay.className = 'preview-overlay';
          overlay.innerHTML = '<div class="icon" aria-hidden="true">🔍</div>';
          previewWrapper.appendChild(overlay);
          // insert preview wrapper directly before the thumbnail so layout is preserved
          thumb.parentNode.insertBefore(previewWrapper, thumb);
          // observe preview wrapper to lazy-render
          if (previewObserver) previewObserver.observe(previewWrapper);
        } catch (e) {
          console.warn('preview insertion failed', e);
        }
      } else if (thumb && href) {
        try {
          const previewWrapper = document.createElement('div');
          previewWrapper.className = 'ratio ratio-4x3 mb-3 preview-wrapper';
          previewWrapper.dataset.href = href;
          // overlay icon
          const overlay = document.createElement('div');
          overlay.className = 'preview-overlay';
          overlay.innerHTML = '<div class="icon" aria-hidden="true">🔗</div>';
          previewWrapper.appendChild(overlay);
          // create lazy iframe for external site preview
          const previewIframe = document.createElement('iframe');
          previewIframe.setAttribute('title', (title ? title + ' preview' : 'Site preview'));
          previewIframe.setAttribute('frameborder', '0');
          previewIframe.style.display = 'none';
          previewIframe.setAttribute('loading', 'lazy');
          previewIframe.dataset.src = href;
          previewWrapper.appendChild(previewIframe);
          // insert preview wrapper directly before the thumbnail so layout is preserved
          thumb.parentNode.insertBefore(previewWrapper, thumb);
          if (previewObserver) previewObserver.observe(previewWrapper);
        } catch (e) {
          console.warn('link preview insertion failed', e);
        }
      }

      // attach open handlers
      card.addEventListener('click', (e) => {
        // Failsafe: Ignore clicks on interactive controls, buttons, links, or inside collapsible content
        if (e.target.closest('button, a, input, select, textarea, [data-bs-toggle], .collapse, .ux-details-toggle, .btn')) {
          return;
        }
        if (href) {
          window.open(href, '_blank', 'noopener');
        } else if (pdf) {
          openPdf(pdf, title.trim());
        }
      });
      card.addEventListener('keydown', (ev) => {
        if (ev.key === 'Enter' || ev.key === ' ') {
          if (ev.target.closest('button, a, input, select, textarea, [data-bs-toggle], .collapse, .ux-details-toggle, .btn')) {
            return;
          }
          ev.preventDefault();
          if (href) window.open(href, '_blank', 'noopener'); else if (pdf) openPdf(pdf, title.trim());
        }
      });
    });

  });
})();