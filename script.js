/* ============================================================
   SINGULAR MENTORIA — script.js
   ============================================================ */

(function () {
  'use strict';

  /* ----------------------------------------------------------
     NAVBAR — scroll + mobile toggle
  ---------------------------------------------------------- */
  const navbar    = document.getElementById('navbar');
  const navToggle = document.getElementById('navToggle');
  const navLinks  = document.getElementById('navLinks');

  // Add .scrolled class after user scrolls 50px
  function handleNavScroll() {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  }

  window.addEventListener('scroll', handleNavScroll, { passive: true });
  handleNavScroll(); // run on load in case page is already scrolled

  // Mobile hamburger
  navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.classList.toggle('active', isOpen);
    navToggle.setAttribute('aria-expanded', String(isOpen));
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  // Close mobile menu when a link is clicked
  navLinks.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navToggle.classList.remove('active');
      navToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });

  // Close on backdrop click (outside nav-container)
  navLinks.addEventListener('click', e => {
    if (e.target === navLinks) {
      navLinks.classList.remove('open');
      navToggle.classList.remove('active');
      navToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
  });

  /* ----------------------------------------------------------
     ACTIVE NAV LINK — highlight on scroll
  ---------------------------------------------------------- */
  const sections     = document.querySelectorAll('section[id]');
  const allNavLinks  = document.querySelectorAll('.nav-link');

  function updateActiveLink() {
    let currentId = '';
    sections.forEach(sec => {
      const top = sec.offsetTop - 110;
      if (window.scrollY >= top) currentId = sec.getAttribute('id');
    });

    allNavLinks.forEach(link => {
      const href = link.getAttribute('href');
      const isActive = href === `#${currentId}`;
      link.style.color = isActive ? 'var(--text-primary)' : '';
      link.style.background = (isActive && !link.classList.contains('nav-link-cta'))
        ? 'rgba(255,255,255,0.05)' : '';
    });
  }

  window.addEventListener('scroll', updateActiveLink, { passive: true });

  /* ----------------------------------------------------------
     SCROLL REVEAL — IntersectionObserver
  ---------------------------------------------------------- */
  const revealItems = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;

        // Stagger siblings within the same grid/container
        const parent   = entry.target.parentElement;
        const siblings = [...parent.querySelectorAll('.reveal:not(.visible)')];
        const idx      = siblings.indexOf(entry.target);
        const delay    = Math.max(0, idx * 75);

        setTimeout(() => {
          entry.target.classList.add('visible');
        }, delay);

        revealObserver.unobserve(entry.target);
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -48px 0px' }
  );

  revealItems.forEach(el => revealObserver.observe(el));

  /* ----------------------------------------------------------
     CONTACT FORM
  ---------------------------------------------------------- */
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');
  const submitBtn   = document.getElementById('submitBtn');

  if (contactForm) {
    contactForm.addEventListener('submit', e => {
      e.preventDefault();

      // Basic HTML5 validation
      if (!contactForm.checkValidity()) {
        contactForm.reportValidity();
        return;
      }

      // Loading state
      const originalHTML = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="animation:spin .8s linear infinite">
          <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2.5" stroke-dasharray="42" stroke-dashoffset="12" stroke-linecap="round"/>
        </svg>
        Enviando…
      `;

      // Simulate async send (replace with real fetch if needed)
      setTimeout(() => {
        formSuccess.classList.add('visible');
        contactForm.reset();

        submitBtn.innerHTML = originalHTML;
        submitBtn.disabled  = false;

        // Hide success message after 5s
        setTimeout(() => formSuccess.classList.remove('visible'), 5000);
      }, 1100);
    });
  }

  /* ----------------------------------------------------------
     CSS @keyframes spin (for the button spinner)
     Injected once via JS to avoid adding it to the CSS file
  ---------------------------------------------------------- */
  const spinStyle = document.createElement('style');
  spinStyle.textContent = '@keyframes spin { to { transform: rotate(360deg); } }';
  document.head.appendChild(spinStyle);

  /* ----------------------------------------------------------
     SMOOTH SCROLL POLYFILL for anchor links
     (native scroll-behavior handles most cases, this handles edge)
  ---------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  /* ----------------------------------------------------------
     VÍDEO — FULLSCREEN
  ---------------------------------------------------------- */
  const videoFullscreenBtn = document.getElementById('videoFullscreenBtn');
  const videoPlaceholder   = document.getElementById('videoPlaceholder');

  if (videoFullscreenBtn && videoPlaceholder) {
    videoFullscreenBtn.addEventListener('click', () => {
      if (document.fullscreenElement) {
        document.exitFullscreen();
      } else {
        videoPlaceholder.requestFullscreen();
      }
    });

    document.addEventListener('fullscreenchange', () => {
      const isFs = !!document.fullscreenElement;
      videoFullscreenBtn.setAttribute('aria-label', isFs ? 'Sair da tela cheia' : 'Tela cheia');
      videoFullscreenBtn.innerHTML = isFs
        ? `<svg width="16" height="16" viewBox="0 0 24 24" fill="none">
             <path d="M9 3H3V9M15 3H21V9M21 15V21H15M9 21H3V15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
           </svg>`
        : `<svg width="16" height="16" viewBox="0 0 24 24" fill="none">
             <path d="M3 9V3H9M15 3H21V9M21 15V21H15M9 21H3V15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
           </svg>`;
    });
  }

  /* ----------------------------------------------------------
     FAQ ACCORDION
  ---------------------------------------------------------- */
  const faqBtns = document.querySelectorAll('.faq-btn');

  faqBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const isOpen = btn.getAttribute('aria-expanded') === 'true';
      const body   = btn.nextElementSibling;

      faqBtns.forEach(other => {
        other.setAttribute('aria-expanded', 'false');
        other.nextElementSibling.classList.remove('open');
      });

      if (!isOpen) {
        btn.setAttribute('aria-expanded', 'true');
        body.classList.add('open');
      }
    });
  });

  /* ----------------------------------------------------------
     QUIZ
  ---------------------------------------------------------- */
  const allQuestions = [
    {
      q: 'Quanto é 2³ + 3²?',
      options: ['13', '17', '19', '25'],
      correct: 1
    },
    {
      q: 'Uma PA tem primeiro termo 2 e razão 3. Qual é o 5º termo?',
      options: ['11', '12', '14', '17'],
      correct: 2
    },
    {
      q: 'Quais são as raízes de x² − 5x + 6 = 0?',
      options: ['1 e 6', '2 e 3', '−2 e −3', '3 e 5'],
      correct: 1
    },
    {
      q: 'Um triângulo retângulo tem catetos 3 e 4. Qual é a hipotenusa?',
      options: ['4,5', '5', '6', '7'],
      correct: 1
    },
    {
      q: 'Se log₁₀(100) = x, qual é o valor de x?',
      options: ['1', '2', '10', '100'],
      correct: 1
    },
    {
      q: 'Qual é a área de um círculo de raio 5? (use π ≈ 3,14)',
      options: ['15,7', '31,4', '78,5', '157'],
      correct: 2
    },
    {
      q: 'Uma PG tem primeiro termo 3 e razão 2. Qual é o 4º termo?',
      options: ['12', '18', '24', '48'],
      correct: 2
    },
    {
      q: 'Quantos arranjos de 3 elementos existem em um conjunto de 5?',
      options: ['10', '20', '60', '120'],
      correct: 2
    },
    {
      q: 'Qual o valor de sen(30°)?',
      options: ['√2/2', '√3/2', '1/2', '1'],
      correct: 2
    },
    {
      q: 'Uma urna tem 4 bolas vermelhas e 6 azuis. Qual é a probabilidade de sortear uma vermelha?',
      options: ['2/5', '1/4', '3/5', '1/3'],
      correct: 0
    }
  ];

  const QUIZ_SIZE = 5;

  function pickQuestions() {
    const pool = [...allQuestions];
    for (let i = pool.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pool[i], pool[j]] = [pool[j], pool[i]];
    }
    return pool.slice(0, QUIZ_SIZE);
  }

  let quizData = pickQuestions();

  const quizResults = [
    {
      level: 'Iniciante',
      title: 'Boa tentativa!',
      desc: 'A base é o ponto de partida de tudo. A Singular vai te ajudar a construir um alicerce sólido, no seu ritmo e do zero.'
    },
    {
      level: 'Intermediário',
      title: 'Bom desempenho!',
      desc: 'Você tem potencial! Com metodologia personalizada e prática constante, sua nota vai decolar nos próximos meses.'
    },
    {
      level: 'Avançado',
      title: 'Excelente nível!',
      desc: 'Impressionante! Vamos refinar sua estratégia e maximizar sua pontuação para o vestibular dos seus sonhos.'
    }
  ];

  let currentQ = 0;
  let quizScore = 0;

  const quizStartPanel   = document.getElementById('quizStart');
  const quizQPanel       = document.getElementById('quizQuestions');
  const quizResultPanel  = document.getElementById('quizResult');
  const quizStartBtn     = document.getElementById('quizStartBtn');
  const quizRetryBtn     = document.getElementById('quizRetryBtn');
  const quizCounter      = document.getElementById('quizCounter');
  const quizQuestionEl   = document.getElementById('quizQuestionText');
  const quizOptionsEl    = document.getElementById('quizOptionsGrid');
  const quizProgressFill = document.getElementById('quizProgressFill');
  const quizScoreBadge   = document.getElementById('quizScoreBadge');
  const quizResultLevel  = document.getElementById('quizResultLevel');
  const quizResultTitle  = document.getElementById('quizResultTitle');
  const quizResultDesc   = document.getElementById('quizResultDesc');

  function showQuestion() {
    const q = quizData[currentQ];
    quizCounter.textContent = `Questão ${currentQ + 1} de ${QUIZ_SIZE}`;
    quizProgressFill.style.width = `${(currentQ / QUIZ_SIZE) * 100}%`;
    quizQuestionEl.textContent = q.q;
    quizOptionsEl.innerHTML = '';

    q.options.forEach((opt, idx) => {
      const btn = document.createElement('button');
      btn.className = 'quiz-option';
      btn.textContent = opt;
      btn.addEventListener('click', () => pickOption(idx));
      quizOptionsEl.appendChild(btn);
    });
  }

  function pickOption(idx) {
    const buttons = quizOptionsEl.querySelectorAll('.quiz-option');
    buttons.forEach(b => { b.disabled = true; });

    const correct = quizData[currentQ].correct;
    buttons[correct].classList.add('correct');
    if (idx !== correct) buttons[idx].classList.add('wrong');
    else quizScore++;

    setTimeout(() => {
      currentQ++;
      if (currentQ < QUIZ_SIZE) {
        showQuestion();
      } else {
        showResult();
      }
    }, 820);
  }

  function showResult() {
    quizQPanel.classList.add('quiz-hidden');
    quizResultPanel.classList.remove('quiz-hidden');
    quizProgressFill.style.width = '100%';
    quizScoreBadge.textContent = `${quizScore}/${quizData.length}`;

    const idx    = quizScore <= 1 ? 0 : quizScore <= 3 ? 1 : 2;
    const result = quizResults[idx];
    quizResultLevel.textContent = result.level;
    quizResultTitle.textContent = result.title;
    quizResultDesc.textContent  = result.desc;
  }

  function resetQuiz() {
    currentQ  = 0;
    quizScore = 0;
    quizData  = pickQuestions();
    quizResultPanel.classList.add('quiz-hidden');
    quizStartPanel.classList.remove('quiz-hidden');
  }

  if (quizStartBtn) {
    quizStartBtn.addEventListener('click', () => {
      quizStartPanel.classList.add('quiz-hidden');
      quizQPanel.classList.remove('quiz-hidden');
      showQuestion();
    });
  }

  if (quizRetryBtn) {
    quizRetryBtn.addEventListener('click', resetQuiz);
  }

})();
