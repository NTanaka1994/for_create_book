from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random as rand

def filter(pic):
    h,w=pic.shape[0],pic.shape[1]
    dst=np.zeros((h,w))
    for y in range(h):
        for x in range(w):
            if y==0 and x==0:
                dst[y][x]=int((int(pic[y][x])+int(pic[y+1][x])+int(pic[y][x+1])+int(pic[y+1][x+1]))/4)
            elif y==0 and x==(w-1):
                dst[y][x]=int((int(pic[y][x])+int(pic[y+1][x])+int(pic[y][x-1])+int(pic[y+1][x-1]))/4)
            elif y==(h-1) and x==0:
                dst[y][x]=int((int(pic[y][x])+int(pic[y-1][x])+int(pic[y][x+1])+int(pic[y-1][x+1]))/4)
            elif y==(h-1) and x==(w-1):
                dst[y][x]=int((int(pic[y][x])+int(pic[y-1][x])+int(pic[y][x-1])+int(pic[y-1][x-1]))/4)
            elif y==0:
                dst[y][x]=int((int(pic[y][x])+int(pic[y+1][x])+int(pic[y][x+1])+int(pic[y][x-1])+int(pic[y+1][x+1])+int(pic[y+1][x-1]))/6)
            elif y==(h-1):
                dst[y][x]=int((int(pic[y][x])+int(pic[y-1][x])+int(pic[y][x+1])+int(pic[y][x-1])+int(pic[y-1][x+1])+int(pic[y-1][x-1]))/6)
            elif x==0:
                dst[y][x]=int((int(pic[y-1][x])+int(pic[y][x])+int(pic[y+1][x])+int(pic[y-1][x+1])+int(pic[y][x+1])+int(pic[y+1][x+1]))/6)
            elif x==(w-1):
                dst[y][x]=int((int(pic[y-1][x])+int(pic[y][x])+int(pic[y+1][x])+int(pic[y-1][x-1])+int(pic[y][x-1])+int(pic[y+1][x-1]))/6)
            else:
                dst[y][x]=int((int(pic[y-1][x-1])+int(pic[y-1][x])+int(pic[y-1][x-1])+int(pic[y][x-1])+int(pic[y][x])+int(pic[y][x+1])+int(pic[y+1][x-1])+int(pic[y+1][x])+int(pic[y+1][x+1]))/9)
    return dst
            
name="zeroonenoise.png"
pic=Image.open(name)
pic=pic.convert(mode="L")
pic=np.array(pic)
dst=filter(pic)
plt.axis("off")
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(dst,cmap="gray")
plt.savefig("ave_"+name)
plt.show()
