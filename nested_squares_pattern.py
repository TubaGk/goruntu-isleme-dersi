# ODEV_1 - 500x500 matrisde iç içe kare görünümü
import numpy as np
import matplotlib.pyplot as plt

# Boyut ve piksel değeri
size = 500
pix = 50
uf = np.zeros((size, size))

# İç içe kareler çiziliyor
for j in range(pix, size, 2 * pix):
    for i in range(j, min(j + pix, size)):
        if i < size - 1:
            uf[i, i:size-i] = 1
            uf[i+1:size-(i+1), i] = 1
            uf[i+1:size-(i+1), size-(i+1)] = 1
            uf[size-(i+1), i:size-i] = 1

# Görselleştirme
plt.figure(figsize=(5, 5))
plt.imshow(uf, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.show(block=False)
plt.pause(0.001)
