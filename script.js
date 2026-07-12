// Devakkumar Sheth — Portfolio Scripts

(function () {
  'use strict';

  // Header scroll effect
  const header = document.getElementById('header');
  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile nav toggle
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.classList.toggle('open', isOpen);
    navToggle.setAttribute('aria-expanded', isOpen);
  });

  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navToggle.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });

  // Scroll reveal
  const revealEls = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );
  revealEls.forEach((el) => revealObserver.observe(el));

  // Stagger project cards
  document.querySelectorAll('.project-card.reveal').forEach((card, i) => {
    card.style.transitionDelay = `${(i % 3) * 0.1}s`;
  });

  // Project filter tabs
  const filterTabs = document.querySelectorAll('.filter-tab');
  const projectCards = document.querySelectorAll('.project-card');

  filterTabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      filterTabs.forEach((t) => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.dataset.filter;

      projectCards.forEach((card) => {
        if (filter === 'all') {
          card.classList.remove('hidden');
          return;
        }
        const categories = card.dataset.category.split(' ');
        card.classList.toggle('hidden', !categories.includes(filter));
      });
    });
  });

  // Active nav link on scroll
  const sections = document.querySelectorAll('section[id]');
  const navItems = document.querySelectorAll('.nav__links a[href^="#"]');

  const sectionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navItems.forEach((link) => {
            link.style.color =
              link.getAttribute('href') === `#${id}`
                ? 'var(--text)'
                : '';
          });
        }
      });
    },
    { threshold: 0.3, rootMargin: '-80px 0px -50% 0px' }
  );

  sections.forEach((section) => sectionObserver.observe(section));

  // Resume download — tries PDF first, falls back to online resume page
  const RESUME_FILES = ['Devakkumar_Sheth_Resume.pdf', 'resume.pdf'];
  const RESUME_NAME = 'Devakkumar_Sheth_Resume.pdf';

  async function downloadResume(event) {
    event.preventDefault();

    for (const file of RESUME_FILES) {
      try {
        const response = await fetch(file, { cache: 'no-store' });
        if (!response.ok) continue;

        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = RESUME_NAME;
        document.body.appendChild(link);
        link.click();
        link.remove();
        URL.revokeObjectURL(url);
        return;
      } catch {
        // try next file
      }
    }

    window.open('resume.html', '_blank', 'noopener');
  }

  document.querySelectorAll('.js-download-resume').forEach((el) => {
    el.addEventListener('click', downloadResume);
  });
})();
