document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.sticky-top');
  const navbars = header ? header.querySelectorAll('.navbar') : [];
  const lightSection = document.querySelector('.light-section');

  if (!header || !lightSection || navbars.length === 0) {
    return;
  }

  function checkSection() {
    const lightSectionTop = lightSection.getBoundingClientRect().top;
    const lightSectionBottom = lightSection.getBoundingClientRect().bottom;
    const navbarHeight = (navbars[0] || header).offsetHeight;

    if (lightSectionTop <= navbarHeight && lightSectionBottom >= navbarHeight) {
      header.classList.add('is-light');
      navbars.forEach(nb => {
        nb.classList.remove('navbar-dark', 'bg-custom-dark');
        nb.classList.add('navbar-light', 'bg-light');
      });
    } else {
      header.classList.remove('is-light');
      navbars.forEach(nb => {
        nb.classList.remove('navbar-light', 'bg-light');
        nb.classList.add('navbar-dark', 'bg-custom-dark');
      });
    }
  }

  // Check on load
  checkSection();

  // Check on scroll
  window.addEventListener('scroll', checkSection);

  // Set active class based on current URL (supports clean extensionless URLs, .html, and /es/, /fr/, /ar/, /cmn/, /zh/, /ja/ localization)
  const segments = window.location.pathname.split('/').filter(Boolean);
  const isLang = ['es', 'fr', 'ar', 'zh', 'ja', 'hi', 'cmn'].includes(segments[0]);
  const pageSegment = isLang ? (segments[1] || '') : (segments[0] || '');
  const currentSlug = pageSegment.replace(/\.html$/, '');

  document.querySelectorAll('.nav-link, .dropdown-item').forEach(link => {
    // Skip language selector dropdown links from general navigation active matching
    if (link.closest('#navbarDropdownLang, #navbarDropdownLangMobile, [aria-labelledby="navbarDropdownLang"], [aria-labelledby="navbarDropdownLangMobile"]')) {
      return;
    }
    const href = link.getAttribute('href');
    if (href && !href.startsWith('http') && !href.startsWith('mailto:')) {
      const linkSegments = href.split('#')[0].split('?')[0].split('/').filter(Boolean);
      const linkIsLang = ['es', 'fr', 'ar', 'zh', 'ja', 'hi', 'cmn'].includes(linkSegments[0]);
      const linkPageSegment = linkIsLang ? (linkSegments[1] || '') : (linkSegments[0] || '');
      const normalizedHref = linkPageSegment.replace(/\.html$/, '');

      const isHomeMatch = (currentSlug === '' || currentSlug === 'index') && (normalizedHref === '' || normalizedHref === 'index');
      const isPageMatch = currentSlug !== '' && currentSlug !== 'index' && normalizedHref === currentSlug;

      if (isHomeMatch || isPageMatch) {
        link.classList.add('active');
        // If inside a dropdown, highlight the toggle too
        const dropdown = link.closest('.dropdown, .dropup');
        if (dropdown) {
          const toggle = dropdown.querySelector('.dropdown-toggle');
          if (toggle) toggle.classList.add('active');
        }
      }
    }
  });

  // Handle nested mobile dropend sub-menus
  document.querySelectorAll('.dropdown-menu .dropend > .dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const parent = toggle.closest('.dropend');
      const subMenu = parent.querySelector('.dropdown-menu');
      if (subMenu) {
        const isShown = subMenu.classList.contains('show');
        parent.parentElement.querySelectorAll('.dropend .dropdown-menu.show').forEach(m => m.classList.remove('show'));
        parent.parentElement.querySelectorAll('.dropend.show').forEach(d => d.classList.remove('show'));
        if (!isShown) {
          subMenu.classList.add('show');
          parent.classList.add('show');
        }
      }
    });
  });

  // When parent dropup/dropdown is closed, close all nested sub-menus
  document.querySelectorAll('.dropdown, .dropup').forEach(dropdown => {
    dropdown.addEventListener('hidden.bs.dropdown', () => {
      dropdown.querySelectorAll('.dropdown-menu.show').forEach(m => m.classList.remove('show'));
      dropdown.querySelectorAll('.dropend.show').forEach(d => d.classList.remove('show'));
    });
  });
});
