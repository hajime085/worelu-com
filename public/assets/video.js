/* カイカタ 使ってみた動画ポップアップ（video.js、2026-11-12追加）
   特集ページ共通の動画モーダル。冬ページで実績のある .vpop 実装を共有化したもの。
   ボタン（.vpop-open）に data-vid（YouTube動画ID）/ data-vtitle（モーダル見出し）/
   data-vcredit（クレジット文）を持たせ、モーダル本体はこのスクリプトが生成する。
   iframe の src はモーダルを開いた時だけセットし、閉じたら外す（閉じれば再生も止まる）。 */
(function () {
  'use strict';
  var btns = document.querySelectorAll('.vpop-open[data-vid]');
  if (!btns.length) { return; }

  var back = document.getElementById('vpopBack');
  var modal = document.getElementById('vpopModal');
  var vtitle = null, closeBtn = null, frame = null, credit = null;

  if (!modal) {
    back = document.createElement('div');
    back.className = 'vpop-back';
    back.id = 'vpopBack';

    modal = document.createElement('div');
    modal.className = 'vpop';
    modal.id = 'vpopModal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-hidden', 'true');
    modal.setAttribute('aria-labelledby', 'vpopTitle');

    var box = document.createElement('div');
    box.className = 'vpop-box';

    var hd = document.createElement('div');
    hd.className = 'vpop-hd';
    vtitle = document.createElement('span');
    vtitle.id = 'vpopTitle';
    vtitle.textContent = '使ってみた動画';
    closeBtn = document.createElement('button');
    closeBtn.type = 'button';
    closeBtn.className = 'vpop-close';
    closeBtn.id = 'vpopClose';
    closeBtn.setAttribute('aria-label', '閉じる');
    closeBtn.textContent = '×';
    hd.appendChild(vtitle);
    hd.appendChild(closeBtn);

    var body = document.createElement('div');
    body.className = 'vpop-body';
    var frameWrap = document.createElement('div');
    frameWrap.className = 'vpop-frame';
    frame = document.createElement('iframe');
    frame.id = 'vpopFrame';
    frame.setAttribute('allow', 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture');
    frame.setAttribute('allowfullscreen', '');
    frame.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    frameWrap.appendChild(frame);
    credit = document.createElement('p');
    credit.className = 'vpop-credit';
    credit.id = 'vpopCredit';
    body.appendChild(frameWrap);
    body.appendChild(credit);

    box.appendChild(hd);
    box.appendChild(body);
    modal.appendChild(box);
    document.body.appendChild(back);
    document.body.appendChild(modal);
  } else {
    vtitle = document.getElementById('vpopTitle');
    closeBtn = document.getElementById('vpopClose');
    frame = document.getElementById('vpopFrame');
    credit = document.getElementById('vpopCredit');
    if (!back) { back = document.getElementById('vpopBack'); }
  }
  if (!modal || !back || !vtitle || !closeBtn || !frame || !credit) { return; }

  function openPop(btn) {
    var vid = btn.getAttribute('data-vid');
    if (!vid) { return; }
    var title = btn.getAttribute('data-vtitle') || '使ってみた動画';
    vtitle.textContent = title;
    credit.textContent = btn.getAttribute('data-vcredit') || '';
    frame.setAttribute('title', title + '（YouTube）');
    frame.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    frame.setAttribute('src', 'https://www.youtube-nocookie.com/embed/' + vid + '?rel=0&autoplay=1');
    modal.classList.add('open');
    back.classList.add('open');
    document.body.classList.add('vpop-lock');
    modal.setAttribute('aria-hidden', 'false');
  }
  function closePop() {
    modal.classList.remove('open');
    back.classList.remove('open');
    document.body.classList.remove('vpop-lock');
    modal.setAttribute('aria-hidden', 'true');
    frame.removeAttribute('src');
  }

  for (var i = 0; i < btns.length; i++) {
    (function (b) {
      b.addEventListener('click', function () { openPop(b); });
    })(btns[i]);
  }
  closeBtn.addEventListener('click', closePop);
  back.addEventListener('click', closePop);
  modal.addEventListener('click', function (e) { if (e.target === modal) { closePop(); } });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closePop(); } });
})();
