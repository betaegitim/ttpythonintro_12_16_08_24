# %%
from abc import ABC,abstractmethod # abstract base class
class GeometrikSekil(ABC):
    @abstractmethod
    def alanhesapla(self):
        pass
    @abstractmethod
    def cevrehesapla(self):
        pass


# %%
from abc import ABC,abstractmethod # abstract base class
class GeometrikSekil(ABC):
    @abstractmethod
    def alanhesapla(self):
        pass
    @abstractmethod
    def cevrehesapla(self):
        pass

class Dikdortgen(GeometrikSekil):
    def __init__(self,uzunluk,genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik
    
    def alanhesapla(self):
        return self.uzunluk*self.genislik

    def cevrehesapla(self):
        return 2*(self.uzunluk+self.genislik)
dDortgen = Dikdortgen(25,30)

# %%



