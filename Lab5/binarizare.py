import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sc

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

#exercitiu 4
cale=r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\imagini\imagini"
cale_img=os.path.join(cale,'test.png')
img_test=plt.imread(cale_img)

img_test_bin = binarizare(rgb2gri(img_test,"png"),256,127)
plt.suptitle("Exercitiu 4 - Binarizare")
plt.subplot(1,2,1),plt.imshow(img_test,cmap="gray"),plt.title("IMagine originala")
plt.subplot(1,2,2),plt.imshow(img_test_bin,cmap="gray"),plt.title("Imagine binarizare")
plt.show()


#exercitiu 5

def contur(img_in,c):
    vx = np.array([[1, 0, -1], [c, 0, -c], [1, 0, -1]])
    vy = np.array([[1, c, 1], [0, 0, 0], [-1, -c, -1]])

    grad_x = sc.convolve(img_test_gri, vx, mode='reflect')
    grad_y = sc.convolve(img_test_gri, vy, mode='reflect')

    contour_test = np.sqrt(grad_x ** 2 + grad_y ** 2)
    return contour_test

img_test_gri = rgb2gri(img_test,"png")
plt.suptitle("Exercitiul 5 - conturul")
plt.subplot(2,2,1),plt.imshow(img_test_gri,cmap="gray"),plt.title("Img originala")
plt.subplot(2,2,2),plt.imshow(contur(img_test_gri,1),cmap="gray"),plt.title("Contur c=1")
plt.subplot(2,2,3),plt.imshow(contur(img_test_gri,np.sqrt(2)),cmap="gray"),plt.title("Contur c=sqrt(2)")
plt.subplot(2,2,4),plt.imshow(contur(img_test_gri,2),cmap="gray"),plt.title("Contur c=2")
plt.show()

#ex 6
a = np.array([[1,1,1,1,1]])
b= np.array([[1],[1],[1]])
Vpond = np.array([[1,1,1],[1,1,1],[1,1,1]])
Varit = np.array([[0,1,0],[1,1,1],[0,1,0]])
Vd1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
Vd2 = np.array([[0,0,1],[0,1,0],[1,0,0]])
print(a)
print(b)
print(Vpond)
print(Varit)
print(Vd1)
print(Vd2)

array_of_matrices = np.array([a, b, Vpond, Varit, Vd1, Vd2], dtype=object)
print(array_of_matrices)

#exercitiu 7
plt.suptitle("Exercitiul 7 - erodare")
for i in range(1, 7):
    erodare1 = sc.binary_erosion(img_test_bin, structure=array_of_matrices[i-1])
    plt.subplot(2, 3, i)
    plt.imshow(erodare1, cmap="gray")
    plt.title(f"Erodare {i}")  # Use f-string for string formatting

plt.show()

#exercitiul 8
plt.suptitle("Exercitiul 8 - dilatare")
for i in range(1, 7):
    dilatare = sc.binary_dilation(img_test_bin, structure=array_of_matrices[i-1])
    plt.subplot(2, 3, i)
    plt.imshow(dilatare, cmap="gray")
    plt.title(f"Dilatare {i}")  # Use f-string for string formatting

plt.show()

#exercitiul 9
plt.suptitle("Exercitiul 9 - deschidere")
for i in range(1, 7):
    deschidere = sc.binary_opening(img_test_bin, structure=array_of_matrices[i-1])
    plt.subplot(2, 3, i)
    plt.imshow(deschidere, cmap="gray")
    plt.title(f"Deschidere {i}")  # Use f-string for string formatting

plt.show()

#exercitiul 10
plt.suptitle("Exercitiul 10 - deschidere(erodare,dilatare)")
for i in range(1, 7):
    erodare = sc.binary_erosion(img_test_bin, structure=array_of_matrices[i-1])
    deschidere = sc.binary_dilation(erodare,structure=array_of_matrices[i-1])
    plt.subplot(2, 3, i)
    plt.imshow(deschidere, cmap="gray")
    plt.title(f"{i}")  # Use f-string for string formatting
plt.show()

#exercitiul 11
plt.suptitle("Exercitiul 11 - inchidere")
for i in range(1, 7):
    inchidere = sc.binary_closing(img_test_bin, structure=array_of_matrices[i-1])
    plt.subplot(2, 3, i)
    plt.imshow(inchidere, cmap="gray")
    plt.title(f"Inchidere {i}")  # Use f-string for string formatting

plt.show()

#exercitiul 12
plt.suptitle("Exercitiul 12 - inchidere(dilatare,erodare)")
for i in range(1, 7):
    dilatare = sc.binary_dilation(img_test_bin, structure=array_of_matrices[i-1])
    inchidere = sc.binary_erosion(dilatare,structure=array_of_matrices[i-1])
    plt.subplot(2, 3, i)
    plt.imshow(inchidere, cmap="gray")
    plt.title(f"{i}")  # Use f-string for string formatting
plt.show()

#exercitiul 13
plt.suptitle("Exercitiul 13 - contur exterior")
for i in range(1, 7):
    ext = sc.binary_dilation(img_test_bin,structure=array_of_matrices[i-1]).astype('uint8')*255-img_test_bin
    plt.subplot(2, 3, i)
    plt.imshow(ext, cmap="gray")
    plt.title(f"{i}")  # Use f-string for string formatting
plt.show()

plt.suptitle("Exercitiul 13 - contur interior")
for i in range(1, 7):
    int = img_test_bin - sc.binary_erosion(img_test_gri,structure=array_of_matrices[i-1]).astype('uint8')*255
    plt.subplot(2, 3, i)
    plt.imshow(ext, cmap="gray")
    plt.title(f"{i}")  # Use f-string for string formatting
plt.show()

plt.suptitle("Exercitiul 13 - gradient morfologic")
for i in range(1, 7):
    int = (sc.binary_dilation(img_test_gri,structure=array_of_matrices[i-1]).astype('uint8') -
           sc.binary_erosion(img_test_gri,structure=array_of_matrices[i-1]).astype('uint8'))
    plt.subplot(2, 3, i)
    plt.imshow(ext, cmap="gray")
    plt.title(f"{i}")  # Use f-string for string formatting
plt.show()