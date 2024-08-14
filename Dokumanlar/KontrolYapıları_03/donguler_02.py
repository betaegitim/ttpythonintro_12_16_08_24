# %% [markdown]
# # Döngüler
# * range
# * for
# * while
# * break
# * continue
# * else

# %%
print(*[1,2,3,4],*"Türk")

# %% [markdown]
# ## range
# ```
# range(baslangic=0,bitis-1,adim=1)
# ```

# %%
range(1,4)

# %%
print(*range(1,4))

# %%
# 2 den 10 a kadar bir sayac için
print(*range(2,10))

# %%
# 5 ten 50 ye kadar 10 adımlı  bir sayac için
print(*range(5,50,5))

# %%
print(*range(0,10))
print(*range(10))

# %%
print(*range(20,10,-2))

# %% [markdown]
# ## for

# %%
for i in range(5):
    print(i)

# %%
metin = "BETA"
#        0123
for i in range(len(metin)):
    print(i,"=>",metin[i])

# %%
#foreach obj in objects
metin = "BETA"
for item in metin:
    print(item)

# %%
liste = [1,2,3,4]
for item in liste:
    print(item**2)

# %%
demet = 1,2,3,4,5
for item in demet:
    print(item**2)

# %%
sozluk = {
    "1":"Bir",
    "2":"İki"
}
for item in sozluk:
    print(item)

# %%
sozluk.items()

# %%
key,value = ('1', 'Bir')
print(key,value)

# %%
sozluk = {
    "1":"Bir",
    "2":"İki"
}
for key,value in sozluk.items():
    print(key,":",value)


# %%
a,b,c,d,e,f,g = "0101101"
print(a,b,c,d,e,f,g)

# %% [markdown]
# Örnek Soru:
# Girilen sayıya kadar asal sayıları listeleyen python programını yazınız

# %%
sayi = input("Sayıyı Giriniz:")
if sayi.isdigit():
    sayi = int(sayi)
    for i in range(2,sayi+1):
        # asal kontrol
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
    

# %% [markdown]
# ##### fibanocci serisi sorusu

# %%
a = 1
b = 1
print(a,b)
c = a + b
print(c)
a = b
b = c
c = a + b
print(c)
a = b
b = c
c = a + b
print(c)
a = b
b = c
c = a + b
print(c)

# %%
a = b = 1
print(a+b)
a,b = b,(a+b)
print(a+b)
a,b = b,(a+b)
print(a+b)
a,b = b,(a+b)
print(a+b)
a,b = b,(a+b)
print(a+b)
a,b = b,(a+b)

# %%
a = b = 1
print(a,b,sep="\n")
for i in range(20):
    print(a+b,a/b)
    a,b = b,(a+b)

# %%
sayi = input("Sayıyı Giriniz:")
if sayi.isdigit():
    sayi = int(sayi)
    toplam = 0
    for i in range(0,sayi+1):
        # toplam = toplam + i 
        toplam += i
print(toplam)

# %% [markdown]
# ## while

# %%
for i in range(5):
    print(i,end="-")

# %%
adim = 0
while adim < 5:
    print(adim,end="-")
    adim += 1


# %%
while giris := input("Giriş Yapınız") != "ç":
    print("Devam Ediyor")

# %%
giris = ""
while giris != "ç":
    giris = input("Giriş Yapınız":)
    print("Devam Ediyor")

# %% [markdown]
# ## break

# %%
adim = 0
while adim < 10:
    print(adim,end="-")
    adim += 1
    if adim == 4:
        break


# %%
for i in range(10):
    if i == 4:
        break
    print(i,end="-")
    

# %% [markdown]
# ## continue

# %%
adim = 0
while adim < 10:
    adim += 1
    if adim == 4:
        continue
    print(adim,end="-")
    print("-----")

# %%
for i in range(10):
    if i == 4:
        continue
    print(i,end="-")

# %% [markdown]
# ## else

# %%
liste = [1,2,3,4]
for item in liste:
    print(item)
else:
    print("Liste Bitti")

# %%
adim = 0
while adim < 10:
    print(adim,end="-")
    adim += 1
    if adim == 4:
        break #-------------- ELSE break ile birlikte çalışmaz
else:
    print("Döngü Bitti")

# %%
adim = 0
while adim < 10:
    print(adim,end="-")
    adim += 1
    if adim == 4:
        continue 
else:
    print("Döngü Bitti")

# %% [markdown]
# Bir metin içerisindeki büyük listesini yazdıran python programını yazınız.

# %%
metin = input("Giriş Yapınız:")
sayac = 0
for item in metin:
    if item.isupper():
        #### 
        sayac += 1
else:
    print(f"{metin} içerisinde {sayac} adet büyük harf vardır.")

# %% [markdown]
# ## Kolay Yazımlar

# %%
a = 5
sonuc = "Çift" if a % 2 == 0 else "Tek"
sonuc

# %%
"""
5 ten 50 ye kadar olan,5 in katları olan sayıların karelerini bir liste halinde yazdırmak istesek
"""
liste = []
for i in range(5,50,5):
    liste.append(i**2)
print(liste)

# %%
liste = [i**2 for i in range(5,50,5)]
print(liste)

# %%
"""
5 ten 50 ye kadar olan,5 in katları olan sayıların karelerinden ÇİFT olanları  bir liste halinde yazdırmak istesek
"""
liste = []
for i in range(5,50,5):
    if i**2 % 2 ==0:
        liste.append(i**2)
print(liste)

# %%
liste = [i**2 for i in range(5,50,5) if i**2 % 2== 0]
print(liste)

# %%
"""
5 ten 50 ye kadar olan,5 in katları olan sayıların karelerinden ÇİFT olanları sayılarla birlikte sözlük  halinde yazdırmak istesek
"""
sozluk = {i:i**2 for i in range(5,50,5) if i **2 % 2 == 0}
print(sozluk)

# %%



