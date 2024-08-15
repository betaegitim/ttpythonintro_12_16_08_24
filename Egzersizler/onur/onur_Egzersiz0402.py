""" 
1. En az 10 karakter uzunluğunda 
2. En az 1 büyük harf
3. En az 1 küçük harf
4. En az 1 rakam
5. En az 1 noktalam işareti
Yukarıda yer alan kurallara uygun şifre üreten python programını yazınız.
"""

# %%
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import random as rnd
liste = [ascii_lowercase,ascii_uppercase,digits,punctuation]
# secilmis = rnd.choice(liste)
sifre = ""
for i in range(10):
    sifre += rnd.choice(rnd.choice(liste))
print(sifre)

# %%
def sifreUret(uzunluk): # fonksiyon tanımlanıyor. uzunluk şifre uzunluğunu ifade edecek
    from string import ascii_lowercase,ascii_uppercase,digits,punctuation
    # şifre üretirken kullanabileceğimiz koleksiyonlar string kütüphanesinden 
    # dosyaya aktarıldı
    import random as rnd
    # random kütüphanesi bizim rastgele seçim yapmamızı sağlayacak
    liste = [ascii_lowercase,ascii_uppercase,digits,punctuation]
    # koleksiyonların rastgele seçilebilmesi için bir liste oluşturduk
    sifre = ""
    # üretilecek sifre için değişken tanımı yapıldı
    for i in range(uzunluk): # uzunluk kadar dönecek bir for döngüsü
        sifre += rnd.choice(rnd.choice(liste)) 
        # önce rastgele koleksiyon seçiliyor
        # ardından bu koleksiyon içinden rastgele üye seçiliyor
        # tüm bu işlemler için iki defa random modülü içerisinde yer alan
        # choice fonksiyonu kullanıldı
    return sifre
    # şifre dışarıya aktarılıyor
sifreUret(10)
# %%