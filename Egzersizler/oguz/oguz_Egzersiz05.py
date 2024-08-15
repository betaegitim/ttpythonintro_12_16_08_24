"""
Bir kullanıcıdan bir sayı girmesini isteyen bir Python programı yazınız. 
Kullanıcı sayı yerine harf veya özel karakter girerse, bir hata mesajı versin.
Program her durumda "Program sona erdi" mesajını ekrana yazdırsın.
"""
def fonk():
    try:
        input1 = input("Sayı Giriniz:")
    say = int(input1)
    if input1.isdigit():
        return(input1)
    else: 
        print("Hatali Giris")
    return