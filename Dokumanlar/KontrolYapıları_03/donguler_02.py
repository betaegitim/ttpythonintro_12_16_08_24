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

# %%



