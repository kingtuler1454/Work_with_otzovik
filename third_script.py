import os
import random
import csv
"""Написать скрипт, создающий копию датасета таким образом, чтобы каждый файл из сходного датасета получил случайный номер от 
0 до 10000, и датасет представлял собой следующую структуру dataset/номер.jpg. Для того чтобы осталась возможность определить 
принадлежность экземпляра к классу создать файл-аннотацию (как в пункте 1)."""


def third_script():
    # redact file 1_0001.txt to random <10000 .txt
    names = [i for i in range(10000)]
    out_directory = os.path.dirname(__file__)
    if os.path.isdir("third_dataset") == False: os.makedirs("third_dataset")
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Абсолютный путь к файлу", "Относительный путь к файлу", "номер звезды"])
        for element in os.listdir("second_dataset"):
            name = random.choice(names)
            names.remove(name)
            with open(os.path.join("second_dataset", element), "rb") as f:
                text = f.read()
            with open(os.path.join("third_dataset", str(name)), "wb") as f:
                f.write(text)
            directory = os.path.join(out_directory, "third_dataset", str(name)+".txt")   
            file_writer.writerow([directory, os.path.join("second_dataset", element), element[0]])


if __name__=="__main__":
    third_script()