/* カイカタ 季節の ambient 演出（fx.js、2026-11-12追加）
   ヒーロー（data-fx 属性つきコンテナ）の中だけに canvas を重ねる共有スクリプト。
     data-fx="snow"    ：白い雪の粒がゆっくり落ちて左右に揺れる（冬支度）
     data-fx="sparkle" ：金色・暖色の光がふわっと瞬く（クリスマス）
   演出はヒーロー帯の中だけ。本文には干渉しない（canvas は pointer-events:none、
   見た目の重ね方は style.css の .fx- が担う）。
   prefers-reduced-motion の場合は canvas 自体を作らない。
   ヒーローが画面外の間と、タブが非表示の間は描画を止める。解像度は等倍（1x）まで。 */
(function () {
  'use strict';

  var reduced = false;
  try {
    reduced = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  } catch (e) { reduced = false; }

  function rand(min, max) { return min + Math.random() * (max - min); }
  function clamp(v, min, max) { return v < min ? min : (v > max ? max : v); }

  /* ---------- 雪（冬支度） ---------- */
  function makeSnow(w, h) {
    var n = Math.round(clamp(w * h / 12000, 8, 40));
    var ps = [];
    for (var i = 0; i < n; i++) {
      ps.push({
        x: rand(0, w), y: rand(0, h),
        r: rand(0.9, 2.3),          /* 粒の半径 */
        vy: rand(14, 34),           /* 落下速度 px/秒 */
        ph: rand(0, Math.PI * 2),   /* 揺れの位相 */
        sw: rand(6, 16),            /* 揺れ幅 px */
        sp: rand(0.25, 0.6),        /* 揺れの速さ Hz */
        a: rand(0.35, 0.85)         /* 不透明度 */
      });
    }
    return ps;
  }
  function drawSnow(ctx, w, h, ps, t) {
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#ffffff';
    for (var i = 0; i < ps.length; i++) {
      var p = ps[i];
      var x = p.x + Math.sin(t * p.sp * Math.PI * 2 + p.ph) * p.sw;
      ctx.globalAlpha = p.a;
      ctx.beginPath();
      ctx.arc(x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  }
  function stepSnow(ps, w, h, dt) {
    for (var i = 0; i < ps.length; i++) {
      var p = ps[i];
      p.y += p.vy * dt;
      if (p.y - p.r > h) { p.y = -p.r; p.x = rand(0, w); }
    }
  }

  /* ---------- 瞬き（クリスマス） ---------- */
  var SPARK_COLORS = ['255,214,140', '255,190,102', '255,233,183', '255,172,92'];
  function makeSprite(rgb) {
    var c = document.createElement('canvas');
    c.width = 32; c.height = 32;
    var g = c.getContext('2d');
    if (!g) return null;
    var grad = g.createRadialGradient(16, 16, 0, 16, 16, 16);
    grad.addColorStop(0, 'rgba(' + rgb + ',1)');
    grad.addColorStop(0.35, 'rgba(' + rgb + ',0.55)');
    grad.addColorStop(1, 'rgba(' + rgb + ',0)');
    g.fillStyle = grad;
    g.fillRect(0, 0, 32, 32);
    return c;
  }
  function makeSparkles(w, h) {
    var n = Math.round(clamp(w * h / 22000, 10, 26));
    var ps = [];
    for (var i = 0; i < n; i++) {
      ps.push({
        x: rand(0.04, 0.96) * w, y: rand(0.06, 0.94) * h,
        s: rand(9, 20),             /* 光のにじみの大きさ px */
        per: rand(2400, 4800),      /* 瞬きの周期 ms */
        ph: rand(0, 1),             /* 位相（0〜1） */
        ci: Math.floor(rand(0, SPARK_COLORS.length))
      });
    }
    return ps;
  }
  function drawSparkles(ctx, w, h, ps, sprites, tms) {
    ctx.clearRect(0, 0, w, h);
    for (var i = 0; i < ps.length; i++) {
      var p = ps[i];
      var spr = sprites[p.ci];
      if (!spr) continue;
      /* sin の正の山だけを使う：ふわっと明るくなって、消える */
      var ph = (tms / p.per + p.ph) % 1;
      var a = Math.sin(ph * Math.PI);
      a = a * a;
      if (a <= 0.01) continue;
      ctx.globalAlpha = a * 0.9;
      ctx.drawImage(spr, p.x - p.s, p.y - p.s, p.s * 2, p.s * 2);
      /* 中心の芯 */
      ctx.globalAlpha = a;
      ctx.fillStyle = 'rgb(' + SPARK_COLORS[p.ci] + ')';
      ctx.beginPath();
      ctx.arc(p.x, p.y, 1.3, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  }

  /* ---------- 共通：コンテナへの組み立て ---------- */
  function setup(host) {
    var kind = host.getAttribute('data-fx');
    if (kind !== 'snow' && kind !== 'sparkle') return;

    var canvas = document.createElement('canvas');
    canvas.className = 'fx-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    host.appendChild(canvas);
    var ctx = canvas.getContext ? canvas.getContext('2d') : null;
    if (!ctx) { host.removeChild(canvas); return; }

    var sprites = null;
    if (kind === 'sparkle') {
      sprites = [];
      for (var i = 0; i < SPARK_COLORS.length; i++) sprites.push(makeSprite(SPARK_COLORS[i]));
    }

    var w = 0, h = 0, ps = [];
    function resize() {
      w = host.clientWidth || 0;
      h = host.clientHeight || 0;
      if (w <= 0 || h <= 0) return;
      canvas.width = w;   /* 等倍（1x）まで：Retina の 2x にはしない */
      canvas.height = h;
      ps = (kind === 'snow') ? makeSnow(w, h) : makeSparkles(w, h);
    }
    resize();

    var rafId = null, lastTs = 0, inView = false;

    function frame(ts) {
      rafId = null;
      if (!inView || document.hidden) return;
      if (!lastTs) lastTs = ts;
      var dt = Math.min((ts - lastTs) / 1000, 0.05);
      lastTs = ts;
      if (w > 0 && h > 0) {
        if (kind === 'snow') { stepSnow(ps, w, h, dt); drawSnow(ctx, w, h, ps, ts / 1000); }
        else drawSparkles(ctx, w, h, ps, sprites, ts);
      }
      rafId = window.requestAnimationFrame(frame);
    }
    function start() {
      if (rafId !== null || !inView || document.hidden) return;
      lastTs = 0;
      rafId = window.requestAnimationFrame(frame);
    }
    function stop() {
      if (rafId !== null) { window.cancelAnimationFrame(rafId); rafId = null; }
    }

    if ('IntersectionObserver' in window) {
      var io = new window.IntersectionObserver(function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].target !== host) continue;
          inView = !!entries[i].isIntersecting;
        }
        if (inView) start(); else stop();
      }, { threshold: 0 });
      io.observe(host);
    } else {
      inView = true; /* IO が無い環境では常時描画にフォールバック */
      start();
    }

    document.addEventListener('visibilitychange', function () {
      if (document.hidden) stop(); else start();
    });

    var rsTimer = null;
    window.addEventListener('resize', function () {
      if (rsTimer) window.clearTimeout(rsTimer);
      rsTimer = window.setTimeout(function () { resize(); }, 200);
    });
  }

  function init() {
    if (reduced) return; /* 動きを減らす設定なら何もしない */
    var hosts = document.querySelectorAll('[data-fx]');
    for (var i = 0; i < hosts.length; i++) setup(hosts[i]);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
