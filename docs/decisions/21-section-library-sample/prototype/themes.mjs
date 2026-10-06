// PROTOTYPE (#21) — two neutral test themes. Every colour, font, size, space and radius has its value here and only here.
// Colour: scheme (light | dark) × tone (plain | tinted | bold). In dark, "bold" inverts to a light band.
const set = (bg, surface, text, muted, rule, accent, onAccent) => ({ bg, surface, text, muted, rule, accent, onAccent });

export const themes = {
  a: {
    id: 'test-slate', name: { en: 'Test theme A · Slate', th: 'ธีมทดสอบ A · หินชนวน', zh: '测试主题 A · 石板' },
    font: { pairing: 'sans', display: { weight: 700 }, body: { weight: 400 }, ui: { weight: 500, strong: 600 } },
    color: {
      light: {
        plain: set('#f6f7f6', '#ffffff', '#1a1f1d', '#56605b', '#d6dcd9', '#24577f', '#ffffff'),
        tinted: set('#e9eeec', '#ffffff', '#1a1f1d', '#4f5954', '#c9d2ce', '#1f4e73', '#ffffff'),
        bold: set('#1c2a33', '#243540', '#f1f4f2', '#b7c2c8', '#3a4d57', '#9cc8ec', '#0e1e2a'),
      },
      dark: {
        plain: set('#111514', '#181d1b', '#e4e9e6', '#9aa59f', '#2a322e', '#8fbce3', '#0d1a24'),
        tinted: set('#18201e', '#1e2725', '#e4e9e6', '#a0aaa5', '#323c39', '#93c0e6', '#0d1a24'),
        bold: set('#d8e3ea', '#c8d6df', '#13202a', '#3c4a54', '#afc0cb', '#1e4c70', '#ffffff'),
      },
    },
    size: {
      'display-xl': 'clamp(2.4rem, 1.3rem + 4.6cqi, 4.25rem)', 'display-1': 'clamp(2rem, 1.25rem + 3.2cqi, 3.25rem)',
      h2: 'clamp(1.55rem, 1.2rem + 1.5cqi, 2.15rem)', h3: '1.2rem', lead: '1.1875rem', body: '1.0625rem', ui: '.9375rem', small: '.8125rem',
      figure: 'clamp(2rem, 1.5rem + 2.2cqi, 2.75rem)',
    },
    space: { 1: '.25rem', 2: '.5rem', 3: '.75rem', 4: '1rem', 5: '1.5rem', 6: '2rem', 7: '3rem', 8: '4rem', section: 'clamp(3rem, 2rem + 5cqi, 6rem)', gutter: 'clamp(1rem, .5rem + 3cqi, 2.5rem)' },
    radius: { control: '.375rem', card: '.5rem', media: '.5rem' },
    measure: { page: '72rem' },
    eyebrow: { transform: 'uppercase', tracking: '.08em' },
  },
  b: {
    id: 'test-paper', name: { en: 'Test theme B · Paper', th: 'ธีมทดสอบ B · กระดาษ', zh: '测试主题 B · 纸张' },
    font: { pairing: 'serif', display: { weight: 600 }, body: { weight: 400 }, ui: { weight: 500, strong: 600 } },
    color: {
      light: {
        plain: set('#fbfaf7', '#ffffff', '#23211d', '#625d55', '#e1dcd3', '#2e5b4e', '#ffffff'),
        tinted: set('#f1eee7', '#fbfaf7', '#23211d', '#5c574f', '#d8d2c6', '#2a5447', '#ffffff'),
        bold: set('#23302b', '#2c3b35', '#f3f1ec', '#bdc6c0', '#3e4d47', '#b9d6c6', '#15241e'),
      },
      dark: {
        plain: set('#141412', '#1c1b19', '#ece8e1', '#a8a196', '#2e2c28', '#9cc9b5', '#10201a'),
        tinted: set('#1c1b18', '#23221f', '#ece8e1', '#aba499', '#36342f', '#a2cdb9', '#10201a'),
        bold: set('#e7e2d8', '#dcd6ca', '#1f1d19', '#4f4a42', '#ccc5b7', '#2a5447', '#ffffff'),
      },
    },
    size: {
      'display-xl': 'clamp(2.6rem, 1.3rem + 5.4cqi, 4.75rem)', 'display-1': 'clamp(2.2rem, 1.3rem + 3.8cqi, 3.6rem)',
      h2: 'clamp(1.7rem, 1.25rem + 1.9cqi, 2.4rem)', h3: '1.3rem', lead: '1.25rem', body: '1.0625rem', ui: '.9375rem', small: '.8125rem',
      figure: 'clamp(2.2rem, 1.6rem + 2.6cqi, 3.1rem)',
    },
    space: { 1: '.25rem', 2: '.5rem', 3: '.75rem', 4: '1rem', 5: '1.75rem', 6: '2.5rem', 7: '3.5rem', 8: '5rem', section: 'clamp(3.5rem, 2rem + 6.5cqi, 7.5rem)', gutter: 'clamp(1rem, .5rem + 3.5cqi, 3rem)' },
    radius: { control: '0', card: '0', media: '0' },
    measure: { page: '68rem' },
    eyebrow: { transform: 'none', tracking: '0' },
  },
};
