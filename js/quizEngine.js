/**
 * 딱1분 오늘의 맞춤법 퀴즈 - Quiz Engine
 * 1,825개 데이터셋 기반 날짜 연산 출제 및 LocalStorage 스트릭 시스템
 */

(function(window) {
  'use strict';

  const STORAGE_KEY = 'ttak1bun_quiz_state_v1';
  const REFERENCE_DATE = new Date('2025-01-01T00:00:00');

  class QuizEngine {
    constructor() {
      this.quizzes = [];
      this.isLoaded = false;
      this.state = this.loadState();
    }

    /**
     * Load quizzes from data/quizzes.json
     */
    async init() {
      try {
        const response = await fetch('./data/quizzes.json');
        if (!response.ok) {
          throw new Error(`Failed to load quizzes.json: status ${response.status}`);
        }
        this.quizzes = await response.json();
        this.isLoaded = true;
        return this.quizzes;
      } catch (error) {
        console.error('QuizEngine init error:', error);
        throw error;
      }
    }

    /**
     * Get LocalStorage state or default values
     */
    loadState() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) {
          return JSON.parse(raw);
        }
      } catch (e) {
        console.warn('LocalStorage unavailable or corrupted, using defaults', e);
      }

      return {
        lastPlayedDate: null,
        todaySolved: false,
        todayQuizId: null,
        todayChoice: null,
        todayIsCorrect: false,
        currentStreak: 0,
        maxStreak: 0,
        totalSolved: 0,
        totalCorrect: 0,
        history: []
      };
    }

    /**
     * Save current state to LocalStorage
     */
    saveState() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(this.state));
      } catch (e) {
        console.warn('Failed to save state to LocalStorage', e);
      }
    }

    /**
     * Format date to YYYY-MM-DD
     */
    formatDateKey(date = new Date()) {
      const y = date.getFullYear();
      const m = String(date.getMonth() + 1).padStart(2, '0');
      const d = String(date.getDate()).padStart(2, '0');
      return `${y}-${m}-${d}`;
    }

    /**
     * Calculate deterministically which of the 1,825 quizzes belongs to today
     */
    getTodayQuizIndex(date = new Date()) {
      const todayZero = new Date(date.getFullYear(), date.getMonth(), date.getDate());
      const diffMs = todayZero - REFERENCE_DATE;
      const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
      const totalQuizzes = this.quizzes.length || 1825;
      const index = ((diffDays % totalQuizzes) + totalQuizzes) % totalQuizzes;
      return index;
    }

    /**
     * Get Today's Quiz
     */
    getTodayQuiz(date = new Date()) {
      if (!this.quizzes || this.quizzes.length === 0) return null;
      const index = this.getTodayQuizIndex(date);
      return this.quizzes[index];
    }

    /**
     * Pick a random quiz from the 1,825 dataset for Bonus Mode
     */
    getRandomBonusQuiz(excludeId = null) {
      if (!this.quizzes || this.quizzes.length === 0) return null;
      let candidate;
      let tries = 0;
      do {
        const randomIndex = Math.floor(Math.random() * this.quizzes.length);
        candidate = this.quizzes[randomIndex];
        tries++;
      } while (candidate && candidate.id === excludeId && tries < 10);
      return candidate;
    }

    /**
     * Check if user already solved today's quiz
     */
    hasSolvedToday(todayKey = this.formatDateKey()) {
      return this.state.lastPlayedDate === todayKey && this.state.todaySolved;
    }

    /**
     * Record a quiz attempt and update streak logic
     */
    recordAnswer(quiz, userChoice, isBonus = false) {
      const isCorrect = (quiz.answer.toUpperCase() === userChoice.toUpperCase());
      const todayKey = this.formatDateKey();

      if (!isBonus) {
        // Daily Quiz: Calculate Streak
        if (this.state.lastPlayedDate) {
          const lastDate = new Date(this.state.lastPlayedDate);
          const currentDate = new Date(todayKey);
          const diffDays = Math.round((currentDate - lastDate) / (1000 * 60 * 60 * 24));

          if (diffDays === 1) {
            // Consecutive day: increment streak
            this.state.currentStreak = (this.state.currentStreak || 0) + 1;
          } else if (diffDays > 1) {
            // Streak broken: reset to 1
            this.state.currentStreak = 1;
          }
          // If diffDays === 0, already played today, streak remains
        } else {
          // First time player
          this.state.currentStreak = 1;
        }

        this.state.lastPlayedDate = todayKey;
        this.state.todaySolved = true;
        this.state.todayQuizId = quiz.id;
        this.state.todayChoice = userChoice;
        this.state.todayIsCorrect = isCorrect;
        this.state.maxStreak = Math.max(this.state.maxStreak || 0, this.state.currentStreak);
      }

      // Update aggregate stats
      this.state.totalSolved = (this.state.totalSolved || 0) + 1;
      if (isCorrect) {
        this.state.totalCorrect = (this.state.totalCorrect || 0) + 1;
      }

      // Add to history (keep latest 30)
      this.state.history.unshift({
        date: todayKey,
        quizId: quiz.id,
        isBonus: isBonus,
        isCorrect: isCorrect,
        userChoice: userChoice,
        correctAnswer: quiz.answer
      });
      if (this.state.history.length > 30) {
        this.state.history.pop();
      }

      this.saveState();

      return {
        isCorrect,
        currentStreak: this.state.currentStreak,
        maxStreak: this.state.maxStreak,
        totalSolved: this.state.totalSolved,
        totalCorrect: this.state.totalCorrect
      };
    }

    /**
     * Get computed statistics
     */
    getStats() {
      const total = this.state.totalSolved || 0;
      const correct = this.state.totalCorrect || 0;
      const accuracy = total > 0 ? Math.round((correct / total) * 100) : 0;

      return {
        currentStreak: this.state.currentStreak || 0,
        maxStreak: this.state.maxStreak || 0,
        totalSolved: total,
        totalCorrect: correct,
        accuracy: accuracy,
        unlockedBadges: {
          streak3: (this.state.maxStreak >= 3),
          streak7: (this.state.maxStreak >= 7),
          streak30: (this.state.maxStreak >= 30),
          streak100: (this.state.maxStreak >= 100)
        }
      };
    }
  }

  // Expose globally
  window.QuizEngine = new QuizEngine();

})(window);
