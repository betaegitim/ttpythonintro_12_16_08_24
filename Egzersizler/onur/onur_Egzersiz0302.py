"""
sayi = input("Sayıyı Giriniz:")
if sayi.isdigit():
    sayi = int(sayi)
    toplam = 0
    for i in range(0,sayi+1):
        # toplam = toplam + i 
        toplam += i
print(toplam)
###################
yukarıda yer alan kaynak koddan faydalanarak girilen sayının faktoriyelini hesaplayan kodu yazalım
"""

sayi = int(input("bir sayı giriniz"))
if sayi < 0 :
    print ("negatif sayının faktoriyeli yoktur")
elif sayi == 0 :
    print("1")
else:
    sonuc = 1
    for i in range (1, sayi +1):
        sonuc *=i
        print(sonuc)