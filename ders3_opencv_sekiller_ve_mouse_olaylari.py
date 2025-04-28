# Gerekli kütüphaneleri import edelim
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Görsel okuma ve gösterme
img = cv2.imread('00-puppy.jpg')
plt.imshow(img)
plt.title("Orijinal BGR Görsel")
plt.axis('off')
plt.show()

# BGR'dan RGB'ye dönüştürme ve tekrar gösterme
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
plt.title("RGB Formatlı Görsel")
plt.axis('off')
plt.show()

# Boş bir görsel (siyah ekran) oluşturma
blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)
plt.imshow(blank_img)
plt.title("Boş Görsel")
plt.axis('off')
plt.show()

# Dikdörtgen çizme
cv2.rectangle(blank_img, pt1=(384,10), pt2=(510,150), color=(255,0,0), thickness=-1)
plt.imshow(blank_img)
plt.title("Dikdörtgen Çizildi")
plt.axis('off')
plt.show()

# Daire çizme
cv2.circle(img=blank_img, center=(100,100), radius=50, color=(255,0,0), thickness=-1)
plt.imshow(blank_img)
plt.title("Daire Çizildi")
plt.axis('off')
plt.show()

# Birden fazla daire çizimi
cv2.circle(img=blank_img, center=(100,250), radius=50, color=(80,80,80), thickness=10)
cv2.circle(img=blank_img, center=(170,250), radius=50, color=(80,80,80), thickness=10)
cv2.circle(img=blank_img, center=(240,250), radius=50, color=(80,80,80), thickness=10)
cv2.circle(img=blank_img, center=(310,250), radius=50, color=(80,80,80), thickness=10)
plt.imshow(blank_img)
plt.title("Çoklu Daireler")
plt.axis('off')
plt.show()

# Çizgi çizme
cv2.line(blank_img, pt1=(0,0), pt2=(512,512), color=(10,255,255), thickness=8)
plt.imshow(blank_img)
plt.title("Çizgi Çizildi")
plt.axis('off')
plt.show()

# --- Ekranı temizleyip yeniden başlamak için boş bir görsel oluşturuyoruz ---
blank_img = np.zeros(shape=(512,512,3), dtype=np.int16)
plt.imshow(blank_img)
plt.title("Temizlenmiş Boş Görsel")
plt.axis('off')
plt.show()

# Metin yazdırma
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img, text='Mesaj', org=(80,400), fontFace=font, fontScale=3, color=(80,80,80), thickness=10, lineType=cv2.LINE_AA)
plt.imshow(blank_img)
plt.title("Görsele Metin Yazıldı")
plt.axis('off')
plt.show()

# Yeni bir görsel okuma ve üzerine çizim yapma
img = cv2.imread('dog_backpack.png')
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
plt.title("Yeni Okunan Görsel")
plt.axis('off')
plt.show()

# Görsel üzerine daire çizme
cv2.circle(img=fix_img, center=(400,550), radius=250, color=(255,0,0), thickness=10)
plt.imshow(fix_img)
plt.title("Görsele Daire Çizildi")
plt.axis('off')
plt.show()

# --- Mouse ile çizim yapmak ---
# Boş bir canvas oluşturuluyor
img = np.zeros((512, 512, 3), dtype=np.uint8)

# Çizim modları
drawing = False  # Sağ tık ile çizim modu
ix, iy = -1, -1  # Başlangıç noktası

# Mouse olaylarını yönetecek fonksiyon
def draw_shape(event, x, y, flags, param):
    global drawing, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:  # Sol tıkla daire çiz
        cv2.circle(img, (x, y), 50, (0, 255, 0), 10)
    elif event == cv2.EVENT_RBUTTONDOWN:  # Sağ tıkla çizime başla
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:  # Sağ tıkla sürüklerken geçici dikdörtgen göster
        if drawing:
            temp_img = img.copy()
            cv2.rectangle(temp_img, (ix, iy), (x, y), (255, 0, 0), -1)
            cv2.imshow('My_Drawing', temp_img)
    elif event == cv2.EVENT_RBUTTONUP:  # Sağ tıkı bırakınca dikdörtgeni sabitle
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)

# Pencereyi oluştur ve mouse callback'ini ayarla
cv2.namedWindow('My_Drawing')
cv2.setMouseCallback('My_Drawing', draw_shape)

# Sonsuz döngüyle pencereyi sürekli göster
while True:
    cv2.imshow('My_Drawing', img)
    if cv2.waitKey(20) & 0xFF == 27:  # ESC tuşuna basılırsa çık
        break

# Pencereleri kapat
cv2.destroyAllWindows()
