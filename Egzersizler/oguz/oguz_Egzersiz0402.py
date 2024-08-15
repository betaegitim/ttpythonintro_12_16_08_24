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
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
# şifre üretirken kullanabileceğimiz koleksiyonlar string kütüphanesinden 
# ortama aktarıldı
def sifreUret(uzunluk): # fonksiyon tanımlanıyor. uzunluk şifre uzunluğunu ifade edecek
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
bHarf = kHarf = rakam = noktalama = False
password = "sO2:F5<9?1" # çalışmak için örnek şifre
for item in password: # şifrenin her karakteri için çalışan döngü
    if item.isupper(): #karakter büyük harf mi 
        bHarf = True
    elif item.islower():#karakter küçük harf mi 
        kHarf = True
    elif item.isdigit():# karakter rakam mı
        rakam = True
    elif item in punctuation: # #karakter noktalama işareti mi
        noktalama = True
    if bHarf and kHarf and rakam and noktalama: # şartların hepsi sağlandı mı
        print("Şifre Uygun")
        break
else: # şartlar sağlanmadan break olmadan döngü bitti mi
    print("Şifre Uygun Değil")
# %%
bHarf = kHarf = rakam = noktalama = False
password = "sO2:F5<9?1"