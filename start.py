#-*- coding: utf-8 -*-
import random
import pandas

import urllib2

#Делает Ирина
from class_tevent import *
from class_tperson import *
from class_tcriterion import *
#Делает Коля
#from load_csv_persons import *

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
        r.append (z.split(";"))
        print(z)
    f.close()
    return r


def main():
    # Получить данные
    url = "https://docs.google.com/spreadsheets/d/14feIvAtETBQ7eAh_468PqpzyfZiR_RNJuku5nbOVJ6U/export?format=csv&id=14feIvAtETBQ7eAh_468PqpzyfZiR_RNJuku5nbOVJ6U&gid=290850126"
    download_data(url)
    # Загрузить данные
    
    # Загрузить критерии
    
    # Анализ
    
    # Вывод рекомендаций
    

if __name__ == "__main__":
    main()
