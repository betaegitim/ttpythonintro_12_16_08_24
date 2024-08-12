liste = ["cengiz","ahmet","aysen","ceyda","dogacan","merve","gunhan","oguz","onur"]
import os
os.mkdir("Egzersizler")
fileName = "ilk.py"
for item in liste:
    if not os.path.exists(os.path.join("Egzersizler",item)):
        os.mkdir(os.path.join("Egzersizler",item))
    open(os.path.join("Egzersizler",item,fileName),"w+")