from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pic = Image.open("sample.png")
pic = pic.convert(mode="L")
pic = np.array(pic)
h, w = pic.shape[0], pic.shape[1]

#拡大行列
by = 1#縦1倍
bx = -1#横-1倍
dst = np.zeros((h*abs(by), w*abs(bx)))
for y in range(h):
    for x in range(w):
        xi = int((x)*bx)
        yi = int((y)*by)
        for i in range(by):
            dst[yi+i][xi] = pic[y][x]
        for i in range(bx):
            dst[yi][xi+i] = pic[y][x]
plt.imshow(dst, cmap="gray")
plt.savefig("expand-1-1.png")
plt.show()
