import os
import numpy as np
import matplotlib.pyplot as plt


smile = 4*np.ones((8,9),dtype='uint8')
smile[0,:]=0
smile[1:3,1:4]=1
smile[1:3,5:8]=1
smile[3:5,4]=2
smile[7,2:7]=5
smile[[6,6],[1,7]]=5

plt.figure("smiley face")
plt.imshow(smile,cmap='gray',vmin=0,vmax=5)
plt.show()

img_shape = smile.shape
print("Imaginea smile are "+str(img_shape[0])+" linii si "+
    str(img_shape[1])+" coloane")

print("Valorile imaginii smile sunt de tipul "+str(type(smile[0,0])))

h,_ = np.histogram(smile,bins = 256, range = [0,256])
plt.figure()
plt.bar(range(256),h)
plt.show()

cale = r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\lab1_stefana\L1_imagini"
cale_img = os.path.join(cale,"CThead.tif")
img = plt.imread(cale_img)

plt.figure('Figura 1')
plt.imshow(img)
plt.show()

plt.figure('Figura 2')
plt.imshow(img,cmap='gray',vmin=0,vmax=255)
plt.show()




