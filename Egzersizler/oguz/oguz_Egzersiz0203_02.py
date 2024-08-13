"""
liste = [24,35,65,67,68,90,86]
1. listenin 2. indisine 1000 sayısını ekleyelim
2. listenin sonunda 100 sayısını ekleyelim
3. listenin sonuna [1,2,3] listesini ekleyelim
4. listenin sonuna [1,2,3] listesini genişletelim
"""


liste = [24,35,65,67,68,90,86]
#1
liste.insert(2,1000)
#2
liste.append(100)
#3
liste.append([1,2,3])
#4
liste.extend([1,2,3])
