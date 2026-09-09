/**
 * 딱1분 오늘의 맞춤법 퀴즈 - App Controller
 * UI 인터랙션, 콘페티 애니메이션, 통계 모달, 애드센스 트리거
 */

(function() {
  'use strict';

  // State
  let currentQuiz = null;
  let selectedChoice = null;
  let isBonusMode = false;
  let isSubmitting = false;

  // DOM Elements
  const questionTextEl = document.getElementById('question-text');
  const optionBtnA = document.getElementById('option-btn-a');
  const optionBtnB = document.getElementById('option-btn-b');
  const optionTextA = document.getElementById('option-text-a');
  const optionTextB = document.getElementById('option-text-b');
  const confirmAnswerBtn = document.getElementById('confirm-answer-btn');
  
  const resultSection = document.getElementById('result-section');
  const resultBanner = document.getElementById('result-banner');
  const resultIcon = document.getElementById('result-icon');
  const resultTitle = document.getElementById('result-title');
  const resultSubtitle = document.getElementById('result-subtitle');
  const explanationBody = document.getElementById('explanation-body');
  const tipText = document.getElementById('tip-text');

  const quizIndexIndicator = document.getElementById('quiz-index-indicator');
  const quizCategoryTag = document.getElementById('quiz-category-tag');
  const todayDateText = document.getElementById('today-date-text');
  const streakCountDisplay = document.getElementById('streak-count-display');
  const modeBanner = document.getElementById('mode-banner');
  const returnTodayQuizBtn = document.getElementById('return-today-quiz-btn');

  const shareQuizBtn = document.getElementById('share-quiz-btn');
  const installPwaBtn = document.getElementById('install-pwa-btn');
  const bonusQuizBtn = document.getElementById('bonus-quiz-btn');

  // Stats Modal Elements
  const streakTriggerBtn = document.getElementById('streak-trigger-btn');
  const statsModalOpenBtn = document.getElementById('stats-modal-open-btn');
  const statsModal = document.getElementById('stats-modal');
  const statsModalCloseBtn = document.getElementById('stats-modal-close-btn');
  const modalConfirmBtn = document.getElementById('modal-confirm-btn');

  const statCurrentStreak = document.getElementById('stat-current-streak');
  const statMaxStreak = document.getElementById('stat-max-streak');
  const statTotalSolved = document.getElementById('stat-total-solved');
  const statAccuracy = document.getElementById('stat-accuracy');

  /**
   * Initialize App
   */
  async function initApp() {
    registerServiceWorker();
    setupEventListeners();
    updateDateDisplay();

    try {
      await window.QuizEngine.init();
      loadTodayQuiz();
      updateStreakUI();
    } catch (err) {
      questionTextEl.textContent = '퀴즈 데이터를 불러오는 중 오류가 발생했습니다. 새로고침해 주세요.';
      console.error(err);
    }
  }

  /**
   * Register Service Worker
   */
  function registerServiceWorker() {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('./sw.js')
        .then(() => console.log('SW registered'))
        .catch((err) => console.warn('SW registration failed:', err));
    }
  }

  /**
   * Format & Display Current Date
   */
  function updateDateDisplay() {
    const now = new Date();
    const days = ['일', '월', '화', '수', '목', '금', '토'];
    const y = now.getFullYear();
    const m = String(now.getMonth() + 1).padStart(2, '0');
    const d = String(now.getDate()).padStart(2, '0');
    const dayName = days[now.getDay()];

    const span = todayDateText.querySelector('span');
    if (span) {
      span.textContent = `${y}.${m}.${d} (${dayName})`;
    }
  }

  /**
   * Update Streak badge and header pill
   */
  function updateStreakUI() {
    const stats = window.QuizEngine.getStats();
    streakCountDisplay.textContent = `${stats.currentStreak}일`;
  }

  /**
   * Load and render Today's Quiz
   */
  function loadTodayQuiz() {
    isBonusMode = false;
    modeBanner.classList.remove('active');

    currentQuiz = window.QuizEngine.getTodayQuiz();
    if (!currentQuiz) return;

    renderQuizView(currentQuiz, false);

    // Check if already solved today
    if (window.QuizEngine.hasSolvedToday()) {
      restoreSolvedTodayState();
    }
  }

  /**
   * Render Quiz into UI
   */
  function renderQuizView(quiz, isBonus) {
    selectedChoice = null;
    isSubmitting = false;

    // Reset buttons
    optionBtnA.disabled = false;
    optionBtnB.disabled = false;
    optionBtnA.className = 'option-btn';
    optionBtnB.className = 'option-btn';
    optionBtnA.setAttribute('aria-checked', 'false');
    optionBtnB.setAttribute('aria-checked', 'false');

    // Confirm button reset
    confirmAnswerBtn.disabled = true;
    confirmAnswerBtn.innerHTML = '<span>선택지를 골라주세요</span>';

    // Hide result section
    resultSection.classList.remove('active');

    // Quiz Category & Number
    quizCategoryTag.textContent = quiz.category || '맞춤법';
    if (isBonus) {
      quizIndexIndicator.textContent = `보너스 문제 #${quiz.id} / 1,825`;
    } else {
      quizIndexIndicator.textContent = `오늘의 문제 #${quiz.id} / 1,825`;
    }

    // Question Text with highlighted brackets
    const formattedQuestion = quiz.question.replace(/\[(.*?)\]/g, '<span class="highlight-slot">[$1]</span>');
    questionTextEl.innerHTML = formattedQuestion;

    // Option texts
    optionTextA.textContent = quiz.optionA;
    optionTextB.textContent = quiz.optionB;
  }

  /**
   * Restore solved state if user returns on the same day
   */
  function restoreSolvedTodayState() {
    const state = window.QuizEngine.state;
    const userChoice = state.todayChoice;
    const isCorrect = state.todayIsCorrect;

    // Disable choices
    optionBtnA.disabled = true;
    optionBtnB.disabled = true;

    // Highlight correct & chosen options
    if (userChoice === 'A') {
      optionBtnA.classList.add(isCorrect ? 'is-correct' : 'is-wrong');
      if (!isCorrect) optionBtnB.classList.add('is-correct');
    } else if (userChoice === 'B') {
      optionBtnB.classList.add(isCorrect ? 'is-correct' : 'is-wrong');
      if (!isCorrect) optionBtnA.classList.add('is-correct');
    }

    // Reveal explanation
    showResultExplanation(currentQuiz, isCorrect, true);

    confirmAnswerBtn.disabled = true;
    confirmAnswerBtn.innerHTML = '<span>오늘의 문제 풀이 완료 ✨</span>';
  }

  /**
   * Select Option A or B
   */
  function selectOption(choice) {
    if (isSubmitting || (window.QuizEngine.hasSolvedToday() && !isBonusMode)) return;

    selectedChoice = choice;

    optionBtnA.classList.toggle('selected', choice === 'A');
    optionBtnB.classList.toggle('selected', choice === 'B');
    optionBtnA.setAttribute('aria-checked', choice === 'A');
    optionBtnB.setAttribute('aria-checked', choice === 'B');

    confirmAnswerBtn.disabled = false;
    const choiceText = (choice === 'A') ? currentQuiz.optionA : currentQuiz.optionB;
    confirmAnswerBtn.innerHTML = `<span>'${choiceText}' 정답 확인하기</span>`;
  }

  /**
   * Handle Answer Submission
   */
  function submitAnswer() {
    if (!selectedChoice || !currentQuiz || isSubmitting) return;

    isSubmitting = true;
    optionBtnA.disabled = true;
    optionBtnB.disabled = true;

    // Record answer in engine
    const recordResult = window.QuizEngine.recordAnswer(currentQuiz, selectedChoice, isBonusMode);
    const isCorrect = recordResult.isCorrect;

    // Visual options feedback
    if (selectedChoice === 'A') {
      optionBtnA.classList.add(isCorrect ? 'is-correct' : 'is-wrong');
      if (!isCorrect) optionBtnB.classList.add('is-correct');
    } else {
      optionBtnB.classList.add(isCorrect ? 'is-correct' : 'is-wrong');
      if (!isCorrect) optionBtnA.classList.add('is-correct');
    }

    // Update Header Streak
    updateStreakUI();

    // Trigger Confetti on correct
    if (isCorrect) {
      fireConfetti();
    }

    // Show Result & Explanation
    showResultExplanation(currentQuiz, isCorrect, false);

    confirmAnswerBtn.disabled = true;
    confirmAnswerBtn.innerHTML = isCorrect 
      ? '<span>🎉 정답입니다! 멋져요!</span>' 
      : '<span>💡 오답이지만 하나 배웠어요!</span>';

    // Trigger AdSense refresh / render
    triggerAdSense();
  }

  /**
   * Show Result Banner & Explanation
   */
  function showResultExplanation(quiz, isCorrect, isRestored = false) {
    resultSection.classList.add('active');

    // Banner Styling
    resultBanner.className = `result-banner ${isCorrect ? 'is-correct' : 'is-wrong'}`;
    resultIcon.textContent = isCorrect ? '🎉' : '💡';
    
    if (isCorrect) {
      resultTitle.textContent = '정답입니다!';
      const stats = window.QuizEngine.getStats();
      resultSubtitle.textContent = isBonusMode 
        ? '보너스 문제를 멋지게 맞히셨습니다!' 
        : `연속 출석 🔥 ${stats.currentStreak}일차 달성! 내일도 만나요!`;
    } else {
      resultTitle.textContent = '아쉽지만 오답이에요!';
      const correctWord = (quiz.answer === 'A') ? quiz.optionA : quiz.optionB;
      resultSubtitle.textContent = `바른 표현은 바로 '${correctWord}'입니다.`;
    }

    // Fill Explanation & Tip
    explanationBody.textContent = quiz.explanation;
    tipText.textContent = quiz.tip || '국립국어원 표준 어문 규범에 따른 바른 표현입니다.';

    // Smooth scroll down to explanation
    if (!isRestored) {
      setTimeout(() => {
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }, 150);
    }
  }

  /**
   * Load a Random Bonus Quiz from the 1,825 Pool
   */
  function loadBonusQuiz() {
    isBonusMode = true;
    modeBanner.classList.add('active');

    const bonusQuiz = window.QuizEngine.getRandomBonusQuiz(currentQuiz ? currentQuiz.id : null);
    if (!bonusQuiz) return;

    currentQuiz = bonusQuiz;
    renderQuizView(bonusQuiz, true);

    // Scroll smoothly to top of main card
    document.getElementById('main-quiz-card').scrollIntoView({ behavior: 'smooth' });
    window.ShareHelper.showToast('🚀 보너스 연습 모드가 시작되었습니다!');
  }

  /**
   * Trigger AdSense adsbygoogle push
   */
  function triggerAdSense() {
    try {
      if (window.adsbygoogle && Array.isArray(window.adsbygoogle)) {
        window.adsbygoogle.push({});
      }
    } catch (e) {
      // AdSense script will handle gracefully
      console.log('AdSense slot prepared');
    }
  }

  /**
   * Open Stats Modal & populate numbers
   */
  function openStatsModal() {
    const stats = window.QuizEngine.getStats();

    statCurrentStreak.textContent = `${stats.currentStreak}일`;
    statMaxStreak.textContent = `${stats.maxStreak}일`;
    statTotalSolved.textContent = `${stats.totalSolved}개`;
    statAccuracy.textContent = `${stats.accuracy}%`;

    // Badges unlock states
    document.getElementById('badge-streak-3').classList.toggle('unlocked', stats.unlockedBadges.streak3);
    document.getElementById('badge-streak-7').classList.toggle('unlocked', stats.unlockedBadges.streak7);
    document.getElementById('badge-streak-30').classList.toggle('unlocked', stats.unlockedBadges.streak30);
    document.getElementById('badge-streak-100').classList.toggle('unlocked', stats.unlockedBadges.streak100);

    statsModal.classList.add('active');
    statsModal.setAttribute('aria-hidden', 'false');
  }

  function closeStatsModal() {
    statsModal.classList.remove('active');
    statsModal.setAttribute('aria-hidden', 'true');
  }

  /**
   * Setup Event Listeners
   */
  function setupEventListeners() {
    optionBtnA.addEventListener('click', () => selectOption('A'));
    optionBtnB.addEventListener('click', () => selectOption('B'));

    confirmAnswerBtn.addEventListener('click', submitAnswer);

    // Bonus Mode triggers
    bonusQuizBtn.addEventListener('click', loadBonusQuiz);
    returnTodayQuizBtn.addEventListener('click', loadTodayQuiz);

    // Share & Install
    shareQuizBtn.addEventListener('click', () => {
      if (currentQuiz) {
        const stats = window.QuizEngine.getStats();
        window.ShareHelper.shareQuiz(currentQuiz, stats.currentStreak);
      }
    });

    installPwaBtn.addEventListener('click', () => {
      window.ShareHelper.triggerPWAInstall();
    });

    // Stats Modal triggers
    streakTriggerBtn.addEventListener('click', openStatsModal);
    statsModalOpenBtn.addEventListener('click', openStatsModal);
    statsModalCloseBtn.addEventListener('click', closeStatsModal);
    modalConfirmBtn.addEventListener('click', closeStatsModal);

    statsModal.addEventListener('click', (e) => {
      if (e.target === statsModal) closeStatsModal();
    });

    // Keyboard navigation (1 / 2 or A / B / Enter)
    window.addEventListener('keydown', (e) => {
      if (statsModal.classList.contains('active')) {
        if (e.key === 'Escape') closeStatsModal();
        return;
      }

      if (e.key === '1' || e.key === 'a' || e.key === 'A') {
        selectOption('A');
      } else if (e.key === '2' || e.key === 'b' || e.key === 'B') {
        selectOption('B');
      } else if (e.key === 'Enter' && !confirmAnswerBtn.disabled) {
        submitAnswer();
      }
    });
  }

  /**
   * Lightweight High-Performance Confetti Animation (Zero dependencies)
   */
  function fireConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const colors = ['#6366F1', '#EC4899', '#F59E0B', '#10B981', '#3B82F6', '#F43F5E'];

    for (let i = 0; i < 75; i++) {
      particles.push({
        x: canvas.width / 2 + (Math.random() * 120 - 60),
        y: canvas.height * 0.45,
        w: Math.random() * 9 + 4,
        h: Math.random() * 8 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        vx: (Math.random() - 0.5) * 16,
        vy: (Math.random() * -14) - 6,
        rot: Math.random() * 360,
        rotSpeed: (Math.random() - 0.5) * 12,
        gravity: 0.42,
        opacity: 1
      });
    }

    let animationFrameId;
    let startTime = Date.now();

    function render() {
      const elapsed = Date.now() - startTime;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      let activeCount = 0;

      for (let p of particles) {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += p.gravity;
        p.rot += p.rotSpeed;
        p.opacity = Math.max(0, 1 - (elapsed / 2200));

        if (p.opacity > 0 && p.y < canvas.height + 50) {
          activeCount++;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rot * Math.PI) / 180);
          ctx.globalAlpha = p.opacity;
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
          ctx.restore();
        }
      }

      if (activeCount > 0 && elapsed < 2500) {
        animationFrameId = requestAnimationFrame(render);
      } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        cancelAnimationFrame(animationFrameId);
      }
    }

    render();
  }

  // Start app on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

})();
