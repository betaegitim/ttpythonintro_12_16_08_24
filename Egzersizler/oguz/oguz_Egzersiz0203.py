"""
1. Soru : 
var1 = "TÜRK TELEKOM" 
ifadesini değişken olarak tanımladıktan sonra 5. ve son indiste yer alan karakterleri ekrana yazdırınız.
"""

var1 = "TÜRK TELEKOM"
print(var1[5],var1[-1])

"""
2. Soru: liste = [2,3,5,7,11,13,17,21]
a. listenin ilk 3 elemanını ekrana yazdıran kod
b. listelinin son 3 elemanını ekrana yazdıran kod
c. listeden 2. indisten sonuna kadar 3 er adımla elemanları yazdıran kod
d. listenin tersinden yazımını yazdıran kod
"""
#a.
print(liste=[2,3,5,7,11,13,17,21])
#b.
print(liste[:3])
#c.
print(liste[-3:])
#d.
print(liste[2::3])
#e.
print(liste[::-1])


"""
3. Soru:
var1 = "             Python Programlama Dili           "
a. `a` harfini `e`harfi ile değiştiren kod
b. verilen metindeki tüm harflerin büyük olmasını sağlayan kod
c. verilen metindeki kelimeleri boşluklara göre birbirinden ayıran kod
d. Metnin başında ve sonunda yer alan boşlukları temizleyen kod
e. split ile bölümlenmiş parçaları ";" ile birleştiren kod
f. "Benim Adım {} Yaşım {}" şeklinde belirlenmiş metin içerisinde isim ve yaş bilgisini giren kod
"""