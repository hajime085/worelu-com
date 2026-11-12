/* カイカタ 買い物メモ（list.js、2026-11-12追加）
   特集の掲載品カード（.pick）から商品名・メーカー・Amazonリンクを読み取り、
   localStorage に保存する汎用スクリプト。カードへのデータ属性の手書きは不要。
   保存キー：dp リンクがあれば ASIN、検索リンクのみのカードは href 全体。 */
(function () {
  'use strict';
  var KEY = 'kaikata-memo-v1';

  /* ---------- 保存データの読み書き（localStorage が使えない環境ではメモリ保持） ---------- */
  var items = [];
  var storageOk = true;
  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      if (raw) {
        var parsed = JSON.parse(raw);
        if (Object.prototype.toString.call(parsed) === '[object Array]') {
          items = [];
          for (var i = 0; i < parsed.length; i++) {
            var p = parsed[i];
            if (p && p.id && p.url) {
              items.push({ id: String(p.id), nm: String(p.nm || ''), maker: String(p.maker || ''), url: String(p.url) });
            }
          }
        }
      }
    } catch (e) { storageOk = false; }
  }
  function save() {
    if (!storageOk) return;
    try { window.localStorage.setItem(KEY, JSON.stringify(items)); }
    catch (e) { storageOk = false; }
  }
  function indexOfId(id) {
    for (var i = 0; i < items.length; i++) if (items[i].id === id) return i;
    return -1;
  }

  /* ---------- カードから商品情報を拾う ---------- */
  function textOf(el) {
    if (!el) return '';
    return (el.textContent || '').replace(/^\s+|\s+$/g, '');
  }
  function pickLink(card) {
    var links = card.getElementsByTagName('a');
    var fallback = null;
    for (var i = 0; i < links.length; i++) {
      var href = links[i].getAttribute('href') || '';
      if (href.indexOf('amazon') === -1) continue;
      if (href.indexOf('/dp/') !== -1) return links[i];
      if (!fallback) fallback = links[i];
    }
    return fallback;
  }
  function cardData(card) {
    var link = pickLink(card);
    if (!link) return null;
    var href = link.getAttribute('href') || '';
    var m = href.match(/\/dp\/([A-Z0-9]{10})/);
    return {
      id: m ? m[1] : href,
      nm: textOf(card.getElementsByClassName('nm')[0]),
      maker: textOf(card.getElementsByClassName('maker')[0]),
      url: href,
      link: link
    };
  }

  /* ---------- UI の組み立て ---------- */
  var fab, fabCount, back, panel, body, foot, tracked = [];

  function buildUI() {
    fab = document.createElement('button');
    fab.setAttribute('type', 'button');
    fab.className = 'ml-fab';
    fab.setAttribute('aria-label', '買い物メモを開く');
    fab.appendChild(document.createTextNode('メモ（'));
    fabCount = document.createElement('span');
    fabCount.className = 'ml-count';
    fabCount.appendChild(document.createTextNode('0'));
    fab.appendChild(fabCount);
    fab.appendChild(document.createTextNode('）'));
    document.body.appendChild(fab);

    back = document.createElement('div');
    back.className = 'ml-back';
    document.body.appendChild(back);

    panel = document.createElement('aside');
    panel.className = 'ml-panel';
    panel.setAttribute('aria-label', '買い物メモ');
    panel.setAttribute('aria-hidden', 'true');

    var hd = document.createElement('div');
    hd.className = 'ml-hd';
    var title = document.createElement('span');
    title.appendChild(document.createTextNode('買い物メモ'));
    var closeBtn = document.createElement('button');
    closeBtn.setAttribute('type', 'button');
    closeBtn.className = 'ml-close';
    closeBtn.setAttribute('aria-label', '閉じる');
    closeBtn.appendChild(document.createTextNode('×'));
    hd.appendChild(title);
    hd.appendChild(closeBtn);
    panel.appendChild(hd);

    body = document.createElement('div');
    body.className = 'ml-body';
    panel.appendChild(body);

    foot = document.createElement('div');
    foot.className = 'ml-foot';
    var clearBtn = document.createElement('button');
    clearBtn.setAttribute('type', 'button');
    clearBtn.className = 'ml-clear';
    clearBtn.appendChild(document.createTextNode('全部消す'));
    clearBtn.addEventListener('click', function () {
      items = [];
      save();
      sync();
    });
    foot.appendChild(clearBtn);
    panel.appendChild(foot);

    document.body.appendChild(panel);

    fab.addEventListener('click', openPanel);
    closeBtn.addEventListener('click', closePanel);
    back.addEventListener('click', closePanel);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' || e.keyCode === 27) closePanel();
    });
  }

  function openPanel() {
    renderList();
    panel.classList.add('open');
    back.classList.add('open');
    document.body.classList.add('ml-lock');
    panel.setAttribute('aria-hidden', 'false');
  }
  function closePanel() {
    if (!panel) return;
    panel.classList.remove('open');
    back.classList.remove('open');
    document.body.classList.remove('ml-lock');
    panel.setAttribute('aria-hidden', 'true');
  }

  function renderList() {
    while (body.firstChild) body.removeChild(body.firstChild);
    if (items.length === 0) {
      var empty = document.createElement('p');
      empty.className = 'ml-empty';
      empty.appendChild(document.createTextNode('まだ何も入っていません。特集の掲載品から、気になるものを集められます。'));
      body.appendChild(empty);
      foot.style.display = 'none';
      return;
    }
    foot.style.display = '';
    for (var i = 0; i < items.length; i++) {
      body.appendChild(renderItem(items[i]));
    }
  }
  function renderItem(item) {
    var box = document.createElement('div');
    box.className = 'ml-item';
    var nm = document.createElement('div');
    nm.className = 'nm';
    nm.appendChild(document.createTextNode(item.nm));
    box.appendChild(nm);
    if (item.maker) {
      var maker = document.createElement('div');
      maker.className = 'maker';
      maker.appendChild(document.createTextNode(item.maker));
      box.appendChild(maker);
    }
    var row = document.createElement('div');
    row.className = 'ml-row';
    var go = document.createElement('a');
    go.className = 'ml-go';
    go.setAttribute('href', item.url);
    go.setAttribute('target', '_blank');
    go.setAttribute('rel', 'nofollow sponsored noopener');
    go.appendChild(document.createTextNode('Amazonで見る'));
    var remove = document.createElement('button');
    remove.setAttribute('type', 'button');
    remove.className = 'ml-remove';
    remove.appendChild(document.createTextNode('外す'));
    (function (id) {
      remove.addEventListener('click', function () {
        var idx = indexOfId(id);
        if (idx !== -1) { items.splice(idx, 1); save(); }
        sync();
        renderList();
      });
    })(item.id);
    row.appendChild(go);
    row.appendChild(remove);
    box.appendChild(row);
    return box;
  }

  /* ---------- カード側ボタンの同期 ---------- */
  function sync() {
    fabCount.textContent = String(items.length);
    for (var i = 0; i < tracked.length; i++) {
      var t = tracked[i];
      var on = indexOfId(t.data.id) !== -1;
      t.btn.className = on ? 'ml-add on' : 'ml-add';
      t.btn.textContent = on ? '✓ メモに入ってる' : '＋ メモに入れる';
      t.btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    }
  }

  function attachButtons() {
    var cards = document.getElementsByClassName('pick');
    for (var i = 0; i < cards.length; i++) {
      var data = cardData(cards[i]);
      if (!data) continue;
      var btn = document.createElement('button');
      btn.setAttribute('type', 'button');
      btn.className = 'ml-add';
      (function (d, b) {
        b.addEventListener('click', function () {
          var idx = indexOfId(d.id);
          if (idx !== -1) items.splice(idx, 1);
          else items.push({ id: d.id, nm: d.nm, maker: d.maker, url: d.url });
          save();
          sync();
        });
      })(data, btn);
      var parent = data.link.parentNode;
      if (parent) {
        if (data.link.nextSibling) parent.insertBefore(btn, data.link.nextSibling);
        else parent.appendChild(btn);
      }
      tracked.push({ data: data, btn: btn });
    }
  }

  function init() {
    load();
    buildUI();
    attachButtons();
    sync();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
