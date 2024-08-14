"""
parametre olarak gönderilen sayının kontrollerini 
tamamladıktan sonra o sayıya kadar olan tüm asal sayıların toplamını geri gönderen python fonkisyonunu yazınız
"""

def kontrol(*args):
    sonuc=[]
    
    match args:
        case int():
            sonuc.append["int"]
            print("Int")
        case str():
            sonuc.append["String"]            
        case float():
            sonuc.append["Float"]
        case _:
            sonuc.append["int"]
    return sonuc