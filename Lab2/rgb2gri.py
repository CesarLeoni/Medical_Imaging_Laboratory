import os

import numpy as np
from matplotlib import pyplot as plt


def rgb2gri(img_in, format):
    img_in = img_in.astype('float')
    s = img_in.shape
    if len(s) == 3 and s[2] == 3:
        if format == 'png':
            img_out = (0.299 * img_in[:, :, 0] + 0.587 * img_in[:, :, 1] + 0.114 * img_in[:, :, 2]) * 255
        elif format == 'jpg':
            img_out = 0.299 * img_in[:, :, 0] + 0.587 * img_in[:, :, 1] + 0.114 * img_in[:, :, 2]
        img_out = np.clip(img_out, 0, 255)
        img_out = img_out.astype('uint8')
        return img_out
    else:
        print('Conversia nu a putut fi realizata deoarece imaginea de intrare nu este color!')
        return img_in


cale = r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\lab1_stefana\L1_imagini"
cale_img = os.path.join(cale,"Scintigrafia.jpg")
img = plt.imread(cale_img)

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(1,2,2)
plt.imshow(rgb2gri(img, "jpg"),cmap="gray")
plt.title("Grayscale Image")
plt.show()

