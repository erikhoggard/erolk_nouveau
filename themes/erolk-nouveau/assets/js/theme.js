document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.getElementById('theme-toggle');

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      document.documentElement.classList.toggle('dark');

      const theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
      localStorage.setItem('color-theme', theme);

    });
  }

});

