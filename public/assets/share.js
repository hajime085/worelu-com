/* カイカタ: 記事シェア欄（X / LINE / リンクコピー、2026-11-12追加）
   各ページの og:title と og:url からシェアリンクを組み立てる。
   .share-slot の中身を JS で生成する。失敗しても他の JS には影響させない。 */
(function () {
  'use strict';

  function metaContent(prop) {
    var el = document.querySelector('meta[property="' + prop + '"]');
    return el ? (el.getAttribute('content') || '') : '';
  }

  function build(slot) {
    var title = metaContent('og:title') || document.title || '';
    var url = metaContent('og:url') || location.href;
    if (!url) return;

    var box = document.createElement('div');
    box.className = 'share-box';

    var hd = document.createElement('div');
    hd.className = 'share-hd';
    hd.textContent = 'この記事をシェア';
    box.appendChild(hd);

    var row = document.createElement('div');
    row.className = 'share-row';

    var ax = document.createElement('a');
    ax.className = 'share-btn share-x';
    ax.href = 'https://twitter.com/intent/tweet?text=' +
      encodeURIComponent(title) + '&url=' + encodeURIComponent(url);
    ax.target = '_blank';
    ax.rel = 'noopener';
    ax.textContent = 'Xでシェア';
    row.appendChild(ax);

    var al = document.createElement('a');
    al.className = 'share-btn share-line';
    al.href = 'https://social-plugins.line.me/lineit/share?url=' +
      encodeURIComponent(url);
    al.target = '_blank';
    al.rel = 'noopener';
    al.textContent = 'LINEで送る';
    row.appendChild(al);

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'share-btn share-copy';
    btn.textContent = 'リンクをコピー';
    btn.addEventListener('click', function () {
      var timer = null;
      function done() {
        btn.textContent = 'コピーしました';
        btn.classList.add('share-done');
        if (timer) clearTimeout(timer);
        timer = setTimeout(function () {
          btn.textContent = 'リンクをコピー';
          btn.classList.remove('share-done');
        }, 2000);
      }
      function fallback() {
        try {
          var ta = document.createElement('textarea');
          ta.value = url;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
          done();
        } catch (e) { /* コピーできない環境では静かに諦める */ }
      }
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(done, fallback);
        } else {
          fallback();
        }
      } catch (e) {
        fallback();
      }
    });
    row.appendChild(btn);

    box.appendChild(row);
    slot.appendChild(box);
  }

  function init() {
    try {
      var slots = document.querySelectorAll('.share-slot');
      for (var i = 0; i < slots.length; i++) {
        try { build(slots[i]); } catch (e) { /* スロット単位で無視 */ }
      }
    } catch (e) { /* シェア欄が出なくても本文には影響させない */ }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
