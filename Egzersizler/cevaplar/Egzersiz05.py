"""
Bir kullanıcıdan bir sayı girmesini isteyen bir Python programı yazınız. 
Kullanıcı sayı yerine harf veya özel karakter girerse, bir hata mesajı versin.
Program her durumda "Program sona erdi" mesajını ekrana yazdırsın.
"""
def fonk():
    try:
        sayi = int(input("Sayı Giriniz: "))
    except ValueError:
        print("Değer Hatası")
    finally:
        print("Program Sona Erdi.")
fonk()
