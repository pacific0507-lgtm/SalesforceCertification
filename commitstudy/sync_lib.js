/* CommitStudy: 端末・タブをまたいだ記録の合わせ方(window.CSQ)。patch_sync_merge.py がページの先頭に埋め込む。
   - 時刻: now() は「この端末の時計」と「これまでに見た一番新しい時刻+1」の大きい方(時計のずれた端末があっても、あとからの操作が勝つ)
   - 項目ごとの更新時刻(stamp / mapMerge): 消した項目も時刻を残し(消した印)、ほかの端末の古い控えで復活しない
   - 回答数・学習量: 端末ごとの数を持ち、合計を表示用の値にする(2台で解いても大きい方にならない)
   - 端末の保存容量がいっぱいのときは、テキストと問題の控え(chcache / qcache)を消してから保存し直し、それでもだめなら知らせる */
(function () {
  if (window.CSQ) return;
  var LS = null;
  try { LS = window.localStorage; } catch (e) {}
  function g(k) { try { return LS ? LS.getItem(k) : null; } catch (e) { return null; } }
  function sset(k, v) { try { LS && LS.setItem(k, v); } catch (e) {} }
  function clone(o) { return o == null ? o : JSON.parse(JSON.stringify(o)); }
  function js(o) { return JSON.stringify(o === undefined ? null : o); }
  function isObj(o) { return !!o && typeof o === "object" && !Array.isArray(o); }

  /* ---- 時刻 ---- */
  var CK = "cs-clock", last = +g(CK) || 0, FAR = 3e11; /* FAR: 10年以上先の時刻は壊れた値として無視 */
  function seen(t) {
    t = +t || 0;
    if (t > last && t < Date.now() + FAR) { last = t; sset(CK, String(t)); }
  }
  function now() {
    var t = Math.max(Date.now(), last + 1, (+g(CK) || 0) + 1);
    last = t; sset(CK, String(t));
    return t;
  }
  function seenMap(m) { if (isObj(m)) Object.keys(m).forEach(function (k) { seen(m[k]); }); }

  /* ---- 端末ID(このブラウザ) ---- */
  var DK = "cs-dev-id", DEV = g(DK);
  if (!DEV) { DEV = "d" + Date.now().toString(36) + Math.random().toString(36).slice(2, 8); sset(DK, DEV); }
  function dev() { return DEV; }

  /* ---- 項目ごとの更新時刻 ---- */
  /* cur と sh(前回の控え)を比べ、変わった・消えた項目の時刻を tm に入れる。変わったら true */
  function stamp(cur, sh, tm, t) {
    cur = cur || {}; sh = sh || {};
    var ch = false, keys = {};
    Object.keys(cur).forEach(function (k) { keys[k] = 1; });
    Object.keys(sh).forEach(function (k) { keys[k] = 1; });
    Object.keys(keys).forEach(function (k) {
      if (js(cur[k]) !== js(sh[k])) { tm[k] = t || (t = now()); ch = true; }
    });
    return ch;
  }
  /* a(時刻 at) と b(時刻 bt) を項目ごとに合わせる。時刻が新しい方を採用(消した印も含む)。
     時刻がない古い記録どうしは、ある方を残す(a を優先) */
  function mapMerge(a, at, b, bt) {
    a = a || {}; b = b || {}; at = at || {}; bt = bt || {};
    var v = {}, t = {}, keys = {};
    [a, b, at, bt].forEach(function (m) { Object.keys(m).forEach(function (k) { keys[k] = 1; }); });
    Object.keys(keys).forEach(function (k) {
      var ta = +at[k] || 0, tb = +bt[k] || 0, src;
      if (ta > tb) src = a; else if (tb > ta) src = b;
      else src = (k in a) ? a : b;
      if (k in src) v[k] = clone(src[k]);
      if (ta || tb) t[k] = Math.max(ta, tb);
    });
    seenMap(t);
    return { v: v, t: t };
  }

  /* ---- 問題集の回答履歴(hist): 端末ごとの数(hd)の合計 ----
     hd = {端末ID: {e: リセット時刻, q: {問題番号: {n, c, l, t}}}}、hr = 最後にリセットした時刻。
     hd がない古い記録は、そのときの hist を "_0"(移行分)として持つ */
  function cleanB(b, hr) {
    if (!b || (+b.e || 0) >= hr) return b;
    var q = {};
    Object.keys(b.q || {}).forEach(function (k) {
      var x = b.q[k];
      if (x && (+x.t || 0) >= hr) q[k] = { n: 1, c: x.l === "o" ? 1 : 0, l: x.l, t: x.t };
    });
    return { e: hr, q: q };
  }
  function derive(hd, hr) {
    var h = {};
    Object.keys(hd || {}).forEach(function (d) {
      var b = cleanB(hd[d], +hr || 0);
      Object.keys((b && b.q) || {}).forEach(function (k) {
        var x = b.q[k], o = h[k] || (h[k] = { n: 0, c: 0 });
        if (!x) return;
        o.n += +x.n || 0; o.c += +x.c || 0;
        if ((+x.t || 0) >= (+o.t || 0) && x.l) { o.l = x.l; o.t = +x.t || 0; }
      });
    });
    Object.keys(h).forEach(function (k) { if (!h[k].n) delete h[k]; });
    return h;
  }
  /* st.hist が hd の合計より多い分(古い版や、この端末で数えた分)を、端末 d の数へ足して hist を合計に揃える */
  function reconcile(st, d) {
    if (!st || typeof st !== "object") return st;
    if (!isObj(st.hist)) st.hist = {};
    st.hr = +st.hr || 0;
    if (!isObj(st.hd)) st.hd = { _0: { e: st.hr, q: clone(st.hist) } };
    Object.keys(st.hd).forEach(function (k) { st.hd[k] = cleanB(st.hd[k], st.hr); });
    var D = derive(st.hd, st.hr);
    Object.keys(st.hist).forEach(function (k) {
      var h = st.hist[k] || {}, x = D[k] || { n: 0, c: 0 }, dn = (+h.n || 0) - x.n;
      if (dn > 0) {
        var b = st.hd[d] || (st.hd[d] = { e: st.hr, q: {} }), en = b.q[k] || (b.q[k] = { n: 0, c: 0 });
        en.n = (+en.n || 0) + dn;
        en.c = (+en.c || 0) + Math.max(0, Math.min(dn, (+h.c || 0) - x.c));
        if ((+h.t || 0) >= (+en.t || 0)) { en.l = h.l; en.t = +h.t || 0; }
      }
    });
    st.hist = derive(st.hd, st.hr);
    return st;
  }
  function hdMerge(A, B, hr) {
    var o = {};
    A = A || {}; B = B || {};
    Object.keys(A).concat(Object.keys(B)).forEach(function (d) {
      if (o[d]) return;
      var a = cleanB(A[d], hr), b = cleanB(B[d], hr);
      if (!a || !b) { o[d] = clone(a || b); return; }
      if ((+a.e || 0) !== (+b.e || 0)) { o[d] = clone((+a.e || 0) > (+b.e || 0) ? a : b); return; }
      var q = {};
      Object.keys(a.q || {}).concat(Object.keys(b.q || {})).forEach(function (k) {
        var x = (a.q || {})[k], y = (b.q || {})[k];
        q[k] = clone(!x ? y : !y ? x : ((+x.n || 0) > (+y.n || 0) || ((+x.n || 0) === (+y.n || 0) && (+x.t || 0) >= (+y.t || 0))) ? x : y);
      });
      o[d] = { e: +a.e || 0, q: q };
    });
    return o;
  }
  function union(a, b, cap) {
    var seen1 = {}, o = [];
    (a || []).concat(b || []).forEach(function (x) { var k = js(x); if (!seen1[k]) { seen1[k] = 1; o.push(x); } });
    return cap && o.length > cap ? o.slice(-cap) : o;
  }
  /* 問題集の記録(S)を合わせる。base は画面の状態(位置・絞り込み・モードなど)をそのまま使う方。
     中身(回答・履歴・しおり・取り込み済みの印・解答ログ・リセット)は両方を合わせる */
  function qMerge(base, a, b) {
    var d = dev();
    a = reconcile(clone(a), d); b = reconcile(clone(b), "_x");
    var o = clone(base);
    o.hr = Math.max(+a.hr || 0, +b.hr || 0);
    o.hd = hdMerge(a.hd, b.hd, o.hr);
    o.hist = derive(o.hd, o.hr);
    o.answers = {}; o.at = {};
    ["study", "exam"].forEach(function (m) {
      var r = mapMerge((a.answers || {})[m], (a.at || {})[m], (b.answers || {})[m], (b.at || {})[m]);
      o.answers[m] = r.v; o.at[m] = r.t;
    });
    Object.keys(a.answers || {}).concat(Object.keys(b.answers || {})).forEach(function (m) {
      if (!o.answers[m]) o.answers[m] = clone((a.answers || {})[m] || (b.answers || {})[m]);
    });
    var bmA = {}, bmB = {};
    (a.bm || []).forEach(function (n) { bmA[n] = 1; });
    (b.bm || []).forEach(function (n) { bmB[n] = 1; });
    var r = mapMerge(bmA, a.bt, bmB, b.bt), order = (a.bm || []).concat(b.bm || []), bm = [];
    order.forEach(function (n) { if (r.v[n] && bm.indexOf(n) < 0) bm.push(n); });
    o.bm = bm; o.bt = r.t;
    o.pa = union(a.pa, b.pa, 1500);
    var lg = {}, L = [];
    (a.log || []).concat(b.log || []).forEach(function (e) { if (!e) return; var k = e.i + "|" + e.m + "|" + e.t; if (!lg[k]) { lg[k] = 1; L.push(e); } });
    L.sort(function (x, y) { return (x.t || 0) - (y.t || 0); });
    if (L.length > 2000) L = L.slice(-2000);
    if (L.length || a.log || b.log) o.log = L;
    o.ts = Math.max(+a.ts || 0, +b.ts || 0, +base.ts || 0);
    seen(a.ts); seen(b.ts); seen(o.hr);
    return o;
  }
  /* 中身だけを比べる(画面の状態の違いは無視) */
  function qBody(s) { s = s || {}; return js([s.hist, s.answers, s.bm, s.hr, s.at, s.bt, s.pa, (s.log || []).length]); }

  /* ---- 学習の記録(act): 日ごとに端末ごとの数(v)を持ち、q・c・t はその合計 ---- */
  function dayNorm(x) {
    x = isObj(x) ? x : {};
    if (!isObj(x.v)) x.v = { _0: { q: +x.q || 0, c: +x.c || 0, t: +x.t || 0 } };
    if (!Array.isArray(x.r)) x.r = [];
    var s = { q: 0, c: 0, t: 0 };
    Object.keys(x.v).forEach(function (d) { var y = x.v[d] || {}; s.q += +y.q || 0; s.c += +y.c || 0; s.t += +y.t || 0; });
    x.q = s.q; x.c = s.c; x.t = s.t;
    return x;
  }
  function actMerge(A, B) {
    A = isObj(A) ? A : {}; B = isObj(B) ? B : {};
    var o = { ts: Math.max(+A.ts || 0, +B.ts || 0), d: {} };
    [A.d || {}, B.d || {}].forEach(function (src) {
      Object.keys(src).forEach(function (k) {
        var x = dayNorm(clone(src[k])), y = o.d[k];
        if (!y) { o.d[k] = x; return; }
        Object.keys(x.v).forEach(function (d) {
          var p = y.v[d] || (y.v[d] = { q: 0, c: 0, t: 0 }), q = x.v[d];
          ["q", "c", "t"].forEach(function (f) { p[f] = Math.max(+p[f] || 0, +q[f] || 0); });
        });
        x.r.forEach(function (s) { if (y.r.indexOf(s) < 0 && y.r.length < 80) y.r.push(s); });
        dayNorm(y);
      });
    });
    seen(o.ts);
    return o;
  }
  /* 今日の分に、この端末の数を足す(f: q / c / t、n: 足す数) */
  function actBump(act, day, f, n) {
    if (!isObj(act)) act = { ts: 0, d: {} };
    if (!isObj(act.d)) act.d = {};
    var x = dayNorm(act.d[day] || (act.d[day] = { q: 0, c: 0, r: [], v: {} })), v = x.v[dev()] || (x.v[dev()] = { q: 0, c: 0, t: 0 });
    v[f] = (+v[f] || 0) + (n == null ? 1 : n);
    dayNorm(x);
    act.ts = now();
    return act;
  }
  function actDays(act) { return js(((act && act.d) || {})); }

  /* ---- 端末の記録の同期(fam-ls) ----
     項目ごとに合わせる鍵(用語カード・復習の予定・合格した科目)。ほかは鍵ごとに新しい方 */
  var MAPK = ["cs-term-known-v1", "cs-term-bm-v1", "cs-review-v1", "cs-subj-passed", "cs-badge-told"], IT = "ls-mirror-it";
  function pj(v, d) { try { var x = JSON.parse(v); return x == null ? d : x; } catch (e) { return d; } }
  function itAll() { var x = pj(g(IT), {}); return isObj(x) ? x : {}; }
  /* setItem のたびに(古い値と新しい値を比べて)項目ごとの時刻を残す */
  function famStamp(k, ov, nv, write) {
    if (MAPK.indexOf(k) < 0) return;
    var a = pj(nv, {}), b = pj(ov, {});
    if (!isObj(a) || !isObj(b)) return;
    var all = itAll(), tm = isObj(all[k]) ? all[k] : {};
    if (stamp(a, b, tm)) { all[k] = tm; write(IT, js(all)); }
  }
  /* アカウントの keys(ck)と端末の記録を合わせる。io: {get, set(端末へ書く。同期の通知はしない), ts(鍵ごとの時刻 obj), setTs(obj)} */
  function famMerge(W, ck, io) {
    ck = isObj(ck) ? ck : {};
    var out = Object.assign({}, ck), mts = io.ts(), all = itAll(), itCh = false, tsCh = false;
    W.forEach(function (e) {
      var nm = e.replace(/-/g, "_"), c = isObj(ck[nm]) ? ck[nm] : null, lv = io.get(e), lts = +mts[e] || 0;
      if (c) { seen(c.ts); seenMap(c.it); }
      if (MAPK.indexOf(e) >= 0) {
        var lo = pj(lv, null), co = c && typeof c.v === "string" ? pj(c.v, null) : null;
        if (!isObj(lo) && !isObj(co)) return;
        var r = mapMerge(isObj(lo) ? lo : {}, all[e], isObj(co) ? co : {}, c && c.it), nv = js(r.v);
        if (nv !== lv) io.set(e, nv);
        if (js(r.t) !== js(all[e] || {})) { all[e] = r.t; itCh = true; }
        var t1 = Math.max(lts, c ? +c.ts || 0 : 0) || now();
        if (t1 !== lts) { mts[e] = t1; tsCh = true; }
        out[nm] = { v: nv, ts: t1, it: r.t };
      } else if (e === "ls-badges-v1") {
        var r1 = pj(lv, {}), i1 = c ? pj(c.v, {}) : {};
        r1 = isObj(r1) ? r1 : {}; i1 = isObj(i1) ? i1 : {};
        if (lv == null && !c) return;
        var m = Object.assign({}, i1, r1);
        Object.keys(i1).forEach(function (k) { if (+i1[k] && +r1[k] && +i1[k] < +r1[k]) m[k] = i1[k]; });
        var mv = js(m);
        if (mv !== js(r1)) io.set(e, mv);
        out[nm] = { v: mv, ts: Math.max(lts, c ? +c.ts || 0 : 0) || now() };
      } else if (e === "ls-stamps-seen" || e === "ls-letters-v1") {
        var la = pj(lv, null), ca = c ? pj(c.v, null) : null;
        if (!Array.isArray(la) && !Array.isArray(ca)) {
          if (lv != null) out[nm] = { v: lv, ts: lts || now() };
          else if (c) io.set(e, c.v);
          return;
        }
        var u;
        if (e === "ls-stamps-seen") u = union(Array.isArray(ca) ? ca : [], Array.isArray(la) ? la : [], 120);
        else {
          var ks = {}; u = [];
          (Array.isArray(la) ? la : []).concat(Array.isArray(ca) ? ca : []).forEach(function (x) { var k = x && x.key; if (k && !ks[k]) { ks[k] = 1; u.push(x); } });
          u = u.slice(0, 12);
        }
        var uv = js(u);
        if (uv !== lv) io.set(e, uv);
        out[nm] = { v: uv, ts: Math.max(lts, c ? +c.ts || 0 : 0) || now() };
      } else {
        if (c && typeof c.v === "string" && (lv == null || (+c.ts || 0) > lts)) {
          if (lv !== c.v) io.set(e, c.v);
          if (lts !== (+c.ts || 0)) { mts[e] = +c.ts || 0; tsCh = true; }
        } else if (lv != null) {
          if (!lts) { lts = now(); mts[e] = lts; tsCh = true; }
          out[nm] = { v: lv, ts: lts };
        }
      }
    });
    if (itCh) io.set(IT, js(all));
    if (tsCh) io.setTs(mts);
    return { keys: out, changed: js(out) !== js(ck) };
  }

  /* ---- 保存容量がいっぱいのとき ---- */
  var CACHE = /^sr-[a-z0-9]+-(chcache|qcache)-v1$/, warned = false;
  function isQuota(e) {
    return !!e && (e.name === "QuotaExceededError" || e.name === "NS_ERROR_DOM_QUOTA_REACHED" || e.code === 22 || e.code === 1014);
  }
  function evict(keep) {
    var ks = [], n = 0;
    try { for (var i = 0; i < LS.length; i++) { var k = LS.key(i); if (CACHE.test(k) && k !== keep) ks.push(k); } } catch (e) {}
    ks.forEach(function (k) { try { LS.removeItem(k); n++; } catch (e) {} });
    return n;
  }
  function warn() {
    if (warned) return;
    warned = true;
    var show = function () {
      try {
        var d = document.createElement("div");
        d.id = "cs-quota";
        d.setAttribute("role", "alert");
        d.style.cssText = "position:fixed;z-index:9999;left:12px;right:12px;bottom:calc(14px + env(safe-area-inset-bottom,0px));max-width:560px;margin:0 auto;background:#8a1c1c;color:#fff;border-radius:12px;padding:12px 44px 12px 14px;font:14px/1.6 sans-serif;box-shadow:0 10px 26px -10px rgba(0,0,0,.45)";
        d.textContent = "この端末の保存容量がいっぱいのため、記録を端末に保存できませんでした。アカウントにつながっていれば、アカウントには保存されます。ほかのサイトのデータを消すか、ブラウザの設定で空きを作ってください。";
        var x = document.createElement("button");
        x.type = "button"; x.textContent = "×"; x.setAttribute("aria-label", "閉じる");
        x.style.cssText = "position:absolute;top:6px;right:6px;width:32px;height:32px;border:0;border-radius:50%;background:rgba(255,255,255,.18);color:inherit;font-size:18px;cursor:pointer";
        x.onclick = function () { d.remove(); };
        d.appendChild(x);
        document.body.appendChild(d);
      } catch (e) {}
    };
    if (document.body) show(); else document.addEventListener("DOMContentLoaded", show);
  }
  try {
    var sp = Storage.prototype.setItem;
    Storage.prototype.setItem = function (k, v) {
      try { return sp.apply(this, arguments); }
      catch (e) {
        if (this !== LS || !isQuota(e) || CACHE.test(String(k))) throw e;
        evict();
        try { return sp.apply(this, arguments); }
        catch (e2) { warn(); throw e2; }
      }
    };
  } catch (e) {}

  window.CSQ = {
    now: now, seen: seen, dev: dev, clone: clone, stamp: stamp, mapMerge: mapMerge,
    reconcile: reconcile, derive: derive, qMerge: qMerge, qBody: qBody,
    dayNorm: dayNorm, actMerge: actMerge, actBump: actBump, actDays: actDays,
    famStamp: famStamp, famMerge: famMerge, MAPK: MAPK, evict: evict
  };
})();
