// 딱1분 맞춤법 퀴즈 - Service Worker
const CACHE_NAME = 'ttak1bun-quiz-v2';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './about.html',
  './privacy.html',
  './terms.html',
  './contact.html',
  './css/style.css',
  './js/app.js',
  './js/quizEngine.js',
  './js/share.js',
  './data/quizzes.json',
  './assets/icon.svg',
  './manifest.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  // Let Google AdSense and analytics pass through network directly
  if (event.request.url.includes('googlesyndication') || 
      event.request.url.includes('google-analytics') || 
      event.request.url.includes('doubleclick') ||
      event.request.url.includes('kakao')) {
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request).catch(() => {
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
      });
    })
  );
});
