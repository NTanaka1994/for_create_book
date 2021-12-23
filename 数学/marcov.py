import pandas as pd
import random

def marcovPredict(data,word,num):
    Pt={}
    P={}
    for i in range(len(data)-1):
        try:
            _=Pt[data[i]]
            Pt[data[i]]=Pt[data[i]]+1
        except:
            Pt[data[i]]=1
        try:
            _=P[data[i]][data[i+1]]
            P[data[i]][data[i+1]]=P[data[i]][data[i+1]]+1
        except:
            tmp={data[i+1]:1}
            if data[i] in P:
                P[data[i]].update(tmp)
            else:
                P[data[i]]=tmp
    Pa={}
    for col1 in Pt:
        tmp=[]
        for col2 in Pt:
            if col2 in P[col1]:
                tmp.append([col2,P[col1][col2]/Pt[col1]])
        tmp=sorted(tmp,key=lambda x:x[1],reverse=True)
        tmp=pd.DataFrame(tmp)
        tmp[1]=tmp[1].cumsum()
        tmp=tmp.values
        Pa[col1]=tmp
    text=word
    for i in range(num):
        rand=random.random()
        for j in range(len(Pa[word])):
            if rand<Pa[word][j][1]:
                text=text+Pa[word][j][0]
                word=Pa[word][j][0]
                break
    return text

from janome.tokenizer import Tokenizer
t=Tokenizer()
f=open("sample.txt",encoding="utf-8")
text=f.read()
f.close()
text=text.replace("「","")
text=text.replace("」","")
text=text.replace("『","")
text=text.replace("』","")
text=text.replace("(","")
text=text.replace(")","")
text=text.replace("（","")
text=text.replace("）","")

wlist=list(t.tokenize(text,wakati=True))
text=marcovPredict(wlist,wlist[0],300)
print(text)
