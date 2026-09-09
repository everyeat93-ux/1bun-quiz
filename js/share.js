/**
 * 딱1분 오늘의 맞춤법 퀴즈 - Share & PWA Handler
 * 바이럴 공유 및 PWA 설치 프롬프트 처리
 */

(function(window) {
  'use strict';

  let deferredInstallPrompt = null;

  // Listen for beforeinstallprompt event
  window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent the mini-infobar from appearing on mobile
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredInstallPrompt = e;
    console.log('PWA install prompt ready');
  });

  window.addEventListener('appinstalled', () => {
    deferredInstallPrompt = null;
    showToast('🎉 앱이 홈 화면에 추가되었습니다!');
  });

  /**
   * Display floating toast notification
   */
  function showToast(message, duration = 2600) {
    const toast = document.getElementById('toast-msg');
    if (!toast) return;

    toast.textContent = message;
    toast.classList.add('show');

    setTimeout(() => {
      toast.classList.remove('show');
    }, duration);
  }

  /**
   * Share Quiz via Web Share API or Clipboard Copy
   */
  async function shareQuiz(quiz, streakCount) {
    const currentUrl = window.location.href.split('?')[0];
    const cleanQuestion = quiz.question.replace(/\[.*?\]/g, `[ ${quiz.optionA} vs ${quiz.optionB} ]`);
    
    const shareTitle = '딱1분 오늘의 맞춤법 퀴즈';
    const shareText = `[딱1분 맞춤법 퀴즈 🔥 ${streakCount}일차 달성!]\n\nQ. 너 이 문제 정답 알아?\n"${cleanQuestion}"\n\nA. ${quiz.optionA}\nB. ${quiz.optionB}\n\n👉 10초 만에 정답 확인하기:`;

    // Try native Web Share API (mobile Kakao, Safari, Chrome share sheet)
    if (navigator.share) {
      try {
        await navigator.share({
          title: shareTitle,
          text: shareText,
          url: currentUrl
        });
        showToast('공유가 완료되었습니다!');
        return;
      } catch (err) {
        if (err.name !== 'AbortError') {
          console.warn('Navigator share error:', err);
        } else {
          return; // User cancelled share
        }
      }
    }

    // Fallback: Clipboard copy
    const fullCopyText = `${shareText}\n${currentUrl}`;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      try {
        await navigator.clipboard.writeText(fullCopyText);
        showToast('📋 링크와 문제가 클립보드에 복사되었습니다! 카톡에 붙여넣어 보세요.');
      } catch (e) {
        legacyCopyFallback(fullCopyText);
      }
    } else {
      legacyCopyFallback(fullCopyText);
    }
  }

  function legacyCopyFallback(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand('copy');
      showToast('📋 문제가 클립보드에 복사되었습니다!');
    } catch (err) {
      showToast('링크 복사에 실패했습니다. 브라우저 설정을 확인해 주세요.');
    }
    document.body.removeChild(textarea);
  }

  /**
   * Prompt user to install PWA
   */
  async function triggerPWAInstall() {
    if (deferredInstallPrompt) {
      deferredInstallPrompt.prompt();
      const { outcome } = await deferredInstallPrompt.userChoice;
      if (outcome === 'accepted') {
        showToast('🎉 딱1분 퀴즈 설치가 시작됩니다!');
      }
      deferredInstallPrompt = null;
    } else {
      // If iOS Safari or standalone
      const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
      if (isIOS) {
        showToast('Safari 브라우저 하단의 [공유] 버튼 > [홈 화면에 추가]를 눌러주세요!');
      } else {
        showToast('브라우저 우측 상단 메뉴(⋮)에서 [홈 화면에 추가] 또는 [앱 설치]를 선택하세요!');
      }
    }
  }

  window.ShareHelper = {
    showToast,
    shareQuiz,
    triggerPWAInstall
  };

})(window);
