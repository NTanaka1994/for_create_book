import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("DoE_result.csv",encoding="shift-jis")

y_name="y"
y=df[y_name]
x=df.drop(y_name,axis=1)
data=[]
name=[]
for col in x.columns:
    arr=x[col].values
    arr=list(set(arr))
    for row in arr:
        df_q=df.query("%s=='%s'"%(col,row))
        data.append(df_q[y_name].values)
        name.append("%s_%s"%(col,row))
ave=[]
pos=[]
for i in range(len(data)):
    pos.append(i)
    ave.append(np.mean(data[i]))
plt.boxplot(data,labels=name,positions=pos)
#plt.show()
for i in range(int(len(ave)/2)):
    plt.plot([2*i,2*i+1],[ave[2*i],ave[2*i+1]],marker="x")
plt.show()
