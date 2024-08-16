liste = ["cengiz","ahmet","aysen","ceyda","dogacan","merve","gunhan","oguz","onur"]
import os
import shutil
# os.mkdir("Egzersizler")
fileName = "Egzersiz0602.py"
status = 1
for item in liste:
    if not os.path.exists(os.path.join("Egzersizler",item)):
        os.mkdir(os.path.join("Egzersizler",item))
    if status == 1:
        shutil.copy(os.path.join("Egzersizler","cevaplar",fileName),os.path.join("Egzersizler",item,f"{item}_{fileName}"))
    else:
        open(os.path.join("Egzersizler",item,fileName),"w+")

