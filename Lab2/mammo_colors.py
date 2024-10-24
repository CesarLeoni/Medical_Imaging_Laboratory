import os

import numpy as np
from matplotlib import pyplot as plt

# mammografie
cale = r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\lab1_stefana\L1_imagini"
cale_img_mamo = os.path.join(cale, "mdb028.png")
img_mamo = plt.imread(cale_img_mamo)

# plt.imshow(img_mamo)
# plt.show()

img_green = plt.imread(cale_img_mamo)
img_green[:, :, 0] = img_green[:, :, 2] = 0
plt.subplot(1, 3, 1)
plt.title("Green\nMammography")
plt.imshow(img_green)

img_turqoise = plt.imread(cale_img_mamo)
img_turqoise[:, :, 0] *= 0.15
img_turqoise[:, :, 1] *= 0.78
img_turqoise[:, :, 2] *= 0.82
plt.subplot(1, 3, 2)
plt.title("Turqoise\nMammography")
plt.imshow(img_turqoise)

img_yellow = plt.imread(cale_img_mamo)
img_yellow[:, :, 2] = 0
plt.subplot(1, 3, 3)
plt.title("Yellow\nMammography")
plt.imshow(img_yellow)
plt.show()
