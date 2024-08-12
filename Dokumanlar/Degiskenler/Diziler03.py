# %% [markdown]
# # Diziler
# * Dizilerde Erişim
# * str
#     - Yardımcı Fonksiyonlar
# * list
#     - Ekleme
#     - Güncelleme
#     - Silme
#     - Diğerleri
# * tuple
#     - index,count

# %% [markdown]
# ## Dizilerde Erişim

# %%
var1 = "Turk Telekom" # str
var2 = ["a","b","c","d"] # list
var3 = ("a","b","c","d") # tuple

# %% [markdown]
# ```
# var1[baslangic:bitis-1:adim]
# ```
# 

# %%
var1 = "BETA"
#       0123
#      -4-3-2-1
var1[0],var1[-4]

# %%
var1 = ["B","E","T","A"]
#       0.   1.  2.  3  
#       -4.  -3. -2. -1
var1[0],var1[-4]

# %%
var1 = ("B","E","T","A")
#       0.   1.  2.  3  
#       -4.  -3. -2. -1
var1[0],var1[-4]

# %%
var1[len(var2)-1],var1[-1]

# %%
var1 = "TÜRK TELEKOM"
#       012345
var1[0:4]

# %%
var1[0:-8]

# %%
var1[:-8]

# %%
var1[5:]

# %%
var1[1:8:2] # 1 3 5 7

# %%
tckimlikNo = "10000000146"
tckimlikNo[0:10:2] # 0 2 4 6 8

# %%
liste = [1,2,3,4,5,6,7,8,9,10,11]
#        0 1 2 3 4 5 6 7 8 9 10
liste[1:8:2]

# %%
liste[10:2:-3] # 10 7 4

# %%
liste[10:3:-1]

# %%
liste[:]

# %%
liste[::-1]

# %%
liste = [["a","b","c"],["d","e","f"],["g","h","i"]]
#          0        1       2
liste[0] # => ["a","b","c"]
#              0 1 2
liste[0][2]

# %%
liste = ["BETA",[1,2,3,4,5]]
liste[0][1],liste[1][1]

# %% [markdown]
# Yukarıdaki erişim yöntemleri str,list ve tuple veri tipleri için geçerlidir.

# %% [markdown]
# ## str

# %%
var1 = ""
var2 = ''
var3 = """""" # docstring
print(type(var1),type(var2),type(var3))

# %%
var1 = "1"
var2 = "2"
var1 + var2 # concatenate

# %%
var1 = "BETA"
# var1[0] = "3" # 'str' object does not support item assignment => immutable bir veri tipi olduğu için hata verdi

# %%
a = "Teşekkürler Süpermen"

# %% [markdown]
# ### Yardımcı Fonksiyonlar
# * replace
# * upper,lower
# * split
# * strip
# * join
# * capitalize
# * format
# * is fonksiyonları

# %%
# replace
a = "Teşekkürler Süpermen"
a.replace("e","ı").replace("ü","ı")

# %%
a

# %%
a = a.replace("e","ı").replace("ü","ı")
a

# %%
# upper,lower
a = "Teşekkürler Süpermen "
a.upper()

# %%
a = "Teşekkürler Süpermen"
a.lower()

# %%
# split
satir = "Merhaba;TT Akademi;Beta;1;2;3;4\n"
satir.split() # parametre verilmezse boşluk dikkate alınır

# %%
satir = "Merhaba;TT Akademi;Beta;1;2;3;4\n"
satir.split(";") # parametre verilmezse boşluk dikkate alınır

# %%
satir.split(";")[3]

# %% [markdown]
# --------------------------
# ```
# Escape Sequence
# \
# \n
# \b
# \t
# ```
# 

# %%
yol = "C:\talat\nalan\buket.html"
print(yol)

# %%
yol = "C:\\talat\\nalan\\buket.html"
print(yol)

# %%
yol = r"C:\talat\nalan\buket.html"
print(yol)

# %% [markdown]
# --------------------------

# %%
# strip 
var1 = "                               BETA AKADEMİ                            "
var1.strip()

# %%
var1 = "            ____________A_____   BETA AKADEMİ         __________________   "
var1.strip("_ A")

# %%
var1.rstrip("_ A")

# %%
var1.lstrip("_ A")

# %%
# join
";".join(["Türk","Telekom","Beta","Akademi","Python"])

# %%
import os
os.sep # Win => \ , Mac,Linux => /

# %%
os.sep.join(["Türk","Telekom","Beta","Akademi","Python"])

# %%
# capitalize
"python".capitalize()

# %%
# format
var1 = "Merhaba Sayın {} {}" # string interpolation
var1.format("Ali","Veli")

# %%
var1 = "Merhaba Sayın {1} {0}" # string interpolation
var1.format("Ali","Veli")

# %%
var1 = "Merhaba Sayın {a} {b}" # string interpolation
var1.format(a = "Ali",b = "Veli")

# %%
a = "Ali"
b = "Veli"
var1 = f"Merhaba Sayın {a} {b}" # string interpolation
var1

# %%



