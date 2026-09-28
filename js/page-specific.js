// Ensure page-specific scripts run reliably regardless of DOM ready state
(function () {
  function initPageSpecific() {
    // 1. Sticky Navbar Color Transition on Scroll
    const navbar = document.querySelector('.sticky-top .navbar');
    const lightSections = document.querySelectorAll('.light-section, .bg-tan');

    if (navbar && lightSections.length > 0) {
      function checkNavbarColor() {
        const navbarHeight = navbar.offsetHeight;
        let isOverLightSection = false;

        lightSections.forEach(section => {
          const rect = section.getBoundingClientRect();
          if (rect.top <= navbarHeight && rect.bottom >= navbarHeight) {
            isOverLightSection = true;
          }
        });

        if (isOverLightSection) {
          navbar.classList.remove('navbar-dark', 'bg-custom-dark');
          navbar.classList.add('navbar-light', 'bg-light');
        } else {
          navbar.classList.remove('navbar-light', 'bg-light');
          navbar.classList.add('navbar-dark', 'bg-custom-dark');
        }
      }

      checkNavbarColor();
      window.addEventListener('scroll', checkNavbarColor, { passive: true });
    }

    // 2. UX Writing Category Filter System
    const carouselEl = document.getElementById('uxSamplesCarousel');
    const filterContainer = document.querySelector('.ux-filter-dock, .ux-filter-container');

    if (carouselEl && filterContainer) {
      const carouselInner = carouselEl.querySelector('.carousel-inner');
      if (carouselInner) {
        // Cache all initial items in their curated order
        const allItems = Array.from(carouselInner.querySelectorAll('.carousel-item'));
        const filterButtons = filterContainer.querySelectorAll('.ux-filter-pill');

        filterButtons.forEach(btn => {
          btn.addEventListener('click', function (e) {
            e.preventDefault();
            const filter = this.getAttribute('data-filter');

            // Update active pill button state
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Center active pill in horizontal scroll dock on mobile
            if (window.innerWidth < 768) {
              this.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            }

            // Determine matching items
            const matchingItems = (filter === 'all')
              ? allItems
              : allItems.filter(item => {
                  const categories = (item.getAttribute('data-category') || '').split(' ');
                  return categories.includes(filter);
                });

            if (matchingItems.length === 0) return;

            // Dispose existing Bootstrap Carousel instance to avoid stale index caches
            if (window.bootstrap && bootstrap.Carousel) {
              const existingCarousel = bootstrap.Carousel.getInstance(carouselEl);
              if (existingCarousel) {
                existingCarousel.dispose();
              }
            }

            // Sync carousel-inner with matching items
            carouselInner.innerHTML = '';
            matchingItems.forEach((item, index) => {
              item.classList.remove('active');
              if (index === 0) {
                item.classList.add('active');
              }
              carouselInner.appendChild(item);
            });

            // Re-initialize Bootstrap carousel on the updated items
            if (window.bootstrap && bootstrap.Carousel) {
              const newCarousel = new bootstrap.Carousel(carouselEl, {
                ride: false,
                wrap: true
              });
              newCarousel.to(0);
            }
          });
        });
      }
    }

    // 3. Challenge 14 Draft Toggle (Before / After Switcher via Delegation)
    document.addEventListener('click', function (e) {
      const toggleBtn = e.target.closest('.btn-draft-toggle');
      if (!toggleBtn) return;
      e.preventDefault();
      e.stopPropagation();

      const pdfSrc = toggleBtn.getAttribute('data-pdf');
      if (!pdfSrc) return;

      // Update all draft toggle buttons with matching pdfSrc to active
      document.querySelectorAll('.btn-draft-toggle').forEach(b => {
        if (b.getAttribute('data-pdf') === pdfSrc) {
          b.classList.add('active');
        } else {
          b.classList.remove('active');
        }
      });

      const iframe = document.getElementById('challenge14Iframe');
      if (iframe) {
        iframe.src = pdfSrc;
      }

      const card = toggleBtn.closest('.sample-card') || document.querySelector('[data-pdf*="challenge-14"]');
      if (card) {
        card.setAttribute('data-pdf', pdfSrc);
      }
    });

    // 4. Hardware Technical Writing Category Filter System
    const hardwareFilterContainer = document.querySelector('.hardware-filter-dock');
    const hardwareGrid = document.querySelector('.bg-custom-dark .row.g-4.justify-content-center');

    if (hardwareFilterContainer && hardwareGrid) {
      const filterButtons = hardwareFilterContainer.querySelectorAll('.hardware-filter-pill');
      const originalCards = hardwareGrid.querySelectorAll('.hardware-card-col:not(.carousel-clone)');
      const layoutBreak = hardwareGrid.querySelector('.hardware-layout-break');

      filterButtons.forEach(btn => {
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          const filter = this.getAttribute('data-filter');

          // Update active pill button state
          filterButtons.forEach(b => b.classList.remove('active'));
          this.classList.add('active');

          // Center active pill in horizontal scroll dock on mobile
          if (window.innerWidth < 768) {
            this.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
          }

          // Handle layout break (only shown when 'all' is active on desktop)
          if (layoutBreak) {
            if (filter === 'all') {
              layoutBreak.style.removeProperty('display');
            } else {
              layoutBreak.style.setProperty('display', 'none', 'important');
            }
          }

          // Filter original cards
          originalCards.forEach(cardCol => {
            const categories = (cardCol.getAttribute('data-category') || '').split(' ');
            const matches = (filter === 'all') || categories.includes(filter);
            if (matches) {
              cardCol.classList.remove('d-none');
              cardCol.style.removeProperty('display');
            } else {
              cardCol.classList.add('d-none');
              cardCol.style.setProperty('display', 'none', 'important');
            }
          });

          // Handle carousel clones generated by interactive.js on mobile
          const clones = hardwareGrid.querySelectorAll('.carousel-clone');
          clones.forEach(clone => {
            if (filter === 'all') {
              clone.classList.remove('d-none');
              clone.style.removeProperty('display');
            } else {
              clone.classList.add('d-none');
              clone.style.setProperty('display', 'none', 'important');
            }
          });

          // Reset horizontal scroll position on mobile so user sees visible cards immediately
          if (window.innerWidth < 768) {
            hardwareGrid.scrollLeft = 0;
          }
        });
      });
    }

    // 5. Articles Category Filter System
    const articleFilterContainer = document.querySelector('.article-filter-dock');
    const articleGrid = document.querySelector('.light-section .row.g-4.justify-content-center');

    if (articleFilterContainer && articleGrid) {
      const filterButtons = articleFilterContainer.querySelectorAll('.article-filter-pill');
      const originalCards = articleGrid.querySelectorAll('.article-card-col:not(.carousel-clone)');

      filterButtons.forEach(btn => {
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          const filter = this.getAttribute('data-filter');

          // Update active pill button state
          filterButtons.forEach(b => b.classList.remove('active'));
          this.classList.add('active');

          // Center active pill in horizontal scroll dock on mobile
          if (window.innerWidth < 768) {
            this.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
          }

          // Filter original cards
          originalCards.forEach(cardCol => {
            const categories = (cardCol.getAttribute('data-category') || '').split(' ');
            const matches = (filter === 'all') || categories.includes(filter);
            if (matches) {
              cardCol.classList.remove('d-none');
              cardCol.style.removeProperty('display');
            } else {
              cardCol.classList.add('d-none');
              cardCol.style.setProperty('display', 'none', 'important');
            }
          });

          // Handle carousel clones generated by interactive.js on mobile
          const clones = articleGrid.querySelectorAll('.carousel-clone');
          clones.forEach(clone => {
            if (filter === 'all') {
              clone.classList.remove('d-none');
              clone.style.removeProperty('display');
            } else {
              clone.classList.add('d-none');
              clone.style.setProperty('display', 'none', 'important');
            }
          });

          // Reset horizontal scroll position on mobile so user sees visible cards immediately
          if (window.innerWidth < 768) {
            articleGrid.scrollLeft = 0;
          }
        });
      });
    }
  }


  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPageSpecific);
  } else {
    initPageSpecific();
  }
})();