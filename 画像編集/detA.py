from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pic = Image.open("sample.png")
pic = pic.convert(mode="L")
pic = np.array(pic)
detp = np.linalg.pinv(pic)
plt.imshow(detp, cmap="gray")
plt.show()

plt.imshow(np.dot(pic, detp), cmap="gray")
plt.show()
