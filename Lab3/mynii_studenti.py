# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:54:30 2021

@author: andre
"""

import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

cale = r'C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\imagini\imagini'
cale_nii = os.path.join(cale,'pancreas_001.nii.gz' )

#8
img = nib.load(cale_nii)
myimg = np.asarray(img.dataobj)
img1 = myimg[:,:,1]

print('fisierul: ', 'img1')
print('tipul de date al unui pixel: ',type(img1[0][0]))
print('minim: ',np.min(img1),' maxim: ',np.max(img1))
print()
plt.imshow(img1,cmap='gray')
plt.show()

#9
img2 =myimg[:,:,2]
print('fisierul: ', 'img2')
print('tipul de date al unui pixel: ',type(img2[0][0]))
print('minim: ',np.min(img2),' maxim: ',np.max(img2))
print()
plt.imshow(img2,cmap='gray')
plt.show()






