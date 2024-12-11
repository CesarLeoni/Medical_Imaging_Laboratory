import os
import numpy as np
import matplotlib.pyplot as plt
from functools import partial
from PIL import Image
import cv2

def binarizare(img_in, L, a):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            if (img_in[i, j] < a):
                img_out[i, j] = 0
            else:
                img_out[i, j] = L-1

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

cale = os.path.join(os.path.dirname(__file__), "contrast_img")

save_directory = os.path.join(os.path.dirname(__file__), "segmentare_img")
os.makedirs(save_directory, exist_ok=True)

L=256
prag = 128

plt.suptitle("Imagini segmentate")

for i in range(1,11):
    cale_img = os.path.join(cale, f"contrast_{i}.png")
    try:
        m = plt.imread(cale_img)
        m = m * (L - 1)
        print(f"Image {i}.png loaded successfully!")


        save_path = os.path.join(save_directory, f"segmentare_{i}.png")
        image = Image.fromarray(binarizare(m,L,prag))
        image.save(save_path)

        plt.subplot(2, 5, i), plt.imshow(image, cmap="gray"), plt.title(f"img{i}")

        print(f"Image saved at {save_path}")
    except FileNotFoundError:
        print(f"Image {i}.png not found in {cale}")

print("Segmented images saved")
plt.show()

def praguire_otsu(img):
    # Verifică dacă imaginea este una color (RGB/BGR)
    if len(img.shape) == 3:  # Imagine color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convertim imaginea în 8 biți dacă nu este deja
    if img.dtype != np.uint8:
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)  # Normalizează la intervalul [0, 255]
        img = np.uint8(img)  # Conversie la 8 biți

    # Aplică metoda Otsu pentru praguire
    _, img_praguita = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return img_praguita


cale_img = os.path.join(cale, f"contrast_1.png")
m = plt.imread(cale_img)
m = m * (L - 1)

plt.suptitle("Exemplu otsu")
plt.plot(), plt.imshow(praguire_otsu(m), cmap="gray"), plt.title(1)
plt.show()
