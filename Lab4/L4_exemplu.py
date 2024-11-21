import os
import numpy as np
import matplotlib.pyplot as plt
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

##Citirea imaginii CT_head.tif
cale=r"C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\imagini\imagini"
cale_img=os.path.join(cale,'CThead.tif')
img_ct=plt.imread(cale_img)

cale_img2=os.path.join(cale,'mdb028.png')
img_mamo=plt.imread(cale_img2)

img_mamo_gri=rgb2gri(img_mamo,'png')

#exercitiu 2
def contrast_liniar_portiuni(img_in,L,a,b,Ta,Tb):
    s=img_in.shape
    img_out=np.empty_like(img_in)
    img_in=img_in.astype(float)
    for i in range(0,s[0]):
        for j in range(0,s[1]):
            if (img_in[i,j]<a):
                img_out[i,j]=(Ta/a)*img_in[i,j]
            if(img_in[i,j]>=a and img_in[i,j]<=b):
                img_out[i,j]=Ta+((Tb-Ta)/(b-a))*(img_in[i,j]-a)
            if(img_in[i,j]>b):
                img_out[i,j]=Tb+((L-1-Tb)/(L-1-b))*(img_in[i,j]-b)
                
    img_out=np.clip(img_out,0,255)
    img_out=img_out.astype('uint8')
    return img_out


#exercise 1
def negativare(img_in, L):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            img_out[i, j] = L-1 - img_in[i, j]

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

img_negata = negativare(img_ct, 256)
plt.suptitle("Exercitiu 1 - negativarea CT")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(img_negata, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiu 2
img_modif=contrast_liniar_portiuni(img_ct,256,80,120,60,170)
plt.suptitle('Exercitiu 2 - Modificarea contrastului liniara pe portiuni')
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiu 3
cale_test = os.path.join(cale,'test.png')
test = plt.imread(cale_test)
test_gri = rgb2gri(test,'png')

test_contrastata = contrast_liniar_portiuni(test_gri,256,50,205,30,225)
plt.suptitle("Exercitiu 3 - contrastarea test")
plt.subplot(1,2,1), plt.imshow(test_gri, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(test_contrastata, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()


#exercitiu 4
ct_contrast_max = contrast_liniar_portiuni(img_ct,256,40,160,0,255)
plt.suptitle("Exercitiu 4 - contrastarea maxima ct")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(ct_contrast_max, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiu 5
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

ct_binarizat = binarizare(img_ct,256,120)
plt.suptitle("Exercitiu 5 - binarizarea ct")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(ct_binarizat, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiu 6
ct_interes = (ct_binarizat/255) * img_ct
plt.suptitle("Exercitiu 6 - selectare zona de interes")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(ct_interes, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiul 7
def clipping(img_in, L, a, b, Ta, Tb):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            if (img_in[i, j] < a):
                img_out[i, j] = 0
            if (img_in[i, j] >= a and img_in[i, j] < b):
                img_out[i, j] = Ta + ((Tb - Ta) / (b - a)) * (img_in[i, j] - a)
            if (img_in[i, j] >= b):
                img_out[i, j] = 0

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

ct_clipped = clipping(img_ct,256,100,160,80,180)
plt.suptitle("Exercitiu 7 - clipping ct")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(ct_clipped, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiul 8
def slicing(img_in, L, a, b, Ta):
    s = img_in.shape
    img_out = np.empty_like(img_in)
    img_in = img_in.astype(float)
    for i in range(0, s[0]):
        for j in range(0, s[1]):
            if (img_in[i, j] < a):
                img_out[i, j] = 0
            if (img_in[i, j] >= a and img_in[i, j] < b):
                img_out[i, j] = Ta
            if (img_in[i, j] >= b):
                img_out[i, j] = 0

    img_out = np.clip(img_out, 0, 255)
    img_out = img_out.astype('uint8')
    return img_out

ct_sliced = slicing(img_ct,256,100,160,255)
plt.suptitle("Exercitiul 8 - slicing ct")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(ct_sliced, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiu 9
ct_interes_slice = (ct_sliced/255) *img_ct
plt.suptitle("Exercitiul 9 - selectare zona de interes")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(ct_interes_slice, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiul 10
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

ct_putere = contrast_putere(img_ct,256,3)
plt.suptitle("Exercitiul 10 - contrast putere")
plt.subplot(1,3,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,3,2), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nprelucrata cu r=3')
ct_putere = contrast_putere(img_ct,256,0.5)
plt.subplot(1,3,3), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nprelucrata cu r=0.5')
plt.show()

#exercitiul 11
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

ct_putere = contrast_putere_cu_pct_fix(img_ct,256,3,80)
plt.suptitle("Exercitiul 11 - contrast putere")
plt.subplot(1,3,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,3,2), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nprelucrata\ncu r=3 si a=80')
ct_putere = contrast_putere_cu_pct_fix(img_ct,256,0.5,80)
plt.subplot(1,3,3), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nprelucrata\ncu r=0.5 si a=80')
plt.show()

#exercitiul 12
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

ct_log = contrast_log(img_ct,256)
plt.suptitle("Exercitiul 12 - contrast logaritm")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(ct_log, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiul 13
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

ct_exp= contrast_exp(img_ct,256)
plt.suptitle("Exercitiul 13 - contrast exponential")
plt.subplot(1,2,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,2,2), plt.imshow(ct_exp, cmap='gray'), plt.title('Imaginea prelucrata')
plt.show()

#exercitiul 14
# ct_putere = contrast_putere(img_ct,256,0.2)
# plt.suptitle("Exercitiul 14 - r putere")
# plt.subplot(3,3,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
#
# plt.subplot(3,3,2), plt.imshow(ct_exp, cmap='gray'), plt.title('Imaginea\nexponentiala')
#
# plt.subplot(3,3,3), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=0.2')
#
# ct_putere = contrast_putere(img_ct,256,0.4)
# plt.subplot(3,3,4), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=0.4')
#
# ct_putere = contrast_putere(img_ct,256,0.8)
# plt.subplot(3,3,5), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=0.8')
#
# ct_putere = contrast_putere(img_ct,256,1)
# plt.subplot(3,3,6), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=1')
#
# ct_putere = contrast_putere(img_ct,256,1.5)
# plt.subplot(3,3,7), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=1.5')
#
# ct_putere = contrast_putere(img_ct,256,2)
# plt.subplot(3,3,8), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=2')
#
# ct_putere = contrast_putere(img_ct,256,4)
# plt.subplot(3,3,9), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=4')
# plt.show()

plt.suptitle("Exercitiul 14 - r putere")
plt.subplot(1,3,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,3,2), plt.imshow(ct_exp, cmap='gray'), plt.title('Imaginea\nexponentiala')
ct_putere = contrast_putere(img_ct,256,4.5)
plt.subplot(1,3,3), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=4.5')
plt.show()

#exercitiul 15
plt.suptitle("Exercitiul 15 - r putere log")
plt.subplot(1,3,1), plt.imshow(img_ct, cmap='gray'), plt.title('Imaginea originala')
plt.subplot(1,3,2), plt.imshow(ct_log, cmap='gray'), plt.title('Imaginea\nlogaritm')
ct_putere = contrast_putere(img_ct,256,0.2)
plt.subplot(1,3,3), plt.imshow(ct_putere, cmap='gray'), plt.title('Imaginea\nputere r=0.2')
plt.show()
