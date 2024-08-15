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



