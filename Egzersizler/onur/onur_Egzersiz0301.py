"""
sayi = input("Sayıyı Giriniz:") # str
if sayi and sayi.isdigit():
    sayi = int(sayi)
    if sayi % 2 == 0:
        print(sayi,"Çift")
    else:
        print(sayi,"Tek")
else:
    print("Giriş Hatası")
##############################

yukarıda yer alan kod örneğini dikkate alarak kullanıcı tarafından girilen yaş bilgisinin 18 den büyük olması halinde
oy kullanabileceğini ekrana yazdıran bir python kodu yazınız.
"""

"""
aci1 = input("1. Açıyı Giriniz:")
aci2 = input("2. Açıyı Giriniz:")
Bir üçgenin iç açılarından yola çıkarak o üçgenin türünü ekrana yazdıran python programını yazalım.
İkizkenar üçgen
Dik üçgen
Eşkenar üçgen
Çeşitkenar üçgen
"""

aci1 = input("1. Açıyı Giriniz:")
aci2 = input("2. Açıyı Giriniz:")
if aci1.isdigit() and aci2.isdigit():
    aci1,aci2 = int(aci1),int(aci2)
    aciList = [180-(aci1+aci2),aci1,aci2]

    if 178 >= aciList[0] > 0:
        print("")
        aciSayisi = len(set(aciList))
        if aciSayisi == 2:
            print("İkizkenar Üçgen")
        elif aciSayisi == 1:
            print("Eşkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
        if 90  in aciList: 
            print("Dik Üçgen")
    else:
        print("Açı Hatası")
else:
    print("Giriş Hatası")

