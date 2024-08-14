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
    carpim=1
    for i in range(sayi):
        carpim*=i+1
     
print(carpim)   
