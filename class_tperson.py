#-*- coding: utf-8 -*-

# Класс, который описывает персону и ее участие в событиях

class TPerson():
	def __init__(self, name1 = "", name2 = "", name3 ="", bdate = ""):
		self.name1 = name1
		self.name2 = name2
		self.name2 = name3
		self.bdate = bdate
		self.interest = interesr
		self.myevents = []
	
	def __str__(self):
		print("-------------------")
		print("ФИО: %s %s %s"%(self.name1, self.name2, self.name3))
		print("Дата рождения: %s"%(self.data))
