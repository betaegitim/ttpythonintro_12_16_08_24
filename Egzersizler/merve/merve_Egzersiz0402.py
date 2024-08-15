""" 
1. En az 10 karakter uzunluğunda 
2. En az 1 büyük harf
3. En az 1 küçük harf
4. En az 1 rakam
5. En az 1 noktalam işareti
Yukarıda yer alan kurallara uygun şifre üreten python programını yazınız.
"""

from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import random as rnd
liste=[ascii_lowercase,ascii_uppercase,digits,punctuation]
# secilmis = rnd.choice
rnd.choice(rnd.choice(liste))
sifre=""
for i in range(10):
    sifre += rnd.choice(rnd.choice(liste))
print(sifre)


def sifreUret(uzunluk):
    from string import ascii_lowercase,ascii_uppercase,digits,punctuation
    import random as rnd
    liste = [ascii_lowercase,ascii_uppercase,digits,punctuation]
    sifre = ""
    for i in range(uzunluk):
        sifre += rnd.choice(rnd.choice(liste))
    return sifre
sifreUret(10)

bHarf = kHarf = rakam = noktalama = False
password= "s02:F5<9?1"
for item in password:
    if item.isupper():
        bHarf=True
    elif item.islower():
        kHarf=True
    elif item.isdigit():
        rakam=True
    elif item in punctuation:
        noktalama=True
    if bHarf and kHarf and rakam and noktalama:
        print("Şifre Uygun")
        break
else:
    print("Şifre Uygun Değil")

bHarf = kHarf = rakam = noktalama = False
password = "sO2:F5<9?1"
indis = 0
while not (bHarf and kHarf and rakam and noktalama) and len(password) > indis:
    item = password[indis]
    if item.isupper():
        bHarf=True
    elif = 


