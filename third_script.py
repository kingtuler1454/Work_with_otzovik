import os
import random

import csv


def third_script(path: str) -> str:
    # redact file 1_0001.txt to random <10000 .txt
    names = [i for i in range(10000)]
    out_directory = os.path.dirname(__file__)
    if os.path.isdir("third_dataset") is False:
        os.makedirs("third_dataset")
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
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


def iterator3(name: str) -> str:
    '''create a csv'''
    names = os.listdir(os.path.join("dataset", name))
    for i in range(len(names)):
        yield (names[i])  # делаем итератор
    return None


class Iterator3_txt:
    def __init__(self, name: str):
        self.names = os.listdir(os.path.join("dataset", name))
        self.limit = len(self.names)
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration


def script_3(name: str) -> None:
    """create a csv"""
    third_script(name)


if __name__ == "__main__":
    script_3("rt")
