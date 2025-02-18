const CACHE_NAME = 'pwa-cache-v1'
const OFFLINE_PATH = '/offline.html';

const urlsToCache = [
    '/static/css/styles.css', // CSS file
    '/static/js/script.js',   // JS file
    '/',                      // Home page
    OFFLINE_PATH,             // Offline page
    ]

const self = this;

// Install SW
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    )
    self.skipWaiting();
});

// Activate the SW
self.addEventListener('activate', (event) => {
    const cacheWhitelist = [];
    cacheWhitelist.push(CACHE_NAME)

    event.waitUntil(
        caches.keys().then((cacheNames) => Promise.all(
            cacheNames.map((cacheName) => {
                if(!cacheWhitelist.includes(cacheName)) {
                    return caches.delete(cacheName)
                }
            })
        ))
    )
});

// Listen for requests
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request)
                    .catch(() => caches.match(OFFLINE_PATH))
            })
    )
});

// self.addEventListener('fetch', (event) => {
//     event.respondWith(
//         caches.match(event.request).then((response) => {
//             if (response) {
//                 return response; // Return the cached response if found
//             }
//             return fetch(event.request).catch(() => {
//                 // If the fetch fails, return the fallback page
//                 return caches.match(OFFLINE_PATH);
//             });
//         })
//     );
// });
