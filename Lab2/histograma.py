# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:30:05 2021

@author: andre
"""

import os
import numpy as np
import matplotlib.pyplot as plt

cale = r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\lab1_stefana\L1_imagini"
img = plt.imread(os.path.join(cale,'CThead.tif'))
h,_ = np.histogram(img,bins = 256, range=(0,256))
#h = np.histogram(img, bins=256, range=[0,256]) - error

plt.figure()
plt.subplot(3,3,1), plt.imshow(img, cmap = 'gray'), plt.title('Imagine')
plt.subplot(3,3,2), plt.plot(range(256),h), plt.title('Histograma Plot')
plt.subplot(3,3,3), plt.plot(h), plt.yscale('log'),
plt.title('Histograma Plot\n axa y logaritmica')
plt.subplot(3,3,7), plt.bar(range(256),h,width=0.3), plt.title('Histograma Bar')
plt.subplot(3,3,8), plt.bar(range(256),h,width=0.3),plt.yscale('log'),
plt.title('Histograma Bar\n axa y logaritmica')
plt.show()