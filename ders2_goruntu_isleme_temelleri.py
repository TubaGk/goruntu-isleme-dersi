# Ders 2: Görüntü İşleme Temelleri

from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1. Görüntüyü oku ve RGB kanallarını ayır
im = np.array(Image.open('/content/indir.jpeg'))
red_channel = im[:, :, 0]
green_channel = im[:, :, 1]
blue_channel = im[:, :, 2]

# 2. Renk kanallarını ayrı ayrı göster
plt.figure(figsize=(10, 7))

plt.subplot(1, 3, 1)
plt.imshow(red_channel, cmap='gray')
plt.title("Kırmızı Kanal")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(green_channel, cmap='gray')
plt.title("Yeşil Kanal")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(blue_channel, cmap='gray')
plt.title("Mavi Kanal")
plt.axis('off')

plt.savefig('image.jpg')  # RGB kanallarının gösterildiği görüntüyü kaydet
plt.show()

# 3. Kaydedilen görüntüyü gri tonlamalı (grayscale) olarak oku
im_gray = cv2.imread('/content/image.jpg', cv2.IMREAD_GRAYSCALE)

# 4. Threshold (eşikleme) işlemi ile ikili (binary) görüntü oluştur
threshold_value = 110
im_bw = cv2.threshold(im_gray, threshold_value, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('image_binary.png', im_bw)

# 5. Parlaklık aralığına göre intensity slicing işlemi
img = cv2.imread('/content/indir.jpeg', 0)  # Gri tonlamalı oku
row, column = img.shape
img_sliced = np.zeros((row, column), dtype='uint8')

min_range = 60
max_range = 100

for i in range(row):
    for j in range(column):
        if min_range < img[i, j] < max_range:
            img_sliced[i, j] = 255  # Belirli aralıktakileri beyaz yap
        else:
            img_sliced[i, j] = img[i-1, j-1]  # Diğerlerini bir önceki pikselin değeriyle doldur

cv2.imwrite('original_gray.jpg', img)
cv2.imwrite('sliced_image.jpg', img_sliced)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. İki farklı görüntüde kanal değiştirip, birleştirme işlemi
img1 = cv2.imread('/content/kedi1.jpg')
img2 = cv2.imread('/content/kedi2.jpg')

# Görüntüleri aynı boyuta getir
img1 = cv2.resize(img1, (100, 200))
img2 = cv2.resize(img2, (100, 200))

# img1'de mavi kanalı sıfırla
img1[:, :, 0] = 0

# img2'de kırmızı kanalı sıfırla
img2[:, :, 2] = 0

# İki görüntüyü topla
total_image = cv2.add(img1, img2)

# Sonuçları göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("Kırmızı Kanal Kapalı")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("Mavi Kanal Kapalı")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(total_image, cv2.COLOR_BGR2RGB))
plt.title("Toplanmış Görüntü")
plt.axis("off")

plt.show()
