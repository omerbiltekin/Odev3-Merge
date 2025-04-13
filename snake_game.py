import pygame
import time
import random

pygame.init()

# Renkler
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

beyaz = hex_to_rgb("#FFFFFF")
siyah = hex_to_rgb("#000000")
kirmizi = hex_to_rgb("#D32F2F")
yesil  = hex_to_rgb("#66BB6A")
mavi   = hex_to_rgb("#42A5F5")
cim = hex_to_rgb("#A8DF8E") 
yilan_rengi = hex_to_rgb("#2C2C2C") 

# Ekran boyutu
genislik = 600
yukseklik = 400

# Yılan ayarları
yilan_blok = 10
yilan_hizi = 15

font = pygame.font.SysFont("bahnschrift", 25)
font_buyuk = pygame.font.SysFont("comicsansms", 35)

ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Yılan Oyunu - Python")

saat = pygame.time.Clock()

def skor_goster(skor):
    deger = font.render("Skor: " + str(skor), True, beyaz)
    ekran.blit(deger, [0, 0])

def yilan(cizgi, yilan_listesi):
    for x in yilan_listesi:
        pygame.draw.rect(ekran, yilan_rengi, [x[0], x[1], cizgi, cizgi])

def mesaj(msg, renk, y=0):
    metin = font_buyuk.render(msg, True, renk)
    rect = metin.get_rect(center=(genislik / 2, yukseklik / 2 + y))
    ekran.blit(metin, rect)

def baslangic_ekrani():
    bekle = True
    while bekle:
        ekran.fill(beyaz)
        mesaj("YILAN OYUNU", siyah, -50)
        mesaj("Başlamak için SPACE'e bas", mavi, 10)
        mesaj("Çıkmak için Q tuşuna bas", kirmizi, 60)
        pygame.display.update()
        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                pygame.quit()
                quit()
            if etkinlik.type == pygame.KEYDOWN:
                if etkinlik.key == pygame.K_SPACE:
                    bekle = False
                elif etkinlik.key == pygame.K_q:
                    pygame.quit()
                    quit()

def oyun():
    baslangic_ekrani()

    oyun_bitti = False
    oyun_kapandi = False

    x1 = genislik / 2
    y1 = yukseklik / 2

    x1_degisiklik = 0
    y1_degisiklik = 0

    yilan_listesi = []
    yilan_uzunlugu = 1

    yemx = round(random.randrange(0, genislik - yilan_blok) / 10.0) * 10.0
    yemy = round(random.randrange(0, yukseklik - yilan_blok) / 10.0) * 10.0

    while not oyun_bitti:

        while oyun_kapandi:
            ekran.fill(beyaz)
            mesaj("Kaybettin! C - devam, Q - çıkış", kirmizi)
            skor_goster(yilan_uzunlugu - 1)
            pygame.display.update()

            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.KEYDOWN:
                    if etkinlik.key == pygame.K_q:
                        oyun_bitti = True
                        oyun_kapandi = False
                    if etkinlik.key == pygame.K_c:
                        oyun()

        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                oyun_bitti = True
            if etkinlik.type == pygame.KEYDOWN:
                if etkinlik.key == pygame.K_LEFT:
                    x1_degisiklik = -yilan_blok
                    y1_degisiklik = 0
                elif etkinlik.key == pygame.K_RIGHT:
                    x1_degisiklik = yilan_blok
                    y1_degisiklik = 0
                elif etkinlik.key == pygame.K_UP:
                    y1_degisiklik = -yilan_blok
                    x1_degisiklik = 0
                elif etkinlik.key == pygame.K_DOWN:
                    y1_degisiklik = yilan_blok
                    x1_degisiklik = 0

        if x1 >= genislik or x1 < 0 or y1 >= yukseklik or y1 < 0:
            oyun_kapandi = True

        x1 += x1_degisiklik
        y1 += y1_degisiklik
        ekran.fill (cim)
        pygame.draw.rect(ekran, kirmizi, [yemx, yemy, yilan_blok, yilan_blok])
        yilan_kafa = []
        yilan_kafa.append(x1)
        yilan_kafa.append(y1)
        yilan_listesi.append(yilan_kafa)
        if len(yilan_listesi) > yilan_uzunlugu:
            del yilan_listesi[0]

        for x in yilan_listesi[:-1]:
            if x == yilan_kafa:
                oyun_kapandi = True

        yilan(yilan_blok, yilan_listesi)
        skor_goster(yilan_uzunlugu - 1)

        pygame.display.update()

        if x1 == yemx and y1 == yemy:
            yemx = round(random.randrange(0, genislik - yilan_blok) / 10.0) * 10.0
            yemy = round(random.randrange(0, yukseklik - yilan_blok) / 10.0) * 10.0
            yilan_uzunlugu += 1

        saat.tick(yilan_hizi)

    pygame.quit()
    quit()

oyun()
