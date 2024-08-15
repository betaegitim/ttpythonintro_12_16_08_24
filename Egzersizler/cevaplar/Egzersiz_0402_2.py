"""
girilen sayıların ortalamasını hesapyalan python fonkisyonunu yazınız
"""
def ortalama(*args):
    return sum(args)/len(args)
liste = [1,2,3]
print(ortalama(*liste))