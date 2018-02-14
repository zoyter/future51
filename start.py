#-*- coding: utf-8 -*-
import random
import pandas

level_of_event = ["школа", "город", "регион", "страна", "мир"]
type_of_event = ["очное", "заочное"]
# Место на собыытии 0 - места не занял, 1,2,3
place_on_event = 0

class TEvent():
	def __init__(self, name = "", date = "", place = "", description = ""):
		self.name = name
		self.date = date
		self.place = place
		self.description = description
	def __str__(self):
		print("-------------------------------------")
		print("Информация о событии:")
		print("\t Название: %s"%(self.name))
		print("\t Дата: %s"%(self.date))
		print("\t Место: %s"%(self.place))
		print("\t Описание: %s"%(self.description))
		print("-------------------------------------")
		

class TPerson():
	def __init__(self, name1 = "", name2 = "", name3 ="", bdate = ""):
		self.name1 = name1
		self.name2 = name2
		self.name2 = name3
		self.bdate = bdate
		self.interest = interesr
	
	def __str__(self):
		print("-------------------")
		print("ФИО: %s %s %s"%(self.name1, self.name2, self.name3))жде
		print("Дата рождения: %s"%)
		

class TCriterion():
	def __init__(self):
		self.level

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

def get_criterii_ocenki(fname):
	""" Читаем критерии оценки
		
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
	fname = "data.csv"
	get_data_from_file(fname)
	fname = "kriterii.csv"
	get_criterii_ocenki()

	  
	

	

if __name__ == "__main__":
	main()
