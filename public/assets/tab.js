/* カイカタ 章タブ（tab.js、2026-11-12追加）
   スマホ専用：記事ページの目次（.toc）から、画面右端に固定する
   縦書きタブ列（クリアファイルのインデックス風）を生成する共有スクリプト。
   タブの短縮ラベルは各 TOC リンクの data-tab 属性で持つ（目次側で保守する）。
   表示・非表示は style.css の .tb- クラス（max-width:640px のみ表示）が担う。 */
(function () {
  'use strict';
  var SHOW_AFTER = 600; /* この px 数を超えたらフェードイン */

  function init() {
    var toc = document.querySelector('.toc');
    if (!toc) return;
    var links = toc.querySelectorAll('a[href^="#"]');
    if (!links || links.length === 0) return;

    var nav = document.createElement('nav');
    nav.className = 'tb-nav';
    nav.setAttribute('aria-label', '章へのショートカット');

    var tabs = [];
    var sections = [];
    var i, link, id, sec, tab;
    for (i = 0; i < links.length; i++) {
      link = links[i];
      id = (link.getAttribute('href') || '').slice(1);
      if (!id) continue;
      sec = document.getElementById(id);
      if (!sec) continue;
      tab = document.createElement('a');
      tab.className = 'tb-tab';
      tab.setAttribute('href', '#' + id);
      tab.textContent = link.getAttribute('data-tab') || (link.textContent || '').replace(/^\s+|\s+$/g, '');
      (function (target, targetId) {
        tab.addEventListener('click', function (e) {
          e.preventDefault();
          var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
          target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
          try { window.history.replaceState(null, '', '#' + targetId); } catch (err) {}
        });
      })(sec, id);
      nav.appendChild(tab);
      tabs.push(tab);
      sections.push(sec);
    }
    if (tabs.length === 0) return;
    document.body.appendChild(nav);

    /* ある程度スクロールしたらフェードイン（最上部では通常の目次と重複するため） */
    function onScroll() {
      var y = window.scrollY || window.pageYOffset || 0;
      if (y > SHOW_AFTER) nav.classList.add('tb-on');
      else nav.classList.remove('tb-on');
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    /* 今読んでいる章のタブをハイライト（画面中央付近の帯に入った章を採用） */
    if ('IntersectionObserver' in window) {
      var visible = {};
      var current = -1;
      function applyCurrent() {
        var pick = -1;
        for (var k = 0; k < sections.length; k++) {
          if (visible[k]) { pick = k; break; }
        }
        if (pick === -1 || pick === current) return;
        current = pick;
        for (var j = 0; j < tabs.length; j++) {
          if (j === current) tabs[j].classList.add('tb-cur');
          else tabs[j].classList.remove('tb-cur');
        }
      }
      var io = new window.IntersectionObserver(function (entries) {
        for (var n = 0; n < entries.length; n++) {
          var idx = sections.indexOf(entries[n].target);
          if (idx === -1) continue;
          if (entries[n].isIntersecting) visible[idx] = true;
          else delete visible[idx];
        }
        applyCurrent();
      }, { rootMargin: '-35% 0px -58% 0px', threshold: 0 });
      for (var s = 0; s < sections.length; s++) io.observe(sections[s]);
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
