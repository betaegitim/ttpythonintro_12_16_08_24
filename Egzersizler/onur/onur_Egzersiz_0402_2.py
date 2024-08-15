"""
girilen sayıların ortalamasını hesapyalan python fonkisyonunu yazınız

"""

def ortalama(*args):
    return sum(args)/len(args)
liste = [1,2,3]
print(ortalama(*liste))


#liste=[10,20,30,40,50,60]
 
#toplam=0
#for sayi in liste:
  #  toplam+=sayi
    
#adet=len(liste)
#print(toplam/adet)