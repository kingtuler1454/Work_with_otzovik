from base64 import encode
import csv
import os


def second_script():
    with open("classmates.csv","r") as fh:
        reader = csv.reader(fh) # (!) обратите внимание, что reader возвращает итератор
        spisok = list(reader)  # поэтому мы делаем приведение к типу list
    if os.path.isdir("second_dataset")==False: os.makedirs("second_dataset")
    content=False
    for element in spisok:
        if content:
            with open(element[0],"rb") as f:
                text=f.read()
                namefile=element[1].split("/")
            with open(os.path.join("second_dataset",element[2]+"_"+namefile[2]),"wb") as f:
                f.write(text)
        content=True