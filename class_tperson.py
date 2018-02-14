#-*- coding: utf-8 -*-

# Класс, который описывает персону и ее участие в событиях

from class_tevent import *

class TPerson():
    def __init__(self, name1 = "", name2 = "", name3 ="", bdate = "",global_skill=0,hard_skill=0,soft_skill=0):
        self.name1 = name1
        self.name2 = name2
        self.name2 = name3
        self.bdate = bdate
        self.myevents = []
        self.global_skill = global_skill
        self.hard_skill = hard_skill
        self.soft_skill = soft_skill
    
    def add_event(self,data):
        """
        """
        for i in data:
            self.myevents.append(TEvent(i))
            
        #n = 0
        #for i in person.myevents:
            #n += 1
            #print("---------------")
            #print("Событие №%s"%(n))
            #for j in i:
                #print("\t %s"%(j))
            #print("----------------")
    
    def __str__(self):
        """
        """
        print("-------------------")
        print("ФИО: %s %s %s"%(self.name1, self.name2, self.name3))
        print("Дата рождения: %s"%(self.data))

    def update_status(self):
        """
        """
        kriterii=[[[1,3,3,4],[5,7,7,10],[10,12,12,15],[10,12,12,15],[4,6,7,8]],
                  [[4,6,6,6],[7,15,15,15],[9,20,20,20],[18,25,25,25],[0,0,0,0]],
                  [[4,6,6,6],[5,10,10,10],[6,15,15,15],[7,20,20,20],[0,0,0,0]],
                  [[3,4,4,4],[5,10,10,10],[9,15,15,15],[0,0,0,0],[0,0,0,0]]]
        #for i in self.myevents:
        #    self.global_skill += kriterii[???][every_event.level_of_event][every_event.place_of_event]
            
