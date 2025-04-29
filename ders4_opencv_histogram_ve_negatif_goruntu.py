"""
Bu derste:
- Negatif görüntü oluşturma
- Histogram hesaplama ve görselleştirme
- Histogram eşitleme (kontrast iyileştirme)
uygulamaları yapılmıştır.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# NEGATİF GÖRÜNTÜ
# -------------------------------
image = cv2.imread('mammogram.png')  # Görüntü okunur (renkli)
print("Görüntü veri tipi:", image.dtype)

# Negatif görüntü: 255 - piksel değeri
img_neg = 255 - image

# Orijinal ve negatif görüntü ekranda gösterilir
cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# HISTOGRAM HESAPLAMA VE GÖSTERİM
# -------------------------------
# Yalnızca ilk kanal (BGR formatında -> kanal 0 = Mavi) için histogram
histr = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.figure(figsize=(6,4))
plt.title("Orijinal Görüntü Histogramı (Kanal 0)")
plt.xlabel("Piksel Değeri")
plt.ylabel("Frekans")
plt.plot(histr)
plt.show()

# -------------------------------
# HISTOGRAM EŞİTLEME (KONTRAST İYİLEŞTİRME)
# -------------------------------
# Gri tonlamalı görüntü okunur
img_gray = cv2.imread('polen.png', 0)

# Histogram eşitleme uygulanır
equ = cv2.equalizeHist(img_gray)

# Orijinal ve eşitlenmiş görüntülerin histogramları
hist_original = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([equ], [0], None, [256], [0, 256])

# Histogramlar çizilir
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title("Orijinal Histogram")
plt.plot(hist_original)
plt.subplot(1,2,2)
plt.title("Eşitlenmiş Histogram")
plt.plot(hist_equalized)
plt.show()

# Görüntüler yanyana yerleştirilerek karşılaştırma yapılır
res = np.hstack((img_gray, equ))
cv2.imwrite('res.png', res)  # Sonuç dosyaya kaydedilir
