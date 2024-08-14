"""
parametre olarak gönderilen sayının kontrollerini 
tamamladıktan sonra o sayıya kadar olan tüm asal sayıların toplamını geri gönderen python fonkisyonunu yazınız
"""

sayi = input("Sayıyı Giriniz:")
def sonuc(sayi)=
if sayi.isdigit():
    sayi = int(sayi)
    
    for i in range(2,sayi+1):
        # asal kontrol
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)