#-*- coding: utf-8 -*-
import random
import pandas

import urllib2

#from class_tevent import *
from class_tperson import *

#DEBUG = True
DEBUG = False

# 
if DEBUG:
    tmpdata = "tmp/data.csv"
else:
    tmpdata = "tmp/data_offline.csv"


def download_data(url):
    """ Получаем данные из сети
        если отладка включена, то берем данные локально
    """ 
    if DEBUG == 0:
        f = open(tmpdata,"w")        
        # Получаем данные из сети
        response = urllib2.urlopen(url)
        html = response.read()
        z = html.splitlines()
        for i in z:
            f.write(i)
            f.write("\n")
        f.close()
    print("Данные получены и сохранены на диск")


def get_data_from_file(fname):
    """ Читаем данные "портфолио"
    """
    f = open(fname,"r")
    # Список считанныйх данных
    r = []
    for i in f.readlines():
        z = i.replace("\n","")
        r.append (z.split(","))
    f.close()
    return r


def main():
    # Получить данные из сети
    url = "https://docs.google.com/spreadsheets/d/14feIvAtETBQ7eAh_468PqpzyfZiR_RNJuku5nbOVJ6U/export?format=csv&id=14feIvAtETBQ7eAh_468PqpzyfZiR_RNJuku5nbOVJ6U&gid=290850126"
    download_data(url)
    # Загрузить данные
    person = TPerson("Иванов", "Иван", "Иванович", "12.12.2004", "чтение, музыка, программирование")
    person.add_event(get_data_from_file(tmpdata))
    person.update_status()
    
    # Вывод рекомендаций
    

if __name__ == "__main__":
    main()
