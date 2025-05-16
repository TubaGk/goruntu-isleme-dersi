# ODEV_2 - Resimde mouse ile seçilen alanın boyanması
import cv2
import numpy as np

# RGB'yi BGR'ye çevirme fonksiyonu
def rgb_to_bgr(rgb):
    r, g, b = rgb
    return (b, g, r)

# Görseli okuma
img = cv2.imread('ornek.jpg')
clone = img.copy()

drawing = False
ix, iy = -1, -1

# Çizim fonksiyonu
def draw(event, x, y, flags, param):
    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img = clone.copy()
            center_x = (ix + x) // 2
            center_y = (iy + y) // 2
            radius = int(((x - ix)**2 + (y - iy)**2)**0.5 / 2)

            cv2.circle(img, (center_x, center_y), radius, rgb_to_bgr((244, 222, 173)), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        center_x = (ix + x) // 2
        center_y = (iy + y) // 2
        radius = int(((x - ix)**2 + (y - iy)**2)**0.5 / 2)

        cv2.circle(clone, (center_x, center_y), radius, rgb_to_bgr((244, 222, 173)), -1)

# Pencereyi oluşturma ve mouse callback ayarı
cv2.namedWindow('Resim')
cv2.setMouseCallback('Resim', draw)

# Sonsuz döngü ile resim gösterme
while True:
    cv2.imshow('Resim', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
