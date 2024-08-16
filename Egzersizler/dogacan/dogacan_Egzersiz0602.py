"""
Bir okulun öğrenci kayıt sistemini modellemek için Nesneye Yönelik Programlama (OOP) kullanacağız. 
Her öğrencinin adı, soyadı, numarası, not ortalaması gibi özellikleri olduğunu düşünün. 
Bu sistemi modellemek için hangi sınıfları oluşturursunuz? 
Bu sınıfların içinde hangi metotlar (fonksiyonlar) bulunur?
"""

class Ogrenci:
    tip = "Ogrenci"
    def __init__(self,adi,soyadi,numara,ortalama):
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara
        self.ortalama = ortalama
    def ogrencibilgi(self):
        print("*"*30)
        print(self.adi,self.soyadi,self.numara,self.ortalama)    
        print("*"*30)
a = Ogrenci("Jose","Kleberson",35,3)
b = Ogrenci("Guti","Hernandez",40,3.5)
a.ogrencibilgi()
b.ogrencibilgi()