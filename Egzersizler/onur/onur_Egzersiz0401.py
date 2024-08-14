"""
parametre olarak gönderilen sayının kontrollerini 
tamamladıktan sonra o sayıya kadar olan tüm asal sayıların toplamını geri gönderen python fonkisyonunu yazınız
"""

def fonk(sayi:int)->int:
    """
    sayıya kadar olan 
    tüm asal sayıların 
    toplamını geri gönderen 
    python fonkisyonu
    """
    toplam = 0
    if isinstance(sayi,int):
        for i in range(2,sayi+1):
            # asal kontrol
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                toplam += i
        else:
            return toplam
    else:
        return 0

print(fonk(sayi=9))