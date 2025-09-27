module.exports = {
  darkMode: 'class',
  content: [
    './content/**/*.md',
    './themes/erolk-nouveau/layouts/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['ChicagoFLF', 'sans-serif'],
        mono: ['Roboto Mono', 'monospace'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

