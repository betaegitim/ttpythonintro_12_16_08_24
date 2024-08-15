# %% [markdown]
# # Fonksiyonlar 2
# * lambda
# * global,nonlocal
# * gömülü fonksiyonlar

# %% [markdown]
# ## Lambda

# %%
def fonk(a,b):
    return a+b
fonk(2,3)

# %%
fonk = lambda a,b : a+b
fonk(2,3)

# %%
liste = [1,2,3,4,5,6,7]
fonk = lambda x:x.strip().replace(".com","")

# %% [markdown]
# ## global
# 

# %%
a = 4
def testFonk():
    a = 3
    print("Fonk içerisindeki a=",a)
print("1-Dışarıdaki a=",a) # 4
testFonk() # 3
print("2-Dışarıdaki a=",a) # 4

# %%
a = 4
def testFonk():
    global a
    a = 3
    print("Fonk içerisindeki a=",a)
print("1-Dışarıdaki a=",a) # 4
testFonk() # 3
print("2-Dışarıdaki a=",a) # 3

# %% [markdown]
# ## nonlocal

# %%
a = 4
def testFonk():
    global a
    a = 3
    print("Fonk içerisindeki a=",a)
    def icFonk():
        a = 8
        print("İç fonksiyondan a=",a)
    icFonk()
print("1-Dışarıdaki a=",a) # 4
testFonk() # 3
print("2-Dışarıdaki a=",a) # 3

# %%
a = 4
def testFonk():
    a = 3
    print("1-Fonk içerisindeki a=",a)
    def icFonk():
        global a
        a = 8
        print("İç fonksiyondan a=",a)
    icFonk()
    print("2-Fonk içerisindeki a=",a)
print("1-Dışarıdaki a=",a) # 4
testFonk() # 3
print("2-Dışarıdaki a=",a) # 3

# %%
a = 4
def testFonk():
    a = 3 # nonlocal
    print("1-Fonk içerisindeki a=",a)
    def icFonk():
        nonlocal a
        a = 8
        print("İç fonksiyondan a=",a)
    icFonk()
    print("2-Fonk içerisindeki a=",a)
print("1-Dışarıdaki a=",a) # 4
testFonk() # 3
print("2-Dışarıdaki a=",a) # 3

# %% [markdown]
# ## gömülü fonksiyonlar
# * map
# * zip
# * filter
# * reduce
# * sorted
# * all,any

# %%
# map
liste = [1,2,3,4,5,6]
def fonk(x):
    return x**2
print(map(fonk,liste))

# %%
liste = [1,2,3,4,5,6]
def fonk(x):
    return x**2
print(*map(fonk,liste))
print(list(map(fonk,liste)))

# %%
liste = [1,2,3,4,5,6]
list(map(lambda x:x%2==0,liste))

# %%
liste = [1,2,3,4,5,6]
list(map(lambda x:x**2,liste))

# %%
# zip
l1 = ["a","b","c","d"]
l2 = [10,20,40,60]
zip(l1,l2)

# %%
l1 = ["a","b","c","d"]
l2 = [10,20,40,60]
list(zip(l1,l2))

# %%
l1 = ["a","b","c","d"]
l2 = [10,20,40,60,50]
list(zip(l1,l2,strict=True))

# %%
liste = [1,2,2,1,1,1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,3,1,1,1,1,1,2,2,2,1,1,1,1,1,2,2,2,1,1,1]
filter(lambda x:x==3,liste)

# %%
liste = [1,2,2,1,1,1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,3,1,1,1,1,1,2,2,2,1,1,1,1,1,2,2,2,1,1,1]
list(filter(lambda x:x==3,liste))

# %%
if len(list(filter(lambda x:x==3,liste))):
    print(liste.index(3))

# %%
from functools import reduce
import operator 
liste = [1,2,3,4,5]
reduce(operator.add,liste)

# %%
liste = ["çiğdem","şermin","sevgi","ceren","ali","ibrahim","özge","göktuğ","hakan","zeynep"]
liste.sort()
liste

# %%
ord("ş"),ord("s"),ord("z")

# %%
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {x:alfabe.index(x) for x in alfabe}
cevrim

# %%
sorted(liste,key=lambda a:cevrim.get(a[0]))

# %%
# -*- coding: utf-8 -*-

# %%
liste = ["çiğdem","şermin","sevgi","ceren","ali","ibrahim","özge","göktuğ","hakan","zeynep"]

# %%
liste.sort()
liste

# %%
liste = [0,0,0,0,0,0,0,1,0,0,0]
any(liste)

# %%
liste = [0,0,0,0,0,0,0,1,0,0,0]
all(liste)

# %%
liste = [1,1,1,1,1,1,1,1,1,1]
all(liste)

# %% [markdown]
# #### Tüm Kod

# %%
liste = ["çiğdem","şermin","sevgi","ceren","ali","ibrahim","özge","göktuğ","hakan","zeynep"]
liste.sort()
liste

# %%
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {x:alfabe.index(x) for x in alfabe}
sorted(liste,key=lambda a:cevrim.get(a[0])) # 0 2 7

# %% [markdown]
# ## Egzersiz
# 1. Password Policy Control
# 2. T.C. Kimlik Kontrol
# 3. IBAN Kontrol

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
password = "sO2F591"
indis = 0
while not (bHarf and kHarf and rakam and noktalama) and  len(password) > indis:
    item = password[indis]
    if item.isupper(): #karakter büyük harf mi 
        bHarf = True
    elif item.islower():#karakter küçük harf mi 
        kHarf = True
    elif item.isdigit():# karakter rakam mı
        rakam = True
    elif item in punctuation: # #karakter noktalama işareti mi
        noktalama = True
    indis+=1
else:
    if bHarf and kHarf and rakam and noktalama: # şartların hepsi sağlandı mı
        print("Şifre Uygun")
    else:
        # şartlar sağlanmadan break olmadan döngü bitti mi
        print("Şifre Uygun Değil")
# %%
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
sifreKontrol("sO2F591")
# %%
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
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

def sifreUret(uzunluk): 
    import random as rnd
    liste = [ascii_lowercase,ascii_uppercase,digits,punctuation]
    sifre = ""
    while not sifreKontrol(sifre): 
        sifre = ""
        # üretilecek sifre için değişken tanımı yapıldı
        for i in range(uzunluk): # uzunluk kadar dönecek bir for döngüsü
            sifre += rnd.choice(rnd.choice(liste)) 
    else:
        return sifre
    # şifre dışarıya aktarılıyor
sifreUret(4)
# %% [markdown]
"""
TC Kimlik No Doğrulama Algoritması
Bu algoritma 5 adımlı yani 5 şart var. Bu 5 şartın hepsine de uyulması gerekiyor.

1  TC Kimlik Numaraları 11 karakter olmak zorundadır.

2  Her hanesi bir rakam olmaldır.

3  İlk hanesi 0 (sıfır) olamaz

4  1, 3, 5, 7, 9 basamaklarının toplamının 7 katından, 
2, 4, 6, 8 basamaklarının toplamını çıkarttığımızda elde ettiğimiz sonucun 
10’a bölümünden kalan sayı (MOD10)  10. basamaktaki sayıyı vermelidir.

5  İlk 10 hanenin toplamından elde edilen sonucun 10’a bölümünden kalan sayı (MOD10) 11. basamaktaki sayıyı vermelidir.
"""
# %%
# tckimlikNo = input("T.C. Kimlik Numaranızı Giriniz:")
tckimlikNo = "10000000146"

if len(tckimlikNo) == 11:
    if tckimlikNo.isdigit():
        tcList = list(map(int,tckimlikNo))
        if tcList[0] != 0:
            # 1 3 5 7 9 => 0 2 4 6 8 => range(0,9,2) => 0 2 4 6 8
            sayi1List = [tcList[i] for i in range(0,9,2)]
            sayi2List = [tcList[i] for i in range(1,8,2)]
            if (sum(sayi1List)*7 - sum(sayi2List))%10 == tcList[9]:
                sayiList = [tcList[i] for i in range(10)]
                if sum(sayiList) % 10 == tcList[10]:
                    print("Doğru")
                else:
                    print("Hata 5")
            else:
                print("Hata 4")
        else:
            print("Hata 3")
    else:
        print("Hata 2")
else:
    print("Hata 1")

# %%
# tckimlikNo = input("T.C. Kimlik Numaranızı Giriniz:")
tckimlikNo = "10000000146"
def tcKimlikKontrol(tckimlikNo:str)->bool:
    if len(tckimlikNo) == 11:
        if tckimlikNo.isdigit():
            tcList = list(map(int,tckimlikNo))
            if tcList[0] != 0:
                # 1 3 5 7 9 => 0 2 4 6 8 => range(0,9,2) => 0 2 4 6 8
                sayi1List = [tcList[i] for i in range(0,9,2)]
                sayi2List = [tcList[i] for i in range(1,8,2)]
                if (sum(sayi1List)*7 - sum(sayi2List))%10 == tcList[9]:
                    sayiList = [tcList[i] for i in range(10)]
                    if sum(sayiList) % 10 == tcList[10]:
                        return True
    return False
tcKimlikKontrol(tckimlikNo)
# %%
def tcKimlikKontrol(tckimlikNo:str)->bool:
    if len(tckimlikNo) == 11:
        if tckimlikNo.isdigit():
            tcList = list(map(int,tckimlikNo))
            if tcList[0] != 0:
                # 1 3 5 7 9 => 0 2 4 6 8 => range(0,9,2) => 0 2 4 6 8
                sayi1List = [tcList[i] for i in range(0,9,2)]
                sayi2List = [tcList[i] for i in range(1,8,2)]
                if (sum(sayi1List)*7 - sum(sayi2List))%10 == tcList[9]:
                    sayiList = [tcList[i] for i in range(10)]
                    if sum(sayiList) % 10 == tcList[10]:
                        return True
    return False
tckimlikNo = input("T.C. Kimlik Numaranızı Giriniz:")
tcKimlikKontrol(tckimlikNo)
# %%
