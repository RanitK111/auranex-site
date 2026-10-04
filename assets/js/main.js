(function () {
  var btn = document.getElementById('menu-btn');
  var nav = document.getElementById('nav-list');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Cookie / embed notice
  var box = document.getElementById('cookie');
  var KEY = 'auranex_cookie_notice';
  var seen = false;
  try { seen = localStorage.getItem(KEY) === '1'; } catch (e) {}
  if (box && !seen) {
    box.style.display = 'block';
    box.querySelector('[data-ok]').addEventListener('click', function () {
      try { localStorage.setItem(KEY, '1'); } catch (e) {}
      box.style.display = 'none';
    });
  }

  // Demo page: only load Calendly after the visitor asks for it
  var load = document.getElementById('load-cal');
  if (load) {
    load.addEventListener('click', function () {
      var holder = document.getElementById('cal-holder');
      holder.innerHTML = '<iframe src="https://calendly.com/kkgmedia1/30min?hide_gdpr_banner=1&background_color=ffffff" title="Book a demo" loading="lazy"></iframe>';
      load.style.display = 'none';
    });
  }
})();
