from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random as rand

pic=Image.open("sample.png")
pic=pic.convert(mode="L")
pic=np.array(pic)
h,w=pic.shape[0],pic.shape[1]
rpic=pic
spic=pic
gpic=pic
#雑音座標
x=[]
y=[]
for i in range(100):
    x.append(rand.randint(0,w-1))
    y.append(rand.randint(0,h-1))

#一様雑音
for i in range(100):
    rpic[y[i]][x[i]]=rand.randint(0,255)
plt.axis("off")
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(rpic,cmap="gray")
plt.savefig("randnoise.png")
plt.show()

#ガウス雑音
noise=np.random.normal(loc=128,scale=15,size=100)
for i in range(100):
    spic[y[i]][x[i]]=noise[i]
plt.axis("off")
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(spic,cmap="gray")
plt.savefig("gaussnoise.png")
plt.show()

#ゴマ塩雑音
for i in range(100):
    gpic[y[i]][x[i]]=rand.randint(0,1)*255
plt.axis("off")
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(gpic,cmap="gray")
plt.savefig("zeroonenoise.png")
plt.show()
