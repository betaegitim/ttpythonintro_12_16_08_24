"""
Bir okulun öğrenci kayıt sistemini modellemek için Nesneye Yönelik Programlama (OOP) kullanacağız. 
Her öğrencinin adı, soyadı, numarası, not ortalaması gibi özellikleri olduğunu düşünün. 
Bu sistemi modellemek için hangi sınıfları oluşturursunuz? 
Bu sınıfların içinde hangi metotlar (fonksiyonlar) bulunur?
"""

class Ogrenci:
    def __init__(self,ad,soyad,numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.notlar = []

    def not_ekle(self,notu):
        self.notlar.append(notu)

    def not_ortalamasi(self):
        if len(self.notlar) == 0:
            return 0
        else:
            return sum(self.notlar) / len(self.notlar)

    def bilgileri_goster(self):
        print(f"Adı Soyadı: {self.ad} {self.soyad}")
        print(f"Numarası:{self.numara}")
        print(f"Not Ortalaması:{self.not_ortalamasi()}")

ogrenci1 = Ogrenci("Ali","Veli",123)
ogrenci2 = Ogrenci("Ayşe","Veli",456)

ogrenci1.not_ekle(95)
ogrenci1.not_ekle(80)
ogrenci2.not_ekle(75)
ogrenci2.not_ekle(60)

ogrenci1.bilgileri_goster()
ogrenci2.bilgileri_goster()