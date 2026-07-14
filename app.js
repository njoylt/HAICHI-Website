const root = document.documentElement;
const themeButton = document.querySelector('.theme-toggle');
const navButton = document.querySelector('.nav-toggle');
const nav = document.querySelector('#site-nav');
const toast = document.querySelector('.toast');

function attributionValue(value, fallback) {
  const normalized = (value || '').trim().toLowerCase().replace(/[^a-z0-9_-]+/g, '_');
  return normalized.slice(0, 60) || fallback;
}

const pageParams = new URLSearchParams(window.location.search);
const checkoutAttribution = {
  source: attributionValue(pageParams.get('utm_source'), 'haichi_site'),
  campaign: attributionValue(pageParams.get('utm_campaign'), 'one_local_workflow'),
};

document.querySelectorAll('a[href^="https://haichi.lemonsqueezy.com/checkout/"]').forEach(link => {
  const checkoutUrl = new URL(link.href);
  checkoutUrl.searchParams.set('checkout[custom][source]', checkoutAttribution.source);
  checkoutUrl.searchParams.set('checkout[custom][campaign]', checkoutAttribution.campaign);
  checkoutUrl.searchParams.set('checkout[custom][landing_version]', 'v1_1_one_local_workflow');
  link.href = checkoutUrl.toString();
});

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

document.querySelectorAll('.copy-install').forEach(btn => {
  btn.addEventListener('click', async event => {
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
});

document.querySelector('#year').textContent = new Date().getFullYear();
