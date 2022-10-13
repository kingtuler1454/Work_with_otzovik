import os
import csv
from tqdm.notebook import tqdm_notebook


def work():
    out_directory = os.path.dirname(__file__)
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = "\t", lineterminator="\r")
        file_writer.writerow(["Абсолютный путь к файлу", "Относительный путь к файлу", "номер звеззды"])
        for star in tqdm_notebook(range(6)):
            directory=os.path.join(out_directory,"dataset",str(star))
            for dirs,folder,files in os.walk(directory):
                for element in files:
                    print('\nПолный путь к файлу: '+str(dirs)+"/"+element)
                    file_writer.writerow([str(dirs)+"/"+element,"dataset"+'/'+str(star)+"/"+element, star])

    
    
    
        