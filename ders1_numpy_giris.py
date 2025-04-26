import numpy as np
import pandas as pd

my_list = [1,2,3,"merhaba",4.5]
print("Liste: ",my_list)

my_tuple =(10,20,30,"python")
print("Tuple:",my_tuple)

my_dict ={"ad ":"tuba","yas":25,"meslek":"muhendis"}
print("Sözlük:",my_dict)

my_set ={1,2,3,3,4,4}
print("Küme:",my_set)

for i in range(5):
  print(f"Döngü iterasyonu {i}")
if 10 > 5:
  print("10 , 5'ten büyüktür")
if 5 > 10:
  print("5 , 10'dan büyüktür")
else:
  print("5 , 10'dan büyük değildir")

with open ("veri.txt","w") as dosya:
  dosya.write("merhaba Python!")

with open("veri.txt","r") as dosya:
  icerik = dosya.read()
  print(icerik)

liste = [1,2,3,4,5]
dizi =np.array(liste)
print("numpy Dizisi:",dizi)

dizi[2]

print("dizinin Tipi:",type(dizi))
print("Dizinin Boyutu: ",dizi.shape)
print("Dizinin veri tipi: ",dizi.dtype)
print("Dizinin Boyutu: ",dizi.size)
print("dizinin bellekte kapladığı alan(byte)",dizi.nbytes)

float_dizi = np.array([1.2,3.4,4.8])
print("float tipinde dizi: ",float_dizi)

matris =np.array([[1,2,3,],[4,5,6]])
print("2d\n",matris)
print("matrisin boyutu",matris.shape)

sifir_dizi = np.zeros((3,3))
bir_dizi = np.ones((2,2))
rastgele_dizi = np.random.rand(3,3)
print("sifir matrisi\n",sifir_dizi)
print("bir matrisi\n",bir_dizi)
print("rastgele matrisi\n",rastgele_dizi)

A=np.array([1,2,3])
B=np.array([10,20,30])

print("toplam",A+B)
print("fark",A-B)
print("carpim",A*B)
print("bolum",A/B)

C = np.array([10,20,30,40,50,60])
print("ilk 3 eleman: ",C[:3])
print("son 3 eleman: ",C[-3:])
print("ortadaki 3 eleman: ",C[2:5])

dizi =np.array([10,20,30,40,50])
print("dizinin ortalamsı:",np.mean(dizi))
print("dizinin standart sapması:",np.std(dizi))
print("dizinin Maksimum degeri:",np.max(dizi))
print("dizinin Minumum degeri:",np.min(dizi))

data = {
    "Ad":["Ali","Ayşe","Veli","Zeynep"],
    "Yas":[25,30,24,16],
    "Sehir":["Ankara","Adana","istanbul","bolu"]
}

dizi =np.array([[1,2,3,],[4,5,6,]])
df_dizi=pd.DataFrame(dizi,columns=["sütun1","sütun2","sütun3"])
print("df_dizi",df_dizi)

dizi_geri = df_dizi.to_numpy()
print("pandastan numpy",dizi_geri)

sifirmt = np.zeros((500,500))
sifirmt[51][1]

size=500
pix=50
uf=np.zeros((size,size))
for j in range(pix,size,2*pix):
  for i in range(j,j+pix):
    uf[i][i:size-i]=1
    uf[i+1:size-(i+1), i] = 1
    uf[i+1:size-(i+1), size-(i+1)] = 1
    uf[size-(i+1)][i:size-i]=1

print(uf)

# Derste istenen: 500x500 boyutta iç içe siyah-beyaz kareler oluşturmak

import numpy as np
import matplotlib.pyplot as plt

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

print(uf)

plt.figure(figsize=(8, 8))
plt.imshow(uf, cmap='gray', interpolation='nearest')  # Gri renk skalasında göster
plt.axis('off')  # Eksenleri kapat
plt.show()
