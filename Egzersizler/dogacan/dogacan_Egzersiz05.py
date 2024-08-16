"""
Bir kullanıcıdan bir sayı girmesini isteyen bir Python programı yazınız. 
Kullanıcı sayı yerine harf veya özel karakter girerse, bir hata mesajı versin.
Program her durumda "Program sona erdi" mesajını ekrana yazdırsın.
"""

class Cokgen:
     tip ="Araba"
     def __init__(self,kapisayi,isim):
          if isinstance(kapisayi,int) and kapisayi > 1:
              self.kapisayitoplam = kapisayi
              self.kapisayi = kapisayi
          else:
               raise ValueError("Kapı Sayısı Kontrol edilmeli")
          self.cokgenBilgi()     

     def cokgenBilgi(self):
         print("#"*30)
         print(self.isim,self.kenarsayi,self.icAciToplam)
         print("#"*30)
a= Cokgen(2,"Tek Kapı")
b= Cokgen(4,"4 Kapı")


