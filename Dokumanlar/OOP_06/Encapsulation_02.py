# %% [markdown]
# # Encapsulation

# %%
import uuid

myuuid = uuid.uuid4()
print(type(myuuid))

# %%
import uuid
class Hayvan:
    def __init__(self,tur,isim,yas):
        self.tur = tur
        self.isim = isim
        self.yas = yas
        self.__kimlikNo = uuid.uuid4()

    def isminiSoyle(self):
        print(self.isim) 

melek = Hayvan("Kedi","Melek","4")
melek.isminiSoyle()
print(melek.isim)
print(melek.__kimlikNo)


# %% [markdown]
# ```
# __gizli => gizli
# __gizli_ => gizli
# __gizli__ => GİZLİ DEĞİL
# _yarigizli => yarı gizli dikkat etmek için kullanılır
# ```

# %%
import uuid
class Hayvan:
    def __init__(self,tur,isim,yas):
        self.tur = tur
        self.isim = isim
        self.yas = yas
        self.__kimlikNo = uuid.uuid4()

    def kimlikNo(self): # getter
        return self.__kimlikNo

    def isminiSoyle(self):
        print(self.isim) 

melek = Hayvan("Kedi","Melek","4")
melek.isminiSoyle()
melek.kimlikNo() ##########

# %%
import uuid
class Hayvan:
    def __init__(self,tur,isim,yas):
        self.tur = tur
        self.isim = isim
        self.yas = yas
        self.__kimlikNo = uuid.uuid4()

    @property
    def kimlikNo(self): # getter
        return self.__kimlikNo

    def isminiSoyle(self):
        print(self.isim) 

melek = Hayvan("Kedi","Melek","4")
melek.isminiSoyle()
melek.kimlikNo ##################

# %%
import uuid
class Hayvan:
    def __init__(self,tur,isim,yas):
        self.tur = tur
        self.isim = isim
        self.yas = yas
        self.__kimlikNo = uuid.uuid4()

    @property
    def kimlikNo(self): # getter
        return self.__kimlikNo

    @kimlikNo.setter
    def kimlikNo(self,param1):
        if isinstance(param1,uuid.UUID):
            self.__kimlikNo = param1
        else:
            raise ValueError("Değer Hata")

    @kimlikNo.deleter
    def kimlikNo(self):
        print("SİLİNEMEZ")
        raise Exception("Silme Hatası")

    def isminiSoyle(self):
        print(self.isim) 

melek = Hayvan("Kedi","Melek","4")
melek.isminiSoyle()
print(melek.kimlikNo) ##################
melek.kimlikNo = uuid.uuid4()
del melek.kimlikNo


# %%



