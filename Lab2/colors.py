import os

import numpy as np
from matplotlib import pyplot as plt

cale = r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\lab1_stefana\L1_imagini"
cale_img = os.path.join(cale,"Scintigrafia.jpg")
img = plt.imread(cale_img)

plt.subplot(1,3,1)
plt.imshow(img[:,:,0], cmap="gray")
plt.title("Red")

plt.subplot(1,3,2)
plt.imshow(img[:,:,1], cmap="gray")
plt.title("Green")

plt.subplot(1,3,3)
plt.imshow(img[:,:,2], cmap="gray")
plt.title("Blue")
plt.show()

hRed,_ = np.histogram(img[:,:,0],bins = 256, range=(0,256))
hGreen,_ = np.histogram(img[:,:,0],bins = 256, range=(0,256))
hBlue,_ = np.histogram(img[:,:,0],bins = 256, range=(0,256))

plt.subplot(1,3,1)
plt.bar(range(256),hRed)
plt.title("Red Histogram")

plt.subplot(1,3,2)
plt.bar(range(256),hGreen)
plt.title("Green Histogram")

plt.subplot(1,3,3)
plt.bar(range(256),hBlue)
plt.title("Blue Histogram")
plt.show()

#9
hRed_dens = hRed/img[:,:,0].size
H = np.cumsum(hRed_dens)
plt.figure()
plt.plot(H)
plt.show()


#10
img_blue_colBlue = np.zeros([img.shape[0],img.shape[1],3],
                            dtype='uint8')
img_blue_colBlue [:,:,2] = img[:,:,2]
plt.subplot(1,3,1)
plt.imshow(img_blue_colBlue)
plt.title("Blue plane\ncolored blue")

plt.subplot(1,3,2)
plt.imshow(img[:,:,1], cmap="gray")
plt.title("Green plane\ncolored grayscale")

img_green_colMagenta = np.zeros([img.shape[0],img.shape[1],3],
                                dtype='uint8')
img_green_colMagenta [:,:,0] = img[:,:,1]
img_green_colMagenta [:,:,2] = img[:,:,1]
plt.subplot(1,3,3)
plt.imshow(img_green_colMagenta)
plt.title("Green plane\ncolored magenta")
plt.show()





