import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sc

cale=r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\imagini\imagini"
cale_img=os.path.join(cale,'CThead_gauss.jpg')
img_ct_gauss=plt.imread(cale_img)

Varit = np.array([[0,0.125,0],[0.125,0.5,0.125],[0,0.125,0]])
Vpond = np.array([[0.05,0.1,0.05],[0.1,0.4,0.1],[0.05,0.1,0.05]])

img_ct_filtrata1= sc.convolve(img_ct_gauss,Varit,mode='nearest')
img_ct_filtrata2= sc.convolve(img_ct_gauss,Vpond,mode='nearest')
plt.suptitle("Exercitiu 1 - Filtrare zgomot gaussian")
plt.subplot(1,3,1), plt.imshow(img_ct_gauss, cmap='gray'),plt.title('Imaginea originala')
plt.subplot(1,3,2), plt.imshow(img_ct_filtrata1, cmap='gray'),plt.title('Aritmetica')
plt.subplot(1,3,3), plt.imshow(img_ct_filtrata2, cmap='gray'),plt.title('Ponderata')
plt.show()

img_ct_median = sc.median_filter(img_ct_gauss,footprint=np.ones((3,3)),mode='nearest')
plt.suptitle("Exercitiu 2 - Filtrare mediana zgomot gaussian")
plt.subplot(1,2,1), plt.imshow(img_ct_gauss, cmap='gray'),plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(img_ct_filtrata1, cmap='gray'),plt.title('Mediana')
plt.show()

cale=r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\imagini\imagini"
cale_img=os.path.join(cale,'CThead_impulsiv.jpg')
img_ct_impulsiv=plt.imread(cale_img)

img_ct_median = sc.median_filter(img_ct_impulsiv,footprint=np.ones((3,3)),mode='nearest')
img_ct_filtrata1 = sc.convolve(img_ct_impulsiv,Vpond,mode='nearest')
plt.suptitle("Exercitiu 3 - Filtrari zgomot impulsiv")
plt.subplot(1,3,1), plt.imshow(img_ct_impulsiv, cmap='gray'),plt.title('Imaginea originala')
plt.subplot(1,3,2), plt.imshow(img_ct_filtrata1, cmap='gray'),plt.title('Filtru liniar')
plt.subplot(1,3,3), plt.imshow(img_ct_median, cmap='gray'),plt.title('Filtru median')
plt.show()


