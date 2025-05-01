"""
Bu derste:
- Basit bir görüntü üzerinde Fourier Dönüşümü (DFT)
- Gerçek bir resim üzerinde DFT ve filtreleme işlemleri
- Frekans alanında maskeleme ile filtreleme
uygulanmıştır.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ÖRNEK 1: Yapay Görüntü Üzerinde FFT
# -------------------------------
# Siyah zemin üzerinde beyaz dik çizgi
img = np.zeros((300, 300), np.uint8)
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
img[crow - 15:crow + 15, ccol - 5:ccol + 5] = 1

# Fourier dönüşümü
img_float32 = np.float32(img)
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Görselleştirme
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Orijinal Görüntü'), plt.axis('off')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray'), plt.title('Magnitude Spectrum'), plt.axis('off')
plt.tight_layout()
plt.show()

# ÖRNEK 2: Gerçek Görüntü Üzerinde DFT ve Filtreleme
# -------------------------------
# Görüntü okunur (gri tonlamalı)
img = cv2.imread('kedi1.jpg', 0)
if img is None:
    raise FileNotFoundError("Görüntü dosyası 'kedi1.jpg' bulunamadı.")

img_float32 = np.float32(img)
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Magnitude spectrum görselleştirme
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Frekans uzayında maske (horizontal low-pass)
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 50:crow + 50, :] = 1  # Yatay alanda geçiren

# Maske uygulanır
fshift = dft_shift * mask

# Ters dönüşüm ile görüntü geri elde edilir
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
img_back_norm = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Sonuçları göster
cv2.imshow("Orijinal Görüntü", img)
cv2.imshow("FFT Sonrası Görüntü (Filtreli)", img_back_norm)
cv2.waitKey(0)
cv2.destroyAllWindows()
