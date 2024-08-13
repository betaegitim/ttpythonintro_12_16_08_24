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

sayi = input("Yaşınızı Giriniz:") # str
if sayi and sayi.isdigit():
    sayi = int(sayi)
    if sayi >=18 :
        print(sayi,"Oy Kullanabilir")
    else:
        print(sayi,"Oy Kullanamaz")
else:
    print("Giriş Hatası")