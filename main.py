import first_script
import second_script
import third_script
"""
-Написать скрипт для формирования текстового файла-аннотации собранного датасета. Файл-аннотация должен представлять собой 
csv-файл, в котором в первой колонке будет указан абсолютный путь к файлу, во второй колонке относительный путь относительно 
вашего Python-проекта, третья колонка будет содержать текстовое название класса (метку класса), к которому относится данный 
экземпляр.

-Написать скрипт для копирования датасета в другую директорию таким образом, чтобы имена файлов содержали имя класса и его 
порядковый номер. То есть из dataset/class/0000.jpg должно получиться dataset/class_0000.jpg.


Написать скрипт, содержащий функцию, получающую на входе метку класса и возвращающую следующий экземпляр (путь к нему) 
этого класса. Экземпляры идут в любом порядке, но не повторяются. Когда экземпляры заканчиваются, функция возвращает None.
Данная функция должна быть в трёх версиях для пунктов 1–3.
Написать на основе предыщего пункта классы итераторы (пример ниже)."""
def main():
    print('h')
    first_script.first_script()
    second_script.second_script()
    third_script.third_script()
    #first_script.first_script()




if __name__=="__main__":
    main()