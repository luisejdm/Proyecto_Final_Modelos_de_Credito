(() => {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ===== Mobile nav toggle =====
  const toggle = document.getElementById('navToggle');
  const links = document.getElementById('navLinks');

  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('is-open');
      toggle.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
    });

    links.querySelectorAll('a').forEach((a) => {
      a.addEventListener('click', () => {
        links.classList.remove('is-open');
        toggle.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ===== Footer year =====
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // ===== Navbar scroll state =====
  const navbar = document.getElementById('navbar');
  const scrollTopBtn = document.getElementById('scrollTop');

  const onScroll = () => {
    const y = window.scrollY;
    if (navbar) navbar.classList.toggle('is-scrolled', y > 20);
    if (scrollTopBtn) scrollTopBtn.classList.toggle('is-visible', y > 600);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
    });
  }

  // ===== Reveal on scroll =====
  const reveals = document.querySelectorAll('[data-reveal]');
  if (reveals.length && !prefersReducedMotion && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const delay = parseInt(el.getAttribute('data-reveal-delay') || '0', 10);
          el.style.transitionDelay = `${delay}ms`;
          el.classList.add('is-visible');
          io.unobserve(el);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    reveals.forEach((el) => io.observe(el));
  } else {
    // Reduced motion or no IO: show all immediately
    reveals.forEach((el) => el.classList.add('is-visible'));
  }

  // ===== Animated number counters =====
  const counters = document.querySelectorAll('[data-count]');
  const animateCount = (el) => {
    const target = parseFloat(el.getAttribute('data-count'));
    const suffix = el.getAttribute('data-suffix') || '';
    const decimals = (el.getAttribute('data-count').split('.')[1] || '').length;
    const duration = 1600;
    const start = performance.now();

    const tick = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      // ease-out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = target * eased;
      el.textContent = current.toLocaleString('en-US', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
      }) + suffix;
      if (progress < 1) requestAnimationFrame(tick);
      else el.textContent = target.toLocaleString('en-US', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
      }) + suffix;
    };
    requestAnimationFrame(tick);
  };

  if (counters.length && !prefersReducedMotion && 'IntersectionObserver' in window) {
    const cio = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          cio.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach((c) => cio.observe(c));
  } else {
    counters.forEach((el) => {
      const target = parseFloat(el.getAttribute('data-count'));
      const suffix = el.getAttribute('data-suffix') || '';
      const decimals = (el.getAttribute('data-count').split('.')[1] || '').length;
      el.textContent = target.toLocaleString('en-US', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
      }) + suffix;
    });
  }

  // ===== Subtle parallax for hero photo on mouse move =====
  const heroWrap = document.querySelector('.hero-photo-wrap');
  if (heroWrap && !prefersReducedMotion && window.matchMedia('(hover: hover)').matches) {
    const photo = heroWrap.querySelector('.hero-photo');
    const cards = heroWrap.querySelectorAll('.float-card');
    let rect;

    heroWrap.addEventListener('mouseenter', () => {
      rect = heroWrap.getBoundingClientRect();
    });

    heroWrap.addEventListener('mousemove', (e) => {
      if (!rect) rect = heroWrap.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
      const y = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
      if (photo) photo.style.transform = `translate(${x * 6}px, ${y * 6}px)`;
      cards.forEach((c, i) => {
        const depth = (i + 1) * 4;
        c.style.transform = `translate(${x * depth}px, ${y * depth}px)`;
      });
    });

    heroWrap.addEventListener('mouseleave', () => {
      if (photo) photo.style.transform = '';
      cards.forEach((c) => { c.style.transform = ''; });
      rect = null;
    });
  }
})();
