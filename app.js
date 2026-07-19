const root = document.documentElement;
const themeButton = document.querySelector('.theme-toggle');
const navButton = document.querySelector('.nav-toggle');
const nav = document.querySelector('#site-nav');
const toast = document.querySelector('.toast');

function setTheme(theme) {
  root.dataset.theme = theme;
  themeButton.textContent = theme === 'dark' ? 'Light' : 'Dark';
  localStorage.setItem('haichi-site-theme', theme);
}

setTheme(localStorage.getItem('haichi-site-theme') || 'light');

themeButton.addEventListener('click', () => {
  setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
});

navButton.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  navButton.setAttribute('aria-expanded', String(open));
});

nav.addEventListener('click', event => {
  if (event.target.matches('a')) {
    nav.classList.remove('open');
    navButton.setAttribute('aria-expanded', 'false');
  }
});

document.querySelectorAll('.faq-list details').forEach(item => {
  item.addEventListener('toggle', () => {
    if (!item.open) return;
    document.querySelectorAll('.faq-list details').forEach(other => {
      if (other !== item) other.open = false;
    });
  });
});

document.querySelectorAll('.copy-workflow').forEach(btn => {
  btn.addEventListener('click', async event => {
    const target = document.querySelector(event.currentTarget.dataset.copyTarget);
    const text = target?.textContent?.trim() || '';
    try {
      await navigator.clipboard.writeText(text);
      toast.textContent = 'Starter task copied';
    } catch {
      toast.textContent = 'Select and copy the starter task above';
    }
    toast.classList.add('show');
    window.setTimeout(() => toast.classList.remove('show'), 2200);
  });
});

document.querySelector('#year').textContent = new Date().getFullYear();
