"""CommitStudy に「保存状態の帯」を入れる(社労士版と同じ)。
アカウント(クラウド)に保存されていないときだけ、メニューバーの一番上に赤い帯を出す。
  off  = クラウドにつながっていない(この端末にだけ保存中)… 「再読み込み」ボタン
  fail = クラウドへの保存に失敗している … 「再試行」ボタン
  pend = 接続待ち(3秒経っても未接続のとき、黄色) / 15秒つながらなければ off
使い方: python3 patch_syncbar.py <index.html> <出力>   (syncbar.js / syncbar.css を同じフォルダに置く)
"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")

css = open(os.path.join(here, "syncbar.css"), encoding="utf-8").read()
js = open(os.path.join(here, "syncbar.js"), encoding="utf-8").read()
# テンプレート
rep(jesc(".mbar.hide{transform:none}\n"), jesc(".mbar.hide{transform:none}\n" + css))
rep(jesc('<div class="mbar" id="mbar" role="toolbar" aria-label="メニュー">\n'),
    jesc('<div class="mbar" id="mbar" role="toolbar" aria-label="メニュー">\n <div class="syncb" id="syncb" role="status" aria-live="polite" hidden><span id="syncb-t"></span><button type="button" id="syncb-r"></button></div>\n'))
# エンジン
rep('function cdoc(name){return Cloud.db.doc("data/users/"+Cloud.uid+"/"+name)}\n',
    'function cdoc(name){return Cloud.db.doc("data/users/"+Cloud.uid+"/"+name)}\n' + js)
rep('function setStore(ok){\n', 'function setStore(ok){\n  if(ok===false)syncFail("study");else if(ok===true)syncOk("study");\n')
rep('qcloud.set({json:JSON.stringify(S),ts:S.ts}).catch(function(){})}catch(e){}},1500)}}',
    'qcloud.set({json:JSON.stringify(S),ts:S.ts}).then(function(){syncOk("quiz")},function(){syncFail("quiz")})}catch(e){syncFail("quiz")}},1500)}}')
rep('cloudReady.then(function(d){if(!d)gStat(', 'cloudReady.then(function(d){if(!d)syncOff();if(!d)gStat(')
rep('    }catch(e){qcloud=null}\n    try{\n      qaCol=', '    }catch(e){qcloud=null;syncFail("quiz")}\n    try{\n      qaCol=')
rep('    }catch(e){qaCol=null}\n    setTimeout(function(){guardSync()', '    }catch(e){qaCol=null}\n    syncConnected();\n    setTimeout(function(){guardSync()')
rep('  }catch(e){doc=null;setStore()}finally{qaRes();renderQa()}', '  }catch(e){doc=null;setStore();syncOff()}finally{qaRes();renderQa()}')
open(out, "w", encoding="utf-8").write(s); print("ok")
