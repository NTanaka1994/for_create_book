from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pic = Image.open("sample.png")
pic = pic.convert(mode="L")
pic = np.array(pic)
h, w = pic.shape[0], pic.shape[1]

hist = []
for i in range(256):
    hist.append(0)
for y in range(h):
    for x in range(w):
        hist[pic[y][x]] = hist[pic[y][x]] + 1
plt.bar(range(256), hist)
plt.savefig("histgram.png")
plt.show()

sumhist=[]
for i in range(len(hist)):
    if i==0:
        sumhist.append(hist[0])
    else:
        sumhist.append(sumhist[i-1]+hist[i])
plt.bar(range(256),sumhist)
plt.savefig("sumhistgram.png")
plt.show()
