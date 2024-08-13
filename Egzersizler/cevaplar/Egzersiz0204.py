"""

1. Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
sozluk = {}
sozluk = dict1 | dict2 | dict3 
print(sozluk)


"""sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
2. Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız
Beklenen Çıktı :(6,60)
"""
sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sozluk.popitem())


"""dict1={1:10, 2:20}
3. Yukarıdaki sözlüğe bir eleman ekleyiniz. 
Beklenen Çıktı :{1:10, 2:20, 3:30}
"""
dict1={1:10, 2:20}
dict1[3] = 30
print(dict1)

"""liste=[1,2,3,4,5]
4. 
    a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun 
    b.sözlüğün her alamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin.
Beklenen Çıktı :
a. {1:0,2:0,3:0,4:0,5:0}
b. {1:10,2:20,3:30,4:40,5:50}
"""
liste=[1,2,3,4,5]
#a.
sozluk = dict.fromkeys(liste,0)
print(sozluk)
#b.
sozluk = {a:a*10 for a in liste}
print(sozluk)

"""5. sozluk={1:10,2:20,3:30,4:40,5:50}
Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz
"""
sozluk={1:10,2:20,3:30,4:40,5:50}
sozluk.setdefault(6,60)
print(sozluk)