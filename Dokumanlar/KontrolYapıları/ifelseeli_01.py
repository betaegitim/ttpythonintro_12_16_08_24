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

# %%



