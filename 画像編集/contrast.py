from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pic = Image.open("sample.png")
pic = pic.convert(mode="L")
pic = np.array(pic)
h, w = pic.shape[0], pic.shape[1]

hist=[]
for i in range(256):
    hist.append(0)
for y in range(h):
    for x in range(w):
        hist[pic[y][x]] = hist[pic[y][x]] + 1

sumhist = []
for i in range(len(hist)):
    if i == 0:
        sumhist.append(hist[0])
    else:
        sumhist.append(sumhist[i-1]+hist[i])
sumhist = np.array(sumhist)
#
for i in range(len(sumhist)):
    sumhist[i] = int(sumhist[i])
plt.bar(range(256), sumhist)
plt.show()
sumhist = ((sumhist / max(sumhist))) * 255
for y in range(h):
    for x in range(w):
        pic[y][x] = sumhist[pic[y][x]]
plt.axis("off")
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.imshow(pic,cmap="gray")
plt.savefig("contrast.png")
plt.show()

newhist=[]
for i in range(256):
    newhist.append(0)
for y in range(h):
    for x in range(x):
        newhist[pic[y][x]] = newhist[pic[y][x]] + 1
plt.bar(range(256), newhist)
plt.savefig("newhistgram.png")
plt.show()
