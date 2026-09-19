// 딱1분 상식 퀴즈 - Service Worker
const CACHE_NAME = 'ttak1bun-quiz-v9';
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

  // Network-First with cache fallback
  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200 && event.request.method === 'GET') {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      })
      .catch(() => caches.match(event.request))
  );
});
