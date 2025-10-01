document.addEventListener('DOMContentLoaded', function () {
  const mobileMenuButton = document.getElementById('mobile-menu-button');
  const mainNav = document.getElementById('main-nav');

  if (mobileMenuButton && mainNav) {
    mobileMenuButton.addEventListener('click', function () {
      mainNav.classList.toggle('hidden');
    });
  }
});