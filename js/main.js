document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initDropdowns();
  initCustomServiceSlider();
  initProjectTabs();
  initFAQAccordion();
  initVideoControls();
  initForms();
  initScrollAnimations();
  initSmoothScroll();
});

function initMobileNav() {
  const navbar = document.querySelector('.navbar');
  const menuBtn = document.querySelector('.w-nav-button');
  if (!navbar || !menuBtn) return;

  menuBtn.addEventListener('click', () => {
    navbar.classList.toggle('w--nav-menu-open');
    menuBtn.classList.toggle('w--open');
  });

  document.addEventListener('click', (e) => {
    if (!navbar.contains(e.target)) {
      navbar.classList.remove('w--nav-menu-open');
      menuBtn.classList.remove('w--open');
    }
  });
}

function initDropdowns() {
  document.querySelectorAll('.dropdown').forEach((dropdown) => {
    const toggle = dropdown.querySelector('.w-dropdown-toggle');
    if (!toggle) return;

    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const isOpen = dropdown.classList.contains('w--open');
      document.querySelectorAll('.dropdown.w--open').forEach((d) => d.classList.remove('w--open'));
      if (!isOpen) dropdown.classList.add('w--open');
    });
  });

  document.addEventListener('click', () => {
    document.querySelectorAll('.dropdown.w--open').forEach((d) => d.classList.remove('w--open'));
  });
}

function initCustomServiceSlider() {
  const slider = document.querySelector('.custom-services-section');
  if (!slider) return;

  const track = slider.querySelector('.custom-slider-track');
  const cards = slider.querySelectorAll('.custom-slider-card');
  const prevBtn = slider.querySelector('.custom-arrow.prev');
  const nextBtn = slider.querySelector('.custom-arrow.next');
  const dotsContainer = slider.querySelector('.custom-slider-dots');
  
  let currentIndex = 0;
  const totalCards = cards.length;
  
  function getVisibleCardsCount() {
    if (window.innerWidth <= 767) return 1;
    return 2;
  }
  
  function getMaxIndex() {
    return Math.max(0, totalCards - getVisibleCardsCount());
  }

  function buildDots() {
    if (!dotsContainer) return;
    dotsContainer.innerHTML = '';
    const dotsCount = getMaxIndex() + 1;
    
    for (let i = 0; i < dotsCount; i++) {
      const dot = document.createElement('div');
      dot.className = `w-slider-dot${i === currentIndex ? ' w-active' : ''}`;
      dot.addEventListener('click', () => goTo(i));
      dotsContainer.appendChild(dot);
    }
  }

  function goTo(index) {
    const maxIndex = getMaxIndex();
    currentIndex = Math.min(Math.max(0, index), maxIndex);
    
    const cardWidth = cards[0].getBoundingClientRect().width;
    const offset = currentIndex * (cardWidth + 24); // 24px is card gap
    track.style.transform = `translateX(-${offset}px)`;
    
    if (dotsContainer) {
      const dots = dotsContainer.querySelectorAll('.w-slider-dot');
      dots.forEach((dot, idx) => {
        if (idx === currentIndex) {
          dot.classList.add('w-active');
        } else {
          dot.classList.remove('w-active');
        }
      });
    }
  }

  if (prevBtn) prevBtn.addEventListener('click', () => goTo(currentIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => goTo(currentIndex + 1));

  let startX = 0;
  let isSwiping = false;
  
  track.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
    isSwiping = true;
  }, { passive: true });
  
  track.addEventListener('touchend', (e) => {
    if (!isSwiping) return;
    const diff = startX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {
      goTo(diff > 0 ? currentIndex + 1 : currentIndex - 1);
    }
    isSwiping = false;
  });

  window.addEventListener('resize', () => {
    buildDots();
    goTo(0);
  });

  buildDots();
  goTo(0);
}

function initProjectTabs() {
  const tabMenu = document.querySelector('.project-main-tab .w-tab-menu');
  if (!tabMenu) return;

  const links = tabMenu.querySelectorAll('.w-tab-link');
  const panes = document.querySelectorAll('.project-teb-content .w-tab-pane');

  links.forEach((link, i) => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      links.forEach((l) => l.classList.remove('w--current'));
      panes.forEach((p) => p.classList.remove('w--tab-active'));
      link.classList.add('w--current');
      if (panes[i]) panes[i].classList.add('w--tab-active');
    });
  });
}

function initFAQAccordion() {
  document.querySelectorAll('.accordion-item').forEach((item) => {
    const toggle = item.querySelector('.w-dropdown-toggle');
    if (!toggle) return;

    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const isOpen = item.classList.contains('w--open');
      document.querySelectorAll('.accordion-item.w--open').forEach((el) => el.classList.remove('w--open'));
      if (!isOpen) item.classList.add('w--open');
    });
  });
}

function initVideoControls() {
  document.querySelectorAll('[data-w-bg-video-control]').forEach((btn) => {
    const videoId = btn.getAttribute('aria-controls');
    const video = document.getElementById(videoId);
    if (!video) return;

    btn.addEventListener('click', () => {
      if (video.paused) {
        video.play();
        btn.querySelector('span:first-child').hidden = true;
        btn.querySelector('span:last-child').hidden = false;
      } else {
        video.pause();
        btn.querySelector('span:first-child').hidden = false;
        btn.querySelector('span:last-child').hidden = true;
      }
    });
  });
}

function initForms() {
  document.querySelectorAll('.w-form').forEach((formBlock) => {
    const form = formBlock.querySelector('form');
    const done = formBlock.querySelector('.w-form-done');
    const fail = formBlock.querySelector('.w-form-fail');
    if (!form) return;

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let valid = true;
      form.querySelectorAll('[required]').forEach((field) => {
        if (!field.value.trim()) valid = false;
      });

      if (valid) {
        if (done) { done.classList.add('show'); if (fail) fail.classList.remove('show'); }
        form.reset();
        setTimeout(() => done && done.classList.remove('show'), 4000);
      } else if (fail) {
        fail.classList.add('show');
        if (done) done.classList.remove('show');
      }
    });
  });
}

function initScrollAnimations() {
  const targets = document.querySelectorAll(
    '.hero-heading, .hero-tagline, .hero-content-left, .hero-coustomer-counter-card, .about-image-block, .about-video-content-block, .contact-image-block, .contact-right-block, .fade-in'
  );

  targets.forEach((el) => {
    if (!el.classList.contains('fade-in')) el.classList.add('fade-in');
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  targets.forEach((el) => observer.observe(el));
}

function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href');
      if (!id || id === '#') return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      document.querySelector('.navbar')?.classList.remove('w--nav-menu-open');
      document.querySelector('.w-nav-button')?.classList.remove('w--open');
    });
  });
}
