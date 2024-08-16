# %% [markdown]
# # Object Oriented Programming
# * Sınıf ve Nesne => Class and Instance
# * Metot ve Özellik => Method and Attribute
# * Örnek Class

# %% [markdown]
# ## Class and Instance

# %%
class Sinif: # Sınıf
    pass
obj1 = Sinif() # Instance
obj2 = Sinif() # Instance

# %%
a = 2
print(type(a))

# %%
print(type(print))

# %% [markdown]
# ## Method and Attribute
# * Class Method
# * Class Attribute
# * Instance Method
# * Intance Attribute

# %%
class Sinif: # Sınıf
    sinifOzelligi = "SINIF ÖZELLİĞİ"
    def __init__(self): # constructor
        self.ornekOzellik = "ÖRNEK ÖZELLİĞİ"
    
    def ornekMethod(self):
        print("ÖRNEK METHOD ÇALIŞTI")
        print(self.ornekOzellik)

    @classmethod # decorator
    def sinifMetodu(cls):
        print("SINIF METHOD ÇALIŞTI")
        print(cls.sinifOzelligi)
    


# %%
class Sinif: # Sınıf
    sinifOzelligi = "SINIF ÖZELLİĞİ"
    def __init__(self,param1): # constructor
        self.ornekOzellik = param1 # instance attribute
    
    def ornekMethod(self): # instance method 
        print("ÖRNEK METHOD ÇALIŞTI",self.ornekOzellik)

    @classmethod # decorator
    def sinifMetodu(cls):
        print("SINIF METHOD ÇALIŞTI")
        print(cls.sinifOzelligi)
obj1 = Sinif("A")
obj2 = Sinif("B")

# %%
obj1.ornekMethod()

# %%
obj2.ornekMethod()

# %%
obj1.ornekOzellik

# %%
obj2.ornekOzellik

# %%
Sinif.sinifMetodu()
obj1.sinifMetodu()
obj2.sinifMetodu()

# %%
print(obj1.sinifOzelligi)
print(obj2.sinifOzelligi)
print(Sinif.sinifOzelligi)

# %% [markdown]
# Hülagü Orçun Çokgenlerle ilgili bir ödev yapmaktadır. Ödev çokgenlerin yönetilebileceği bir sınıf oluşturması üzerinedir. 

# %%
""" 
üçgen
beşgen
kare
altıgen
"""
# çokgen

# içaçıların toplamı
# kenarsayısı
# isim

# %%
class Cokgen:
    tip = "Çokgen"
    def __init__(self,kenarsayi,isim):
        self.isim = isim
        if isinstance(kenarsayi,int) and kenarsayi > 2:
            self.icAciToplam = (kenarsayi-2)*180
            self.kenarsayi = kenarsayi
        else:
            raise ValueError("Kenar Sayısı Kontrol edilmeli")
        self.cokgenBilgi()
    
    def cokgenBilgi(self):
        print("#"*30)
        print(self.isim,self.kenarsayi,self.icAciToplam)
        print("#"*30)
a = Cokgen(3,"Üçgen1")
b = Cokgen(3,"Üçgen2")
c = Cokgen(4,"Kare")

# %%
a.tip,b.tip,c.tip

# %% [markdown]
# * Encapsulation => Kapsülleme
# * Inheritance => Kalıtım
# * Polymorphism => Çok Biçimlilik
# * Abstraction => Soyutlama

# %%



