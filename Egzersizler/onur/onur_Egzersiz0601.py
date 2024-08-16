"""
Galerici Çamoluk Otomotiv arabalarının satışını takip edebilmek için bir yazılımcıyla anlaşmıştır. 
Yazılımcı personelin bu arabaları kaydederken python programlama dilinde yazması gereken class için bir örnek oluşturalım
"""

class Araba:
    toplam = 0
    liste = []
    def __init__(self,marka,isim):
        self.marka = marka
        self.isim = isim
        if isinstance(marka,str):
            Araba.toplam += 1
            # self.toplam = Araba.toplam
        else:
            raise ValueError("Marka'yi kontrol ediniz")
        self.arabaBilgi()
 
    def arabaBilgi(self):
        print(self.marka,"Toplam Araba:",self.toplam,"=>",self.isim)
    
a = Araba("audi","A3")
b = Araba("Mercedes","GLA 200")
