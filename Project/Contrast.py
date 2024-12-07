import os
from functools import partial
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import cv2

def rgb2gri(img_in, format):
    img_in=img_in.astype('float')
    s=img_in.shape
    if len(s)==3 and s[2]==3:
        if format=='png':
            img_out=(0.299*img_in[:,:,0]+0.587*img_in[:,:,1]+0.114*img_in[:,:,2])*255
        elif format=='jpg':
            img_out=0.299*img_in[:,:,0]+0.587*img_in[:,:,1]+0.114*img_in[:,:,2]
        img_out=np.clip(img_out, 0,255)
        img_out=img_out.astype('uint8')
        return img_out
    else:
        print('Conversia nu a putut fi realizata deoarece imaginea de intrare nu este color!')
        return img_in
def contrast_liniar_portiuni(img_in, L, a, b, Ta, Tb):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            if (img_in[i, j] < a):
                img_out[i, j] = (Ta / a) * img_in[i, j]
            if (img_in[i, j] >= a and img_in[i, j] <= b):
                img_out[i, j] = Ta + ((Tb - Ta) / (b - a)) * (img_in[i, j] - a)
            if (img_in[i, j] > b):
                img_out[i, j] = Tb + ((L - 1 - Tb) / (L - 1 - b)) * (img_in[i, j] - b)

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

def contrast_putere(img_in, L, r):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            img_out[i,j] = (L-1) * (img_in[i,j]/(L-1))**r

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

def contrast_log(img_in, L):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            img_out[i, j] = ((L-1)/np.log(L)) * np.log(img_in[i, j]+1)

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

def contrast_exp(img_in, L):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            img_out[i, j] = L**(img_in[i,j]/(L-1)) - 1

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

def contrast_putere_cu_pct_fix(img_in, L, r,a):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            if(img_in[i,j]<=a):
                img_out[i,j] = a*(img_in[i,j]/a)**r
            else:
                img_out[i,j] = L-1 - (L-1-a) * ((L-1-img_in[i,j])/(L-1-a))**r

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

def afisare(img,f1,f2,f3):
    img_1 = f1(img)
    img_2 = f2(img)
    img_3 = f3(img)

    plt.suptitle("Comparatie contraste")
    plt.subplot(2,2,1),plt.imshow(img,cmap="gray"),plt.title("Imagine originala")
    plt.subplot(2,2,2),plt.imshow(img_1,cmap="gray"),plt.title(f1.func.__name__)
    plt.subplot(2,2,3),plt.imshow(img_2,cmap="gray"),plt.title(f2.func.__name__)
    plt.subplot(2,2,4),plt.imshow(img_3,cmap="gray"),plt.title(f3.func.__name__)
    plt.show()


def histogram_equalization(img):
    # Convert the image to grayscale if it is not already
    if len(img.shape) == 3:  # If the image is a color image (RGB/BGR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Ensure the image is in 8-bit unsigned integer format (CV_8UC1)
    img = np.uint8(img * 255) if img.dtype != np.uint8 else img

    # Apply histogram equalization
    img_equalized = cv2.equalizeHist(img)

    return img_equalized


cale = os.path.join(os.path.dirname(__file__), "img")

save_directory = os.path.join(os.path.dirname(__file__), "contrast_img")
os.makedirs(save_directory, exist_ok=True)

L = 256
for i in range(1,11):
    cale_img = os.path.join(cale, f"{i}.png")
    try:
        m = plt.imread(cale_img)
        m = m * (L - 1)
        print(f"Image {i}.png loaded successfully!")
        afisare(
            m,
            partial(contrast_putere,L=L,r=1),
            partial(contrast_log,L=L),
            #partial(histogram_equalization),
            partial(contrast_liniar_portiuni,L=L,a=80,b=175,Ta=50,Tb=205)
        )
        save_path = os.path.join(save_directory, f"cntrast_{i}.png")
        image = Image.fromarray(contrast_liniar_portiuni(m,L=L,a=80,b=175,Ta=50,Tb=205))
        image.save(save_path)
        print(f"Image saved at {save_path}")
    except FileNotFoundError:
        print(f"Image {i}.png not found in {cale}")

print("Contrasted images saved")

plt.suptitle("Egalizare de histograma")
for i in range(1,10):
    cale_img = os.path.join(cale, f"{i}.png")
    m = plt.imread(cale_img)
    plt.subplot(3,3,i),plt.imshow(histogram_equalization(m),cmap="gray")
plt.show()