"""Написать скрипт, содержащий функцию, получающую на входе метку класса и возвращающую следующий экземпляр (путь к нему) 
этого класса. Экземпляры идут в любом порядке, но не повторяются. Когда экземпляры заканчиваются, функция возвращает None.
Данная функция должна быть в трёх версиях для пунктов 1–3."""
import csv

def forteen_script(star):
    with open("classmates.csv", "r") as fh:
        reader = csv.reader(fh) # (!) обратите внимание, что reader возвращает итератор
        spisok = list(reader)  # поэтому мы делаем приведение к типу list
    for element in spisok:
        if element[2] == str(star): print(element[0])


if __name__=="__main__":
    forteen_script(1)