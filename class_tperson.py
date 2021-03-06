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
        self.types_events = ["олимпиада", "нпк", "конкурс", "спорт"]
        self.prof = []
        buf = ["ученый по профилю", "аналитик", "педагог по профилю" ]
        self.prof.append(buf)
        buf = ["менеджер", "авиаинженер", "ученый", "врач"]
        self.prof.append(buf)
        buf = ["актер", "кондитер", "парикмахер", "дизайнер"]
        self.prof.append(buf)        
        buf = ["спортивный психолог", "спортсмен", "тренер", "спортивный комментатор", "спасатель", "пожарный", "военный", "полицейский"]
        self.prof.append(buf)        
    
    def add_event(self,data):
        """
        """
        for i in data:
            self.myevents.append(TEvent(i))
    
    def __str__(self):
        """
        """
        print("-------------------")
        print("ФИО: %s %s %s"%(self.name1, self.name2, self.name3))
        print("Дата рождения: %s"%(self.data))
        print

    def update_status(self):
        """
        """
        kriterii=[[[1,3,3,4],[5,7,7,10],[10,12,12,15],[10,12,12,15],[4,6,7,8]],
                  [[4,6,6,6],[7,15,15,15],[9,20,20,20],[18,25,25,25],[0,0,0,0]],
                  [[4,6,6,6],[5,10,10,10],[6,15,15,15],[7,20,20,20],[0,0,0,0]],
                  [[3,4,4,4],[5,10,10,10],[9,15,15,15],[0,0,0,0],[0,0,0,0]]]
        score = [0,0,0,0]
        for i in self.myevents:
            for j in range(len(score)):
                score[j] += i.keywords_score[j]
        m = 0
        
        for i in range(len(score)):
            if m<score[i]:
                m = i
        print("      ( \\")
        print("       \ \\")
        print("       / /                |\\")
        print("      / /     .-`````-.   / ^`-.")
        print("      \ \    /         \_/  {|} `o")
        print("       \ \  /   .---.   \\ _  ,--'")
        print("        \ \/   /     \,  \( `^^^")
        print("         \   \/\      (\  )")
        print("          \   ) \     ) \ \\")
        print("      jgs  ) /__ \__  ) (\ \___")
        print("          (___)))__))(__))(__)))")
        print("")
        print("### Результат анализа")
        for i in range(len(score)):
            print("\t\t ------==> %s : \t\t %s <==-------"%(self.types_events[i], score[i]))
        
        print("У вас отмечена активность в %s"%(self.types_events[m]))
        print("Рекомендуемый набор профессий:")
        for i in self.prof[m]:
            print("\t %s"%(i))
        print("---------------")

            
