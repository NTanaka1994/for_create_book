from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pic=Image.open("sample.png")
pic=pic.convert(mode="L")
pic=np.array(pic)
h,w=pic.shape[0],pic.shape[1]
dst=np.zeros((h,w))

for y in range(h-2):
    for x in range(w-2):
        dst[y][x]=abs(int(pic[y+1][x+1])-int(pic[y+2][x+1]))+abs(int(pic[y+1][x+1])-int(pic[y][x+1]))
        dst[y][x]=dst[y][x]+abs(int(pic[y+1][x+1])-int(pic[y+1][x+2]))+abs(int(pic[y+1][x+1])-int(pic[y+1][x]))
plt.imshow(dst,cmap="gray")
plt.savefig("edge1.png")
plt.show()

dst2=np.zeros((h,w))
for y in range(len(dst)-2):
    for x in range(len(dst[y])-2):
        dst2[y][x]=(int(dst[y+1][x+1])-int(dst[y+2][x+1]))+(int(dst[y+1][x+1])-int(dst[y][x+1]))
        dst2[y][x]=dst[y][x]+(int(dst[y+1][x+1])-int(dst[y+1][x+2]))+(int(dst[y+1][x+1])-int(dst[y+1][x]))
plt.imshow(dst2,cmap="gray")
plt.savefig("edge2.png")
plt.show()

dst3=dst2+pic
dst3=(dst3-min(dst3.flatten()))/(max(dst3.flatten())-min(dst3.flatten()))
dst3=dst3*255
plt.imshow(dst3,cmap="gray")
plt.savefig("edge3.png")
plt.show()

for y in range(h-2):
    for x in range(w-2):
        dst[y][x]=(int(pic[y+1][x+1])-int(pic[y+2][x+1]))+(int(pic[y+1][x+1])-int(pic[y][x+1]))
        dst[y][x]=dst[y][x]+(int(pic[y+1][x+1])-int(pic[y+1][x+2]))+(int(pic[y+1][x+1])-int(pic[y+1][x]))
dst4=pic+dst
dst4=(dst4-min(dst4.flatten()))/(max(dst4.flatten())-min(dst4.flatten()))
dst4=dst4*255
plt.imshow(dst4,cmap="gray")
plt.savefig("edge4.png")
plt.show()
