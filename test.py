print(globals())
def testFonk():
    global a
    a = 3
    print("Fonk içerisindeki a=",a)
testFonk() # 3
print("2-Dışarıdaki a=",a) # 3
# print(globals())
print(locals())