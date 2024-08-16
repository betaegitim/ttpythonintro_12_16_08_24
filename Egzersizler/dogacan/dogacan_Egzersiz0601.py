"""
Galerici Çamoluk Otomotiv arabalarının satışını takip edebilmek için bir yazılımcıyla anlaşmıştır. 
Yazılımcı personelin bu arabaları kaydederken python programlama dilinde yazması gereken class için bir örnek oluşturalım
"""

class Araba:
     tip ="Araba"
     def __init__(self,marka,model,km):
         self.marka = marka
         self.model = model
         self.km = km
         self.satildimi = False


     def arabaBilgiVer(self):
         print("*"*30)
         print(self.marka,self.model,self.km,"satıldı" if self.satildimi else "satılmadı", sep="\n")
         print("*"*30)

    def arabayisat(self):
        self.satildimi = True
        return True
             
a= Araba(2,"Tek Kapı")
b= Araba(4,"4 Kapı")