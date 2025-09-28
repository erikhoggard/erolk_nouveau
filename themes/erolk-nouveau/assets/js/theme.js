document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.getElementById('theme-toggle');
  const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
  const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');
  // Function to update the icon based on the current theme
  const updateIcon = () => {
    if (document.documentElement.classList.contains('dark')) {
      themeToggleLightIcon.classList.remove('hidden');
      themeToggleDarkIcon.classList.add('hidden');
    } else {
      themeToggleDarkIcon.classList.remove('hidden');
      themeToggleLightIcon.classList.add('hidden');
    }
  };

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      document.documentElement.classList.toggle('dark');

      const theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
      localStorage.setItem('color-theme', theme);

      updateIcon();
    });
  }

  updateIcon();
});

