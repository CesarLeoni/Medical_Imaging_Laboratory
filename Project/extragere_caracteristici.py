import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# Directorii de lucru
cale = os.path.join(os.path.dirname(__file__), "img")
cale_contrast = os.path.join(os.path.dirname(__file__), "contrast_img")
cale_segmentare = os.path.join(os.path.dirname(__file__), "segmentare_img")
cale_final = os.path.join(os.path.dirname(__file__), "img_finale")

cale_procesare = os.path.join(os.path.dirname(__file__), "img_proces")
os.makedirs(cale_procesare, exist_ok=True)

# Procesarea imaginilor
for i in range(1, 11):
    try:
        # Creează o figură pentru imaginea curentă
        plt.figure(figsize=(10, 8))

        # Imagine Originală
        cale_img = os.path.join(cale, f"{i}.png")
        try:
            originala = plt.imread(cale_img)
            plt.subplot(2, 2, 1), plt.imshow(originala, cmap="gray"), plt.title("Imagine originală")
        except FileNotFoundError:
            print(f"Fișierul nu a fost găsit: {cale_img}")

        # Imagine după ajustarea contrastului
        contrast_img = os.path.join(cale_contrast, f"contrast_{i}.png")
        try:
            contrast = plt.imread(contrast_img)
            plt.subplot(2, 2, 2), plt.imshow(contrast, cmap="gray"), plt.title("După contrast")
        except FileNotFoundError:
            print(f"Fișierul nu a fost găsit: {contrast_img}")

        # Imagine segmentată
        img_segmentata = os.path.join(cale_segmentare, f"segmentare_{i}.png")
        try:
            segmentare = plt.imread(img_segmentata)
            plt.subplot(2, 2, 3), plt.imshow(segmentare, cmap="gray"), plt.title("După segmentare")
        except FileNotFoundError:
            print(f"Fișierul nu a fost găsit: {img_segmentata}")

        # Imagine finală
        img_final = os.path.join(cale_final, f"final_{i}.png")
        try:
            final = plt.imread(img_final)
            plt.subplot(2, 2, 4), plt.imshow(final, cmap="gray"), plt.title("Finală")
        except FileNotFoundError:
            print(f"Fișierul nu a fost găsit: {img_final}")

        # Adaugă un titlu general și ajustează layout-ul
        plt.suptitle(f"Parcurs imagine {i}", fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Lasă spațiu pentru titlu

        # Salvează și afișează figura
        cale_salvare = os.path.join(cale_procesare, f"proces_{i}.png")
        plt.savefig(cale_salvare, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Imaginea {i}.png a fost procesată și salvată în {cale_salvare}")

    except Exception as e:
        print(f"Eroare la procesarea imaginii {i}: {e}")
