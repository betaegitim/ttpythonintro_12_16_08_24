# %% [markdown]
# # Fonksiyonlar
# * Tanımlama
# * Çağırma
# * return deyimi
# * parametre tanımları
#     - 1. yöntem `(a,b)`
#     - 2. yöntem `*args`
#     - 3. yöntem `**kwargs`
# 

# %% [markdown]
# ## Tanımlama

# %%
def fonk():# tanımlama
    print("Merhaba")

# %% [markdown]
# ## Çağırma

# %%
fonk() # çağırma

# %% [markdown]
# ## return

# %%
def fonk():# tanımlama
    print("Merhaba")
a = fonk()
print(a)

# %%
def fonk():# tanımlama
    return 4+2
a = fonk()
print(a)

# %%
def fonk():# tanımlama
    return 4+2
    print("ÇALIŞMAZ")
a = fonk()
print(a)

# %% [markdown]
# ## Parametre Tanımlama

# %% [markdown]
# ### 1. Yöntem

# %%
def fibo():
    a = b = 1
    print(a,b,sep=" ")
    for i in range(10):
        print(a+b,end=" ")
        a,b = b,(a+b)
fibo()

# %%
def fibo(sayi):
    a = b = 1 # TODO buradaya docstring yazılacak
    print(a,b,sep=" ")
    for i in range(sayi):
        print(a+b,end=" ")
        a,b = b,(a+b)
fibo(5)

# %%
def topla(a,b):
    return a+b
topla(2,3)

# %%
topla(topla(4,5),topla(3,2))

# %%
def topla(a,b,c=0):
    return a+b+c
print(topla(2,3))
print(topla(2,3,5))

# %%
print(topla(b=2,a=3))

# %%
def topla(a,b,c=0,d=0):
    return a+b+c+d

# %%
print(topla(2,3))
print(topla(2,3,5))
print(topla(2,3,5,7))

# %%
def fonk(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
fonk(1,2,3,4,e=5,f=6)

# %% [markdown]
# ### 2. Yöntem `*args`

# %%
def topla(*args):
    print(type(args))
topla()
topla(1,2,3,4,5,6,7)
topla(1,2,3)

# %%
def topla(*args):
    sonuc = 0
    for item in args:
        if isinstance(item,int):
            sonuc += item
    return sonuc 
topla(),topla(1,2,3,4,5,6,7),topla(1,2,3)

# %%
topla(*[1,2,3,4,5,6])

# %%
def topla(*args):
    return sum([item for item in args if isinstance(item,int)])
topla(),topla(1,2,3,4,5,6,7),topla(1,2,3)

# %% [markdown]
# ### 3. Yöntem `**kwargs`

# %%
def fonkOrnek(**kwargs):
    for key,value in kwargs.items():
        if key == "topla":
            print(f"{value[0]} + {value[1]} = {value[0] + value[1]}")
        if key == "cikar":
            print(f"{value[0]} - {value[1]} = {value[0] - value[1]}")
fonkOrnek()

# %%
fonkOrnek(topla=[25,15],cikar=[10,10])

# %%
fonkOrnek(cikar=[10,10])

# %% [markdown]
# ## 3 yöntemin bir arada kullanılması

# %%
def fonk(a,b,*args,**kwargs):
    print(a,b)
    print(args)
    print(kwargs)
fonk(1,2,3,4,5,6,7,8,param1=8)

# %%
sayi = 5
from functools import reduce
import operator
def fonk(number):
    return reduce(operator.mul,range(number,0,-1),1)
print(fonk(5))

# %%



