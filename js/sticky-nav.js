document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.sticky-top');
  const navbar = header.querySelector('.navbar');
  const lightSection = document.querySelector('.light-section');

  if (!header || !lightSection || !navbar) {
    return;
  }

  function checkSection() {
    const lightSectionTop = lightSection.getBoundingClientRect().top;
    const lightSectionBottom = lightSection.getBoundingClientRect().bottom;
    const navbarHeight = navbar.offsetHeight;

    if (lightSectionTop <= navbarHeight && lightSectionBottom >= navbarHeight) {
      navbar.classList.remove('navbar-dark', 'bg-custom-dark');
      navbar.classList.add('navbar-light', 'bg-light');
    } else {
      navbar.classList.remove('navbar-light', 'bg-light');
      navbar.classList.add('navbar-dark', 'bg-custom-dark');
    }
  }

  // Check on load
  checkSection();

  // Check on scroll
  window.addEventListener('scroll', checkSection);

  // Set active class based on current URL
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link, .dropdown-item').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (href === currentPath || (currentPath === '' && href === 'index.html'))) {
      link.classList.add('active');
      // If inside a dropdown, highlight the toggle too
      const dropdown = link.closest('.dropdown, .dropup');
      if (dropdown) {
        const toggle = dropdown.querySelector('.dropdown-toggle');
        if (toggle) toggle.classList.add('active');
      }
    }
  });
});
