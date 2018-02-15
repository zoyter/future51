#-*- coding: utf-8 -*-

# Класс, который описывает событие


#level_of_event = ["школа", "город", "регион", "страна", "мир"]
#type_of_event = ["очное", "заочное"]

class TEvent():
    def __init__(self,data):
        """
        """
        self.name = data[1] #название
        self.date = data[2] #дата проведения
        self.level = data[3] #уровень из описания
        x=self.name+self.level
        self.level_of_event = self.detect_level(x)
                                # уровень мероприятия [0 - "школа", 1 - "город", 2 - "регион", 3 - "страна", 4 - "мир"]
        self.type_of_event = self.detect_type1(x)
                                # тип мероприятия [0 - "очное", 1 - "заочное"]
        self.place = data[4] #место проведения
        self.school_class = data[5] #класс ученика на момент проведения события
        self.tutor = data[6] #руководитель
        self.place_of_event = data[7] #результат ученика
        #self.description = data[8] #описание
        
        self.keywords_events = []
        
        self.types_events = ["олимпиада", "нпк", "конкурс", "спорт"]
        
        self.keywords_score = [0,0,0,0]
        # Олимпиада
        buf = ["олимпиада", "чемпионат"]        
        self.keywords_events.append(buf)
        # НПК
        buf = ["конференция", "чемпионат"]        
        self.keywords_events.append(buf)
        # Конкурс
        # эстафета пробег турнир первенство соревнование чемпионат 
        buf = ["конкус", "чемпионат"]        
        self.keywords_events.append(buf)                
        # Спорт
        buf = ["атлетик", "пробег", "шахмат", "акробат", "старт", "спорт"]
        self.keywords_events.append(buf)
        
        self.detect_type2(x)
        
        #print(z)
            
    def detect_level(self,stroka):
        """
        """
        status = 0
        if stroka.lower().find("муницип")!=-1 or stroka.lower().find("городск")!=-1:
            status = 1
        if stroka.lower().find("областн")!=-1:
            status = 2
        if stroka.lower().find("всеросс")!=-1:
            status = 3
        if stroka.lower().find("международн")!=-1:
            status = 4
        return status
        
    def detect_type1(self,stroka):
        """ форма мероприятия
        """
        type_of_event = 1
        if stroka.lower().find("заочн")!=-1:
            type_of_event = 0
        return type_of_event
    
    def detect_type2(self,data):
        """ тип мероприятия
        """    
        #buf = data.split(" ")
        #stroka.lower().count("заочн")
        self.keywords_score
        self.keywords_events
        
        for i in range(len(self.keywords_events)):
            c = 0
            for j in self.keywords_events[i]:
                c += data.count(j)
            self.keywords_score[i] = c
        print(self.keywords_score)


        
        #for i in buf:
            #for j in range(len(self.keywords_events)):
                #if i in self.keywords_events[j]:
                    #self.score[j] += 1
        
        
        print("----------")
        

            
    def __str__(self):
        """
        """
        print("-------------------------------------")
        print("Информация о событии:")
        print("\t Название: %s"%(self.name))
        print("\t Дата: %s"%(self.date))
        print("\t Уровень из описания: %s"%(self.level))
        print("\t Уровень мероприятия: %s"%(self.level_of_event))
        print("\t Тип мероприятия: %s"%(self.type_of_event))
        print("\t Место проведения: %s"%(self.place))
        print("\t Rласс ученика на момент проведения события: %s"%(self.school_class))
        print("\t Руководитель: %s"%(self.tutor))
        print("\t Результат ученика: %s"%(self.place_of_event))
        print("\t Описание: %s"%(self.description))
        print("-------------------------------------")
        
