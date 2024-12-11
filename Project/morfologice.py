import os
import numpy as np
import matplotlib.pyplot as plt
from functools import partial
from PIL import Image
import cv2
import scipy.ndimage as sc


def afisare(img):
    img_1 = sc.binary_erosion(img)
    img_2 = sc.binary_dilation(img)
    img_3 = sc.binary_opening(img)
    img_4 = sc.binary_closing(img)

    plt.suptitle("Comparatie morfologie")
    plt.subplot(2,3,1),plt.imshow(img,cmap="gray"),plt.title("Imagine originala")
    plt.subplot(2,3,2),plt.imshow(img_1,cmap="gray"),plt.title("Erosiune")
    plt.subplot(2,3,3),plt.imshow(img_2,cmap="gray"),plt.title("Dilatare")
    plt.subplot(2,3,4),plt.imshow(img_3,cmap="gray"),plt.title("Deschidere")
    plt.subplot(2, 3, 5), plt.imshow(img_4, cmap="gray"), plt.title("Inchidere")
    plt.show()


cale = os.path.join(os.path.dirname(__file__), "segmentare_img")

save_directory = os.path.join(os.path.dirname(__file__), "img_finale")
os.makedirs(save_directory, exist_ok=True)

L=256
for i in range(1,11):
    cale_img = os.path.join(cale, f"segmentare_{i}.png")
    try:
        m = plt.imread(cale_img)
        m= m/(L-1)
        print(f"Image segmentare_{i}.png loaded successfully!")

        afisare(m)

        save_path = os.path.join(save_directory, f"final_{i}.png")
        m=m*L
        image = Image.fromarray(sc.binary_closing(m))
        image.save(save_path)

        print(f"Image saved at {save_path}")
    except FileNotFoundError:
        print(f"Image {i}.png not found in {cale}")

print("Segmented images saved")
