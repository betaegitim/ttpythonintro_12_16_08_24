# %% [markdown]
# <!-- begin if
# end if
# sub
# end sub
# {}
# () -->
# # Karşılaştırma Yapıları
# * indentitation
# * if ve else
# * elif
# * tek satırda if yazımı

# %% [markdown]
# ```
# a = 3
# if a == 2:
# ---->print("Doğru") ---> indentitation girinti
# print("Çalışmaya devam")
# ```

# %%
a = 3
if a != 2:
    print("Doğru")
    print("girinti devam ediyor")
    if a % 2 > 0:
        print("sayı Tek")
print("Çalışmaya devam")

# %% [markdown]
# ## if ve else

# %%
a = 6
if a % 2 > 0:
    print("Tek")

# %%
a = 6
if a % 2 > 0:
    print("Tek")
else:
    print("Çift")

# %%
a = 0
b = []
c = ""
d = {}
if b:
    print("Dolu")
else:
    print("Boş")

# %%
giris = input("Sayıyı Giriniz:")
if giris:
    print("Giriş Yaptınız")
else:
    print("Giriş Yapılmadı")

# %%
giris = "a"
giris.isdigit()

# %%
a = 2
print(type(a))

# %%
isinstance(a,int)

# %% [markdown]
# ### Örnek Soru

# %%
sayi = input("Sayıyı Giriniz:") # str
if sayi and sayi.isdigit():
    sayi = int(sayi)
    if sayi % 2 == 0:
        print(sayi,"Çift")
    else:
        print(sayi,"Tek")
else:
    print("Giriş Hatası")

# %% [markdown]
# ## elif

# %%
"""
AA 100 - 85
BB 84  - 70
CC 69  - 55
DD 54  - 45
Kaldın  45 ten küçük
"""
notu = input("Notunuzu Giriniz:")
if notu.isdigit():
    notu = int(notu)
    if 85 <= notu <= 100: # 85 <= notu and notu <= 100
        print("AA")
    else:
        if 70 <= notu <= 84:
            print("BB")
        else:        
            if 55 <= notu <= 69:
                print("CC")
            else:
                if 45 <= notu <= 54:
                    print("DD")
                else:
                    print("Kaldın")
else:
    print("Giriş Hatası")


# %%
"""
AA 100 - 85
BB 84  - 70
CC 69  - 55
DD 54  - 45
Kaldın  45 ten küçük
"""
notu = input("Notunuzu Giriniz:")
if notu.isdigit():
    notu = int(notu)
    if 85 <= notu <= 100: # 85 <= notu and notu <= 100
        print("AA")
    elif 70 <= notu <= 84:
        print("BB")
    elif 55 <= notu <= 69:
        print("CC")
    elif 45 <= notu <= 54:
        print("DD")
    else:
        print("Kaldın")
else:
    print("Giriş Hatası")

# %% [markdown]
# ## Match Case

# %% [markdown]
# ```
# match expression:
#     case pattern1:
#         # pattern1 ile eşleşirse yapılacak işlemler
#     case pattern2:
#         # pattern2 ile eşleşirse yapılacak işlemler
#     case _:
#         # Hiçbiriyle eşleşmezse yapılacak işlemler
# ```

# %%
a = 2
b = 2.0
c = "TT"
d = [1,2,3]
e = (1,2,3)
f = {"1":"Bir"}
degisken = c
match degisken:
    case int():
        print("Int")
    case str():
        print("String")
    case float():
        print("Float")
    case _:
        print("Bilinmiyor")

# %%
komut = input("Komutu Giriniz:")

match komut:
    case "çık":
        print("Çıkış Yapıyorum")
    case "kaydet" as emir:
        print(f"İşlem yapılıyor {emir}")
    case _:
        print("Komut Bilinmiyor,")

# %%
liste = [1,2,3,4,5]
match liste:
    case []:
        print("Boş")
    case [1,2,3,4,5]:
        print("Dolu")


# %%



