import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

fig = plt.figure()
x = np.linspace(0, 4*np.pi, 200)
t = x
ims = []
pi_4 = 4 * np.pi
X, Y = np.meshgrid(x, x)
for i in range(len(t)):
    #Z1 = np.cos((X-np.pi) ** 2 + (Y - np.median(x)) ** 2 - t[i]) *0.95 ** ((X - 3) * (X - 3) + (Y - np.median(x)) * (Y - np.median(x)))
    #Z2 = np.sin((X-(np.pi*3)) **2 + (Y - np.median(x)) ** 2 - t[i]) * 0.95 ** ((X - (np.pi * 3)) * (X - (np.pi * 3)) + (Y - np.median(x)) * (Y - np.median(x)))
    #Z3 = Z1 + Z2
    b = t[len(t)-1]
    #im1 = plt.plot(x, np.sin(x-t[i]), color="#0000FF")
    #im2 = plt.plot(x, np.sin(x-t[i]-b)[:: -1], color="#FF0000")
    im3 = plt.plot(x, -1*np.sin(x-t[i]-b)[:: -1]+np.sin(x-t[i]), color="#FF0000")
    im3 = im3 + plt.plot(x, np.sin(x-t[i]), color="#0000FF")
    im3 = im3 + plt.plot(x, -1*np.sin(x-t[i]-b)[:: -1], color="#00FF00")
    #im3 = plt.contourf(X, Y, Z3, cmap="rainbow")
    ims.append(im3)
    #ims.append(im2)
    
ani = anime.ArtistAnimation(fig, ims, interval=100)
plt.show()
