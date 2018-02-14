#-*- coding: utf-8 -*-

# Класс, который описывает событие

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
#------------------------	
