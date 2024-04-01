from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pic = Image.open("sample.png")
pic = pic.convert(mode="L")
pic = np.array(pic)
h, w = pic.shape[0], pic.shape[1]

#拡大行列
sy = - 100#縦100移動
sx = 20#横20移動
dst = np.zeros((h+abs(sy), w+abs(sx)))
for y in range(h):
    for x in range(w):
        xi = int((x)+sx)
        yi = int((y)+sy)
        dst[yi][xi] = pic[y][x]
plt.imshow(dst, cmap="gray")
plt.savefig("expand-1-1.png")
plt.show()
