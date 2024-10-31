import os

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

cale = r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\lab1_stefana\L1_imagini"

files =['scintigrafia.jpg', 'CThead.tif', 'mdb028.png', 'prosthesis.bmp']

#1
# for i in files:
#     cale_img = os.path.join(cale, i)
#     img_plt = plt.imread(cale_img)
#     img_pil = Image.open(cale_img)
#     print('fisierul: ', i, ' are dimensiunile \n in matplotlib', img_plt.shape,
#           '\n in PIL ', img_pil.size)
#     print('benzile fisierului ', i, ' sunt ', img_pil.getbands())
#     img_format = img_pil.format
#     print('Formatul imaginii este: ', img_format)
#     print()

#2
# for i in files:
#     cale_img = os.path.join(cale, i)
#     img_plt = plt.imread(cale_img)
#     img_pil = Image.open(cale_img)
#     print('fisierul: ', i)
#     print('tipul de date al unui pixel: ',type(img_plt[0][0]))
#     print('minim: ',np.min(img_plt),' maxim: ',np.max(img_plt))
#     print()

#3
for i in os.listdir(cale):
    cale_img = os.path.join(cale, i)
    img = Image.open(cale_img)
    plt.imshow(img,cmap='gray')
    plt.show()