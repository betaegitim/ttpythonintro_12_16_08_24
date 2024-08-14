# %% [markdown]
# # Diğer Değişken Tipleri
# * dict
# * set

# %% [markdown]
# ## dict

# %%
sozluk = {}
print(type(sozluk))

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç"
}
print(type(sozluk))

# %%
#         key:value
sozluk = {"1":"Bir"}
#           item
#         key:value
# key  => str,tuple ve sayısal veri tipleri
# value => herşey


# %% [markdown]
# ### Dict Erişim

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç"
}
sozluk["1"] # => "Bir"

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç"
}
# sozluk["4"] # Hata verir çünkü sözlük içerisinde yok

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç"
}
sozluk.get("1")

# %%
print(sozluk.get("4")) # Hata vermez None değerini döner

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç",
    "1":"One" # 1 anahtarını güncellemiş olur
}
len(sozluk)

# %%
sozluk.get("1")

# %% [markdown]
# ### Güncelleme ve Ekleme

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç"
}
sozluk["1"] = "One" # Güncelleme 
sozluk

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç"
}
sozluk["4"] = "Dört" # Ekleme
sozluk

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç"
}
print(sozluk.setdefault("1","One")) # güncellemez,olanı getirir
sozluk

# %%
sozluk = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç"
}
print(sozluk.setdefault("4","Dört")) # olmayan bir bilgiyi ekler verdiğiniz bilgiyi gönderir
sozluk

# %%
s1 = {
    "1":"Bir",
    "2":"İki",
    "3":"Üç",
    "4":"Dört"
}
s2 = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "5":"Five"
}
s1.update(s2)
s1

# %%
alanisimleri = ["adi","soyadi","telefon","adres"]
sozluk = dict.fromkeys(alanisimleri,-1)
sozluk

# %%
sozluk = {}
s2 = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "5":"Five"
}
# zip(["adi","soyadi","telefon","adres"],["ali","veli",555,s2])
sozluk.update(zip(["adi","soyadi","telefon","adres"],["ali","veli",555,s2]))
sozluk

# %% [markdown]
# ### Silme ve temizleme

# %%
s1 = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
print(s1.popitem()) # son eklenmiş olan eleman silinir
print(s1)

# %%
s1 = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
print(s1.pop("4")) # son eklenmiş olan eleman silinir
print(s1)

# %%
s1.clear()
s1

# %% [markdown]
# ### Diğerleri

# %%
s1 = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
s1.items()

# %%
s1 = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
s1.keys()

# %%
s1 = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
s1.values()

# %% [markdown]
# ## set

# %%
kume = set()
print(type(kume))

# %%
l1 = [1,1,1,2,2,2,3,1,1,2,2,3,4,2,1,1,2,2,3,3,4,1]
l2 = [1,2,2,3,3,2,4,5,6,2,2,2,1,2,2,2,2,3,4,5,6,2]
k1 = set(l1)
k2 = set(l2)
k1,k2

# %%
k2.difference(k1)

# %%
k2.intersection(k1)

# %%
k1 = {1,2,3,4}
k2 = {1,2,5,6}
k2.symmetric_difference(k1)

# %%
k1.union(k2)

# %%



