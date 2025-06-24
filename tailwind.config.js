/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./about-us/*.html",
    "./portfolio/*.html",
    "./clients/*.html",
    "./contact/*.html",
    "./film-production-services/*.html",
    "./filming-in-greece/*.html",
    "./equipment-rental-greece/*.html",
    "./location-scouting-greece/*.html",
    "./film-permits-greece/*.html"
  ],
  theme: {
    extend: {
      colors: {
        'greece': {
          'blue': '#f9a531',
          'white': '#ffffff',
          'dark': '#1c1c1c',
          'darker': '#0a0a0a',
          'gray': '#b4b4b4'
        }
      },
      fontFamily: {
        'sans': ['Open Sans', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        'heading': ['Open Sans', 'system-ui', 'sans-serif']
      },
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
        '5xl': ['3rem', { lineHeight: '1' }],
        '6xl': ['3.75rem', { lineHeight: '1' }],
        '7xl': ['4.5rem', { lineHeight: '1' }],
        '8xl': ['6rem', { lineHeight: '1' }],
        '9xl': ['8rem', { lineHeight: '1' }]
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem'
      },
      maxWidth: {
        '8xl': '88rem',
        '9xl': '96rem'
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-in-left': 'slideInLeft 0.5s ease-out',
        'slide-in-right': 'slideInRight 0.5s ease-out',
        'slide-up': 'slideUp 0.5s ease-out',
        'bounce-slow': 'bounce 2s infinite',
        'pulse-slow': 'pulse 3s infinite'
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        slideInLeft: {
          '0%': { transform: 'translateX(-100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' }
        },
        slideInRight: {
          '0%': { transform: 'translateX(100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' }
        },
        slideUp: {
          '0%': { transform: 'translateY(100%)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        }
      },
      backdropBlur: {
        'xs': '2px'
      },
      boxShadow: {
        'greece': '0 4px 6px -1px rgba(249, 165, 49, 0.1), 0 2px 4px -1px rgba(249, 165, 49, 0.06)',
        'greece-lg': '0 10px 15px -3px rgba(249, 165, 49, 0.1), 0 4px 6px -2px rgba(249, 165, 49, 0.05)',
        'greece-xl': '0 20px 25px -5px rgba(249, 165, 49, 0.1), 0 10px 10px -5px rgba(249, 165, 49, 0.04)',
        'glow': '0 0 20px rgba(249, 165, 49, 0.3)',
        'glow-lg': '0 0 40px rgba(249, 165, 49, 0.4)'
      },
      gradientColorStops: {
        'greece-blue': '#f9a531',
        'greece-white': '#ffffff'
      }
    }
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    // Custom plugin for Greece-specific utilities
    function({ addUtilities, theme }) {
      const newUtilities = {
        '.text-gradient-greece': {
          'background': 'linear-gradient(135deg, #f9a531 0%, #ffffff 100%)',
          '-webkit-background-clip': 'text',
          '-webkit-text-fill-color': 'transparent',
          'background-clip': 'text'
        },
        '.bg-gradient-greece': {
          'background': 'linear-gradient(135deg, #f9a531 0%, #ffffff 100%)'
        },
        '.bg-gradient-greece-dark': {
          'background': 'linear-gradient(135deg, #1c1c1c 0%, #0a0a0a 100%)'
        },
        '.hover-lift': {
          'transition': 'transform 0.3s ease-in-out',
          '&:hover': {
            'transform': 'translateY(-4px)'
          }
        },
        '.hover-scale': {
          'transition': 'transform 0.3s ease-in-out',
          '&:hover': {
            'transform': 'scale(1.05)'
          }
        },
        '.glass-effect': {
          'background': 'rgba(28, 28, 28, 0.8)',
          'backdrop-filter': 'blur(20px)',
          '-webkit-backdrop-filter': 'blur(20px)',
          'border': '1px solid rgba(255, 255, 255, 0.1)'
        }
      }
      addUtilities(newUtilities)
    }
  ],
  darkMode: 'class'
}
