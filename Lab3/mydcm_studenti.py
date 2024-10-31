

import pydicom as dicom
import os
import matplotlib.pyplot as plt

cale = r'C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\Laboratorul 3\dicom1'
cale_dcm = os.path.join(cale, 'img01.dcm')
mydcm = dicom.dcmread(cale_dcm)

#4
# dcm_header = mydcm.dir()
#
# dcm_pat = mydcm.dir('pat')
#
# mygrup = []
# for i in dcm_header:
#     if mydcm.data_element(i).tag.group == int("0x0010",16):
#         mygrup.append(i)
#
# xx = mydcm.data_element('PatientName')
# xx.value
# xx.tag
#
# dcm_img = mydcm.pixel_array
# plt.figure()
# plt.imshow(dcm_img, cmap = 'gray')
# plt.show()
#
# for i,row in mydcm.items():
#   if row.VR == "PN":
#       print('VR:', row.VR, ' denumire element: ', mydcm[i].keyword)
#       print('old value: ', mydcm[i].value)
#       mydcm[i].value = "anonymous"
#       print('new value: ', mydcm[i].value)
#
# dicom.dcmwrite(os.path.join(cale,'anon.dcm'),mydcm)

#5
# cale2 = r'C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\Laboratorul 3\dicom2'
#
# a=os.listdir(cale2)
# print(a)
# for i in os.listdir(cale2):
#     cale_dcm2 = os.path.join(cale2, i)
#     if i.endswith(".dcm"):
#         mydcm = dicom.dcmread(cale_dcm2)
#
#         dcm_image = mydcm.pixel_array
#         plt.imshow(dcm_image)
#         plt.show()

#6
cale2 = r'C:\1. Cesar\An 4 Sem 1\IM - Imagistica Medicala\Laboratorul 3\dicom2'
cale_dcm2 = os.path.join(cale2, 'img01.dcm')
mydcm6 = dicom.dcmread(cale_dcm2)

# Extragem și afișăm informațiile dorite
print("Imaginea aleasa: ",'img01.dcm')
img = mydcm6.pixel_array
plt.imshow(img,cmap='gray')
plt.show()
print("Numele pacientului:", mydcm6.get("PatientName", "Necunoscut"))
print("Greutatea pacientului:", mydcm6.get("PatientWeight", "Necunoscut"),"kg")
print("Producătorul aparatului de achizitie:", mydcm6.get("Manufacturer", "Necunoscut"))
print("Tipul investigației (Modality):", mydcm6.get("Modality", "Necunoscut"))



