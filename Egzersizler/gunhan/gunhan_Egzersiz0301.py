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

yas = input("yaşınızı giriniz:")
if yas >= 18 :
    print("Oy kullanabilirsiniz")
else:
    print("yaşınız küçük")   