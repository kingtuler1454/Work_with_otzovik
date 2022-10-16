import os
import csv
from tqdm.notebook import tqdm_notebook


def first_script():
    out_directory = os.path.dirname(__file__)
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Абсолютный путь к файлу", "Относительный путь к файлу", "номер звезды"])
        for star in range(6):
            directory=os.path.join(out_directory,"dataset",str(star))
            for dirs,folder,files in os.walk(directory):
                for element in files:
                    print('\nПолный путь к файлу: '+str(dirs)+"/"+element)
                    file_writer.writerow([str(dirs)+"/"+element,"dataset"+'/'+str(star)+"/"+element, star])