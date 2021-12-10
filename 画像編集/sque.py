from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pic=Image.open("sample.png")
pic=pic.convert(mode="L")
pic=np.array(pic)
h,w=pic.shape[0],pic.shape[1]

#回転行列
dst=np.zeros((len(pic),len(pic[0])))
rad=np.radians(30)#30°で行う
for y in range(h):
    for x in range(w):
        #xi=int((x-int(w/2))*np.cos(rad)-(y-int(h/2))*np.sin(rad)+int(w/2))
        #yi=int((x-int(w/2))*np.sin(rad)+(y-int(h/2))*np.cos(rad)+int(h/2))
        #if xi<(w-1) and yi<(h-1) and yi>0 and xi>0:
        xi=int((x))
        yi=int((x)*np.tan(rad)+(y))
        if xi<(w-1) and yi<(h-1) and yi>0 and xi>0:
            dst[y][x]=pic[yi][xi]
plt.imshow(dst,cmap="gray")
plt.savefig("aphine_60.png")
plt.show()
