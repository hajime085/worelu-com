/* カイカタ 防災 備えチェックリスト（check.js、2026-11-12追加）
   防災グッズ特集（feature/bousai）専用スクリプト。
   カテゴリ別のチェック項目（.ck-item）をタップで記録し、「あなたの備え ○○％」と
   不足カテゴリを表示する。状態は localStorage に保存する。
   保存キー：kaikata-bousai-v1（買い物メモの kaikata-memo-v1 とは別） */
(function () {
  'use strict';
  var KEY = 'kaikata-bousai-v1';

  /* ---------- 保存データの読み書き（localStorage が使えない環境ではメモリ保持） ---------- */
  var checked = {};
  var storageOk = true;
  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      if (raw) {
        var parsed = JSON.parse(raw);
        if (parsed && typeof parsed === 'object') {
          for (var k in parsed) {
            if (Object.prototype.hasOwnProperty.call(parsed, k) && parsed[k]) checked[k] = true;
          }
        }
      }
    } catch (e) { storageOk = false; }
  }
  function save() {
    if (!storageOk) return;
    try { window.localStorage.setItem(KEY, JSON.stringify(checked)); }
    catch (e) { storageOk = false; }
  }

  function init() {
    var box = document.getElementById('ckBox');
    if (!box) return;
    var pctEl = document.getElementById('ckPct');
    var countEl = document.getElementById('ckCount');
    var fillEl = document.getElementById('ckFill');
    var missEl = document.getElementById('ckMiss');
    var resetBtn = document.getElementById('ckReset');
    if (!pctEl || !countEl || !fillEl || !missEl) return;

    var items = box.querySelectorAll('.ck-item');
    if (!items || items.length === 0) return;

    /* カテゴリ単位の集計用に、.ck-cat ごとに項目を束ねる */
    var cats = [];
    var catEls = box.querySelectorAll('.ck-cat');
    for (var c = 0; c < catEls.length; c++) {
      cats.push({
        name: catEls[c].getAttribute('data-ck-cat') || '',
        items: catEls[c].querySelectorAll('.ck-item'),
        countEl: catEls[c].querySelector('[data-ck-cat-count]')
      });
    }

    function isOn(btn) { return !!checked[btn.getAttribute('data-ck-id')]; }

    function paint(btn) {
      var on = isOn(btn);
      if (on) btn.classList.add('on'); else btn.classList.remove('on');
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      var mark = btn.querySelector('.ck-box');
      if (mark) mark.textContent = on ? '✓' : '';
    }

    function update() {
      var total = items.length, done = 0, i, j;
      for (i = 0; i < items.length; i++) if (isOn(items[i])) done++;
      var pct = total ? Math.round(done * 100 / total) : 0;
      pctEl.textContent = pct + '％';
      countEl.textContent = done + '／' + total + '項目';
      fillEl.style.width = pct + '%';

      var missing = [];
      for (j = 0; j < cats.length; j++) {
        var cd = 0;
        for (var k = 0; k < cats[j].items.length; k++) if (isOn(cats[j].items[k])) cd++;
        if (cats[j].countEl) cats[j].countEl.textContent = cd + '／' + cats[j].items.length;
        if (cd < cats[j].items.length && cats[j].name) missing.push(cats[j].name);
      }
      if (done === 0) {
        missEl.textContent = 'まだチェックが付いていません。すでに備えてあるものから、タップして付けていってください。';
      } else if (missing.length === 0) {
        missEl.textContent = '全カテゴリがそろいました。あとは「見直しのタイミング」（下の6）で、期限と電池を定期的に確かめてください。';
      } else {
        missEl.textContent = 'まだ不足しているカテゴリ：' + missing.join('・') + '。カテゴリ名を目印に、上の掲載品から足してください。';
      }
    }

    function onToggle(btn) {
      var id = btn.getAttribute('data-ck-id');
      if (!id) return;
      if (checked[id]) delete checked[id]; else checked[id] = true;
      save();
      paint(btn);
      update();
    }

    for (var i = 0; i < items.length; i++) {
      (function (b) {
        b.addEventListener('click', function () { onToggle(b); });
        paint(b);
      })(items[i]);
    }
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        checked = {};
        save();
        for (var i = 0; i < items.length; i++) paint(items[i]);
        update();
      });
    }
    update();
  }

  load();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
