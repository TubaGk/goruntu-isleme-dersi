# Gerekli kütüphaneler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Liste, Tuple, Sözlük ve Küme
my_list = [1, 2, 3, "merhaba", 4.5]
print("Liste:", my_list)

my_tuple = (10, 20, 30, "python")
print("Tuple:", my_tuple)

my_dict = {"ad": "tuba", "yas": 25, "meslek": "mühendis"}
print("Sözlük:", my_dict)

my_set = {1, 2, 3, 3, 4, 4}
print("Küme:", my_set)

# Döngü ve Koşul
for i in range(5):
    print(f"Döngü iterasyonu {i}")

if 10 > 5:
    print("10, 5'ten büyüktür")

if 5 > 10:
    print("5, 10'dan büyüktür")
else:
    print("5, 10'dan büyük değildir")

# Dosya işlemleri
with open("veri.txt", "w") as dosya:
    dosya.write("merhaba Python!")

with open("veri.txt", "r") as dosya:
    icerik = dosya.read()
    print(icerik)

# NumPy ile temel işlemler
liste = [1, 2, 3, 4, 5]
dizi = np.array(liste)

print("NumPy Dizisi:", dizi)
print("Dizinin Tipi:", type(dizi))
print("Dizinin Boyutu:", dizi.shape)
print("Dizinin Veri Tipi:", dizi.dtype)
print("Dizinin Eleman Sayısı:", dizi.size)
print("Dizinin Bellekte Kapladığı Alan (byte):", dizi.nbytes)

# Farklı veri tipiyle NumPy dizisi
float_dizi = np.array([1.2, 3.4, 4.8])
print("Float Tipinde Dizi:", float_dizi)

# 2D Matris
matris = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Matris:\n", matris)
print("Matrisin Boyutu:", matris.shape)

# Özel matrisler
sifir_dizi = np.zeros((3, 3))
bir_dizi = np.ones((2, 2))
rastgele_dizi = np.random.rand(3, 3)

print("Sıfır Matrisi:\n", sifir_dizi)
print("Bir Matrisi:\n", bir_dizi)
print("Rastgele Matrisi:\n", rastgele_dizi)

# Aritmetik işlemler
A = np.array([1, 2, 3])
B = np.array([10, 20, 30])

print("Toplam:", A + B)
print("Fark:", A - B)
print("Çarpım:", A * B)
print("Bölüm:", A / B)

# Dizi Dilimleme
C = np.array([10, 20, 30, 40, 50, 60])
print("İlk 3 Eleman:", C[:3])
print("Son 3 Eleman:", C[-3:])
print("Ortadaki 3 Eleman:", C[2:5])

# İstatistiksel Hesaplamalar
dizi = np.array([10, 20, 30, 40, 50])
print("Dizinin Ortalaması:", np.mean(dizi))
print("Dizinin Standart Sapması:", np.std(dizi))
print("Dizinin Maksimum Değeri:", np.max(dizi))
print("Dizinin Minimum Değeri:", np.min(dizi))

# NumPy ile Pandas Veri Çerçevesi
dizi = np.array([[1, 2, 3], [4, 5, 6]])
df_dizi = pd.DataFrame(dizi, columns=["Sütun1", "Sütun2", "Sütun3"])
print("DataFrame:\n", df_dizi)

# DataFrame'den tekrar NumPy dizisine dönüşüm
dizi_geri = df_dizi.to_numpy()
print("Pandas'tan NumPy'a Dönüşüm:\n", dizi_geri)

# İçiçe Siyah-Beyaz Kareler Oluşturma (Manuel Yöntem)
size = 500
pix = 50
uf = np.zeros((size, size))

for j in range(pix, size, 2 * pix):
    for i in range(j, min(j + pix, size)):
        if i < size - 1:
            uf[i, i:size-i] = 1
            uf[i+1:size-(i+1), i] = 1
            uf[i+1:size-(i+1), size-(i+1)] = 1
            uf[size-(i+1), i:size-i] = 1

# Matris çıktısı
print(uf)

# Görselleştirme
plt.figure(figsize=(8, 8))
plt.imshow(uf, cmap='gray', interpolation='nearest')
plt.axis('off')  # Eksenleri kapatma
plt.title("İçiçe Siyah-Beyaz Kareler")
plt.show()
