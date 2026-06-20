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

setTheme(localStorage.getItem('haichi-site-theme') || 'dark');

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

document.querySelector('.copy-install').addEventListener('click', async event => {
  const command = event.currentTarget.dataset.command;
  try {
    await navigator.clipboard.writeText(command);
    toast.textContent = 'Install command copied';
  } catch {
    toast.textContent = `Install command: ${command}`;
  }
  toast.classList.add('show');
  window.setTimeout(() => toast.classList.remove('show'), 2200);
});

document.querySelector('#year').textContent = new Date().getFullYear();
