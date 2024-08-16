"""
Bir kullanıcıdan bir sayı girmesini isteyen bir Python programı yazınız. 
Kullanıcı sayı yerine harf veya özel karakter girerse, bir hata mesajı versin.
Program her durumda "Program sona erdi" mesajını ekrana yazdırsın.
"""

class Cokgen:
     tip ="Çokgen"
     def __init__(self,kenarsayi,isim):
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
a= Cokgen(3,"Üçgen1")
b= Cokgen(3,"Üçgen2")
c= Cokgen(4,"Kare")


