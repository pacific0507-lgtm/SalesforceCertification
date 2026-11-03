const {chromium}=require('playwright');
const STUB=`(()=>{const mk=(p)=>({get:async()=>({exists:false,data:()=>null}),set:async()=>{},update:async()=>{},delete:async()=>{},onSnapshot:()=>()=>{}});
const q=()=>{const o={orderBy:()=>o,where:()=>o,limit:()=>o,get:async()=>({docs:[],empty:true,size:0}),onSnapshot:()=>()=>{}};return o};
const db={doc:mk,collection:()=>Object.assign(q(),{doc:mk})};
window.claude={use:async(n)=>n==='db'?db:n==='user'?{id:async()=>'u1',name:async()=>'デモ'}:null};
try{if(!localStorage.getItem('demo-seeded')){const D=(k)=>{const d=new Date();d.setDate(d.getDate()-k);return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')};
 const act={ts:Date.now(),d:{}};[0,1,2,3,5,6,8,9,10,12,13].forEach((k,i)=>{act.d[D(k)]={q:[12,8,15,6,10,4,9,14,7,11,5][i],c:[9,6,12,4,8,3,7,11,5,8,4][i],r:['stream','category'],t:[1500,900,1800,600,1200,500,1000,1700,800,1300,600][i]}});
 localStorage.setItem('sr-d360-act-v1',JSON.stringify(act));
 localStorage.setItem('sr-afsales-act-v1',JSON.stringify({ts:Date.now(),d:{[D(0)]:{q:6,c:5,r:['lifecycle'],t:700},[D(1)]:{q:4,c:3,r:[],t:400}}}));
 localStorage.setItem('sr-d360-study-v1',JSON.stringify({last:{ts:Date.now()-3600e3,title:'カテゴリ(プロファイル / エンゲージメント / 「その他」)',id:'f-category'},done:{intro:1,stream:1,category:1},read:{intro:1,stream:1,category:1,refresh:1}}));
 localStorage.setItem('sr-theme','light');localStorage.setItem('demo-seeded','1');localStorage.setItem('cs-guide-seen','1')}}catch(e){}
})();`;
const U=r=>'http://localhost:8771/index.html#!'+encodeURIComponent(r);
module.exports=async function(){const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2});const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));await p.addInitScript(STUB);
 p.go=async(r,w=4500)=>{await p.goto(U(r));await p.reload();await p.waitForTimeout(w);await p.addStyleTag({content:'html{scroll-behavior:auto!important}'})};return {b,p}};
