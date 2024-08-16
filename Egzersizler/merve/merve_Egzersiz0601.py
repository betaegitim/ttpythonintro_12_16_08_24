"""
Galerici Çamoluk Otomotiv arabalarının satışını takip edebilmek için bir yazılımcıyla anlaşmıştır. 
Yazılımcı personelin bu arabaları kaydederken python programlama dilinde yazması gereken class için bir örnek oluşturalım
"""

class Satis:
    tip = "Araba"
    def __init__(self,model,yil,adet):
        self.model = model
        if isinstance(adet,int) and adet => 0:
            self.arabaToplam = (kenarsayi-2)*180
            self.kenarsayi = kenarsayi
        else:
            raise ValueError("Kenar Sayısı Kontrol edilmeli")
        self.cokgenBilgi()
    
    def cokgenBilgi(self):
        print("#"*30)
        print(self.isim,self.kenarsayi,self.icAciToplam)
        print("#"*30)
a = Satis(3,"Üçgen1")
b = Satis(3,"Üçgen2")
c = Satis(4,"Kare")