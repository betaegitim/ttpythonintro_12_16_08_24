"""
Bir okulun öğrenci kayıt sistemini modellemek için Nesneye Yönelik Programlama (OOP) kullanacağız. 
Her öğrencinin adı, soyadı, numarası, not ortalaması gibi özellikleri olduğunu düşünün. 
Bu sistemi modellemek için hangi sınıfları oluşturursunuz? 
Bu sınıfların içinde hangi metotlar (fonksiyonlar) bulunur?
"""
class Ogrenci:
    def __init__(self,ad,soyad,numara,not_ort):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.not_ort = not_ort
    
def info(ad,soyad,numara,not_ort):
    print()

