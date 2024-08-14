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

if (aci1==aci2):
    print("İkizkenar üçgen")
elif(aci1 == aci2) and ((aci1+aci2)==90):
    print("İkizkenar Dik Üçgen")
elif (aci1==aci2==60):
    print("Eşkenar Üçgen")