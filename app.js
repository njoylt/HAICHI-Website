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
const campaignAttribution = {
  source: attributionValue(pageParams.get('utm_source'), 'direct'),
  medium: attributionValue(pageParams.get('utm_medium'), 'none'),
  campaign: attributionValue(pageParams.get('utm_campaign'), 'haichi_site_v1_2_personal'),
  content: attributionValue(pageParams.get('utm_content'), 'landing'),
  term: attributionValue(pageParams.get('utm_term'), 'none'),
};

window.dataLayer = window.dataLayer || [];

function trackEvent(name, properties = {}) {
  const payload = {
    event: 'haichi_conversion',
    haichi_event: name,
    page_path: window.location.pathname,
    ...campaignAttribution,
    ...properties,
  };

  window.dataLayer.push(payload);
  window.dispatchEvent(new CustomEvent('haichi:measurement', { detail: payload }));

  if (pageParams.get('measurement_debug') === '1') {
    console.info('[HAICHI measurement]', payload);
  }
}

trackEvent('page_view');

document.querySelectorAll('a[href^="https://haichi.lemonsqueezy.com/checkout/"]').forEach(link => {
  const checkoutUrl = new URL(link.href);
  const edition = attributionValue(link.dataset.edition, 'unknown');
  const placement = attributionValue(link.dataset.placement, 'unknown');

  checkoutUrl.searchParams.set('checkout[custom][source]', campaignAttribution.source);
  checkoutUrl.searchParams.set('checkout[custom][medium]', campaignAttribution.medium);
  checkoutUrl.searchParams.set('checkout[custom][campaign]', campaignAttribution.campaign);
  checkoutUrl.searchParams.set('checkout[custom][creative]', campaignAttribution.content);
  checkoutUrl.searchParams.set('checkout[custom][term]', campaignAttribution.term);
  checkoutUrl.searchParams.set('checkout[custom][landing_version]', 'v1_2_personal_release');
  checkoutUrl.searchParams.set('checkout[custom][edition]', edition);
  checkoutUrl.searchParams.set('checkout[custom][cta_placement]', placement);
  link.href = checkoutUrl.toString();

  link.addEventListener('click', () => {
    trackEvent('checkout_click', { edition, placement });
  });
});

document.querySelectorAll('[data-track]:not([href^="https://haichi.lemonsqueezy.com/checkout/"])').forEach(element => {
  element.addEventListener('click', () => {
    trackEvent(attributionValue(element.dataset.track, 'interaction'), {
      placement: attributionValue(element.dataset.placement, 'unknown'),
    });
  });
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

document.querySelectorAll('.copy-workflow').forEach(btn => {
  btn.addEventListener('click', async event => {
    const sourceSelector = event.currentTarget.dataset.copyTarget;
    const target = sourceSelector ? document.querySelector(sourceSelector) : null;
    const text = event.currentTarget.dataset.copyText || target?.textContent?.trim() || '';
    const successMessage = event.currentTarget.dataset.copyLabel || 'Text copied';
    const fallbackMessage = event.currentTarget.dataset.copyFallback || 'Select and copy the text above';
    try {
      await navigator.clipboard.writeText(text);
      toast.textContent = successMessage;
      trackEvent('copy_action', { label: attributionValue(successMessage, 'copy') });
    } catch {
      toast.textContent = fallbackMessage;
      trackEvent('copy_fallback', { label: attributionValue(fallbackMessage, 'copy') });
    }
    toast.classList.add('show');
    window.setTimeout(() => toast.classList.remove('show'), 2200);
  });
});

document.querySelector('#year').textContent = new Date().getFullYear();

window.haichiMeasurement = Object.freeze({ track: trackEvent, attribution: campaignAttribution });
