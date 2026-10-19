# Checks every internal href/src resolves, incl. #anchors, and HTML tag balance.
import os,re,sys
from html.parser import HTMLParser
VOID={"meta","link","img","br","hr","input"}
class P(HTMLParser):
    def __init__(s):super().__init__();s.refs=[];s.ids=set();s.stack=[];s.err=[]
    def handle_starttag(s,t,a):
        a=dict(a)
        if "id" in a:s.ids.add(a["id"])
        for k in("href","src"):
            if a.get(k):s.refs.append(a[k])
        if t not in VOID:s.stack.append(t)
    def handle_endtag(s,t):
        if t in VOID:return
        if not s.stack or s.stack[-1]!=t:s.err.append(f"unexpected </{t}> (open: {s.stack[-3:]})")
        else:s.stack.pop()
pages={};bad=0
for root,_,fs in os.walk("."):
    for f in fs:
        if f.endswith(".html"):
            p=os.path.normpath(os.path.join(root,f));x=P();x.feed(open(p).read());pages[p]=x
for p,x in pages.items():
    for e in x.err+([f"unclosed {x.stack}"] if x.stack else []):print(p,"HTML:",e);bad+=1
    for r in x.refs:
        if re.match(r"(https?:|mailto:|solana:)",r):continue
        path,_,frag=r.partition("#")
        tgt=os.path.normpath(os.path.join(os.path.dirname(p),path)) if path else p
        if not os.path.exists(tgt):print(p,"MISSING",r);bad+=1;continue
        if frag and frag not in pages.get(tgt,P()).ids:print(p,"BAD ANCHOR",r);bad+=1
print("OK" if not bad else f"{bad} problems");sys.exit(bool(bad))
