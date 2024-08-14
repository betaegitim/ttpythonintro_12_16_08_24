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

sayi = input("Sayıyı Giriniz:")
if sayi.isdigit():
    sayi = int(sayi)
    if sayi >= 0:
        faktoryel = 1
        for i in range(1,sayi+1): 
        faktoryel *= i
    print(faktoryel)