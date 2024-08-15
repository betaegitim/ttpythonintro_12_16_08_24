"""
Bir kullanıcıdan bir sayı girmesini isteyen bir Python programı yazınız. 
Kullanıcı sayı yerine harf veya özel karakter girerse, bir hata mesajı versin.
Program her durumda "Program sona erdi" mesajını ekrana yazdırsın.
"""

sayi = input("Lütfen bir sayı giriniz")
try:
    sayi = int(sayi)
except ValueError:
    print("Lütfen sadece sayı giriniz")
