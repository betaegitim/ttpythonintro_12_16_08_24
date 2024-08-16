"""
Bir okulun öğrenci kayıt sistemini modellemek için Nesneye Yönelik Programlama (OOP) kullanacağız. 
Her öğrencinin adı, soyadı, numarası, not ortalaması gibi özellikleri olduğunu düşünün. 
Bu sistemi modellemek için hangi sınıfları oluşturursunuz? 
Bu sınıfların içinde hangi metotlar (fonksiyonlar) bulunur?
"""
class Ogrenci:
    def __init__(self, ad, soyad, numara, not_ortalaması):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.not_ortalaması = not_ortalaması
    def bilgi_gir(self):
        print(f"Adı:{self.ad}, Soyadı:{self.soyad}, Numara:{self.numara}, Not_Ortalaması:{self.not_ortalaması}") 

    def kaldı_mı(self):
        if self.not_ortalaması >= 50:
            return "Geçti"
        else:
            return "Kaldı"       
    


