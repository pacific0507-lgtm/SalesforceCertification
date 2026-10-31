/* 保存状態の帯。off=クラウドにつながっていない / f=保存に失敗中の書類 / pend=接続待ち(3秒以降) */
var Sync={off:false,f:{},pend:false,done:false,tp:null,t2:null};
function syncShow(){
  var b=$("#syncb");if(!b)return;
  var failed=Object.keys(Sync.f).length>0,st=Sync.off?"off":failed?"fail":Sync.pend?"pend":"";
  if(!st){b.hidden=true;return}
  b.hidden=false;b.setAttribute("data-s",st);
  $("#syncb-t").textContent=st==="off"?"アカウントに保存されていません(この端末のみ)":st==="fail"?"クラウドへの保存に失敗しています":"クラウドに接続しています…";
  var r=$("#syncb-r");r.hidden=st==="pend";r.textContent=st==="off"?"再読み込み":"再試行";
}
function syncOff(){Sync.off=true;Sync.done=true;Sync.pend=false;clearTimeout(Sync.tp);clearTimeout(Sync.t2);syncShow()}
function syncConnected(){Sync.off=false;Sync.done=true;Sync.pend=false;clearTimeout(Sync.tp);clearTimeout(Sync.t2);syncShow()}
function syncFail(k){Sync.f[k||"x"]=1;syncShow()}
function syncOk(k){delete Sync.f[k||"x"];syncShow()}
Sync.tp=setTimeout(function(){if(!Sync.done){Sync.pend=true;syncShow()}},3000);
Sync.t2=setTimeout(function(){if(!Sync.done)syncOff()},15000);
(function(){var r=$("#syncb-r");if(r)r.onclick=function(){if(Sync.off){location.reload()}else{try{saveQ();scheduleSave(0)}catch(e){}}}})();
window.addEventListener("offline",function(){if(Cloud.db)syncFail("net")});
window.addEventListener("online",function(){if(Cloud.db){syncOk("net");try{saveQ();scheduleSave(0)}catch(e){}}});
