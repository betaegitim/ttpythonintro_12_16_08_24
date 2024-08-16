# %% [markdown]
# # Polymorphism => Çok Biçimlilik

# %%
print(1)
print("2")

# %%
def fonk(a,b):
    return a+b
def fonk2(a,b):
    return a*b
liste = [fonk,fonk2]
for item in liste:
    print(item(2,3))

# %%
class A: # parent super
    def __init__(self):
        self.a = "a"
    
    def soyle(self):
        print("A sınıfından çalıştım")
    
    def soyleA(self):
        print(self.a)

class B(A): # child 
    def __init__(self): #overload
        super().__init__()
        self.b = "b"

    def soyle(self): # override 
        print("B sınıfından çalıştım") 

    def soyleB(self):
        print(self.b)

# %%
class A: # parent super
    def __init__(self):
        self.a = "a"
    
    def soyle(self):
        print("A sınıfından çalıştım")
    
    def soyleA(self):
        print(self.a)

class B: # parent super
    def __init__(self):
        self.b = "b"
    
    def soyle(self):
        print("B sınıfından çalıştım")
    
    def soyleB(self):
        print(self.b)

objA = A()
objB = B()
def fonk(obj):
    obj.soyle()
liste = [objA,objB]
for item in liste:
    fonk(item)

# %%
class Kitap:
    def __init__(self, isbn, baslik, yazar, yayinevi, yayin_yili):
        self.isbn = isbn
        self.baslik = baslik
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.yayin_yili = yayin_yili
        self.durum = "Rafta"  # Rafta, Ödünç, Kayıp gibi durumlar

    def ode_ucret(self):
        if self.durum == "Kayıp":
            # Kayıp kitap için ücret hesaplama işlemi
            print("Kayıp kitap için ücret hesaplandı.")

class Uye:
    def __init__(self, ad, soyad, uyeno, telefon):
        self.ad = ad
        self.soyad = soyad
        self.uyeno = uyeno
        self.telefon = telefon
        self.odunc_kitaplar = []

    def kitap_odunc_al(self, kitap):
        self.odunc_kitaplar.append(kitap)
        kitap.durum = "Ödünç"

    def kitap_teslim_et(self, kitap):
        self.odunc_kitaplar.remove(kitap)
        kitap.durum = "Rafta"

class Calisan:
    def __init__(self, ad, soyad, calisan_no, gorev):
        self.ad = ad
        self.soyad = soyad
        self.calisan_no = calisan_no
        self.gorev = gorev

    def kitap_ekle(self, kitap):
        # Kütüphane kataloğuna kitap ekleme işlemi
        print("Kitap kütüphane kataloğuna eklendi.")

# Nesneler oluşturma
kitap1 = Kitap("978-3-16-148410-0", "Yüzüklerin Efendisi", "J.R.R. Tolkien", "İthaki", 2005)
uye1 = Uye("Ali", "Veli", 12345, "5554443322")

# Kitap ödünç alma
uye1.kitap_odunc_al(kitap1)

# Kitap teslim etme
uye1.kitap_teslim_et(kitap1)


# %%



