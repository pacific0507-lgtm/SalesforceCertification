// 問題文の書式の確認用ページを作る。使い方: node qfmt_preview.js <data/fe> <出力.html> [s に含まれる文字で絞る]
// 図の画像(〔図:…〕)は <data/fe>/img/ を、出力.html からの相対パスで読む
const fs=require('fs'),path=require('path');const csQF=require('./qfmt.js');
const [dir,out,flt]=process.argv.slice(2);
const base=path.relative(path.dirname(path.resolve(out)),path.resolve(dir,'img')).split(path.sep).join('/')+'/';
const Q=JSON.parse(fs.readFileSync(path.join(dir,'questions.json'),'utf8')).map(x=>x.data).filter(d=>!/^オリジナル/.test(d.s)&&(!flt||d.s.includes(flt)));
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const css=fs.readFileSync(path.join(__dirname,'patch_qfmt.py'),'utf8').match(/css = """([\s\S]*?)"""/)[1];
let h=`<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width"><style>:root{--line:#d9d6cc;--sub:#6b6b6b;--paper:#fff;--brand:#55691a;--ink:#1d1d1f;--accent-soft:#eef2dd}body{font-family:system-ui,sans-serif;margin:0;padding:12px;background:#f6f5f0;color:var(--ink)}.c{background:#fff;border-radius:14px;padding:14px;margin:0 0 14px}.qq{font-size:16px;line-height:1.95;white-space:pre-wrap}.s{font-size:12px;color:#888}.o{font-size:14px;white-space:pre-wrap;border:1px solid #ddd;border-radius:8px;padding:6px 10px;margin:4px 0}${css}</style>`;
Q.forEach((d,i)=>{h+=`<div class="c" id="i${i}"><div class="s">${esc(d.s)}</div><div class="qq">${csQF(esc(d.q),base)}</div>${d.o.map((o,k)=>`<div class="o">${'ABCDEFGHIJ'[k]}. ${esc(o)}</div>`).join('')}</div>`});
fs.writeFileSync(out,h);console.log(Q.length,'問');
