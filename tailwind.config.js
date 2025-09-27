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

      colors: {
        // These colors map to the CSS variables defined in main.css
        background: 'rgb(var(--color-background) / <alpha-value>)',
        'text-primary': 'rgb(var(--color-text-primary) / <alpha-value>)',
        'text-secondary': 'rgb(var(--color-text-secondary) / <alpha-value>)',
        'link-primary': 'rgb(var(--color-link-primary) / <alpha-value>)',
        'link-hover': 'rgb(var(--color-link-hover) / <alpha-value>)',
        border: 'rgb(var(--color-border) / <alpha-value>)',
      },
      // Configure the typography plugin to use our theme colors
      typography: ({ theme }) => ({
        DEFAULT: {
          css: {
            '--tw-prose-body': 'rgb(var(--color-text-secondary))',
            '--tw-prose-headings': 'rgb(var(--color-text-primary))',
            '--tw-prose-lead': 'rgb(var(--color-text-secondary))',
            '--tw-prose-links': 'rgb(var(--color-link-primary))',
            '--tw-prose-bold': 'rgb(var(--color-text-primary))',
            '--tw-prose-counters': 'rgb(var(--color-text-secondary))',
            '--tw-prose-bullets': 'rgb(var(--color-text-secondary))',
            '--tw-prose-hr': 'rgb(var(--color-border))',
            '--tw-prose-quotes': 'rgb(var(--color-text-primary))',
            '--tw-prose-quote-borders': 'rgb(var(--color-border))',
            '--tw-prose-captions': 'rgb(var(--color-text-secondary))',
            '--tw-prose-code': 'rgb(var(--color-text-primary))',
            '--tw-prose-pre-code': 'rgb(var(--color-text-primary))',
            '--tw-prose-pre-bg': 'rgba(var(--color-border), 0.1)',
            '--tw-prose-th-borders': 'rgb(var(--color-border))',
            '--tw-prose-td-borders': 'rgb(var(--color-border))',
          },
        },
      }),

    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

