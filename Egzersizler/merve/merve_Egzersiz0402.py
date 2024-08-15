""" 
1. En az 10 karakter uzunluğunda 
2. En az 1 büyük harf
3. En az 1 küçük harf
4. En az 1 rakam
5. En az 1 noktalama işareti
Yukarıda yer alan kurallara uygun şifre üreten python programını yazınız.
"""

# %%
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
# şifre üretirken kullanabileceğimiz koleksiyonlar string kütüphanesinden 
# ortama aktarıldı
def sifreKontrol(password):
    bHarf = kHarf = rakam = noktalama = False
    # password = "sO2:F5<9?1" # çalışmak için örnek şifre
    for item in password: # şifrenin her karakteri için çalışan döngü
        if item.isupper(): #karakter büyük harf mi 
            bHarf = True
        elif item.islower():#karakter küçük harf mi 
            kHarf = True
        elif item.isdigit():# karakter rakam mı
            rakam = True
        elif item in punctuation: # #karakter noktalama işareti mi
            noktalama = True
    return bHarf and kHarf and rakam and noktalama # True ya da False olarak sonuç döner

def sifreUret(uzunluk): # fonksiyon tanımlanıyor. uzunluk şifre uzunluğunu ifade edecek
    import random as rnd
    # random kütüphanesi bizim rastgele seçim yapmamızı sağlayacak
    liste = [ascii_lowercase,ascii_uppercase,digits,punctuation]
    # koleksiyonların rastgele seçilebilmesi için bir liste oluşturduk
    sifre = ""
    while not sifreKontrol(sifre):
        sifre = ""
        # üretilecek sifre için değişken tanımı yapıldı
        for i in range(uzunluk): # uzunluk kadar dönecek bir for döngüsü
            sifre += rnd.choice(rnd.choice(liste)) 
            # önce rastgele koleksiyon seçiliyor
            # ardından bu koleksiyon içinden rastgele üye seçiliyor
            # tüm bu işlemler için iki defa random modülü içerisinde yer alan
            # choice fonksiyonu kullanıldı
    else:
        return sifre
    # şifre dışarıya aktarılıyor



"""

TC Kimlik No Doğrulama Algoritması
TC Kimlik numaraları, her Türk Vatandaşına doğumunda verilen 11 karakterli bir sayıdır ve benzersizdir. 
Yani aynı TC Kimlik numarasından bir tane daha yoktur. Ben önceleri hep bir sıraya göre gittiklerini düşünüyordum. 
Ancak bir gün ailemden iki kişinin TC Kimlik numaraların benzerlik gösterdiğini fark ettim. 
Bu benzerlik ilk 1,2,3 hane ile 7,8,9 hanelerin aynı olmasıydı. 
O gün aslında sıradan gitmediğini belirli bir algoritmaya göre verildiğini anlamıştım.

Şimdi gelelim bu TC No Doğrulama algoritmasına.



TC Kimlik No Doğrulama Algoritması
Bu algoritma 5 adımlı yani 5 şart var. Bu 5 şartın hepsine de uyulması gerekiyor.

1  TC Kimlik Numaraları 11 karakter olmak zorundadır.

2  Her hanesi bir rakam olmaldır.

3  İlk hanesi 0 (sıfır) olamaz

4  1, 3, 5, 7, 9 basamaklarının toplamının 7 katından, 2, 4, 6, 8 basamaklarının toplamını çıkarttığımızda elde ettiğimiz sonucun 10’a bölümünden kalan sayı (MOD10)  10. basamaktaki sayıyı vermelidir.

5  İlk 10 hanenin toplamından elde edilen sonucun 10’a bölümünden kalan sayı (MOD10) 11. basamaktaki sayıyı vermelidir.
"""


tckimlikNo = "10000000146"
