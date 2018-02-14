#-*- coding: utf-8 -*-

# Класс, который описывает событие


#level_of_event = ["школа", "город", "регион", "страна", "мир"]
#type_of_event = ["очное", "заочное"]

class TEvent():
    def __init__(self,data):
        """
        """
        data = data.split(";")
        self.name = data[1] #название
        self.date = data[2] #дата проведения
        self.level = data[3] #уровень из описания
        x=" ".join(self.name,self.level)
        self.level_of_event = self.detect_level(x)
                                # уровень мероприятия [0 - "школа", 1 - "город", 2 - "регион", 3 - "страна", 4 - "мир"]
        self.type_of_event = self.detect_type1(x)
                                # тип мероприятия [0 - "очное", 1 - "заочное"]
        self.place = data[4] #место проведения
        self.school_class = data[5] #класс ученика на момент проведения события
        self.tutor = data[6] #руководитель
        self.place_of_event = data[7] #результат ученика
        self.description = data[8] #описание
        
        z = self.detect_type2()
        
        print(z)
            
    def detect_level(stroka):
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
        
    def detect_type1(stroka):
        """ форма мероприятия
        """
        type_of_event = 1
        if stroka.lower().find("заочн")!=-1:
            type_of_event = 0
        return type_of_event
    
    def detect_type2(self,data):
        """ тип мероприятия
        """
        # [участие - 0, 3 место - 1, 2 место - 2, 3 место - 3]
        #
        # [олимпиады
        #    [школьный[1,3,3,4],муниципальный[5,7,7,10],региональный[10,12,12,15],заочные_ВСеросс[10,12,12,15],дистанционные[4,6,7,8]],
        #  НПК
        #    [школьный[4,6,6,6],муниципальный[7,15,15,15],региональный[9,20,20,20],Всеросс[18,25,25,25],что_то_еще[0,0,0,0]],
        #  конкурсы / фестивали / интеллектуальные_игры
        #    [школьный[4,6,6,6],муниципальный[5,10,10,10],региональный[6,15,15,15],Всеросс[7,20,20,20],что_то_еще[0,0,0,0],
        #  спорт
        #    [школьный[3,4,4,4],муниципальный[5,10,10,10],региональный[9,15,15,15],что_то_еще[0,0,0,0],что_то_еще[0,0,0,0]]
        #
        types_events = ["олимпиада", "нпк", "конкурс", "спорт"]
        keywords_events = []
        score = []
        # Олимпиада
        buf = ["олимпиада", "чемпионат"]        
        keywords_events.append(buf)
        # НПК
        buf = ["конференция", "чемпионат"]        
        keywords_events.append(buf)
        # Конкурс
        # эстафета пробег турнир первенство соревнование чемпионат 
        buf = ["конкус", "чемпионат"]        
        keywords_events.append(buf)                
        # Спорт
        buf = ["атлетик", "пробег", "шахмат", "акробат", "старт", "спорт"]
        keywords_events.append(buf)
        s = 0
        r = ""
        for i in keywords_events:
            print(i)
            
        
        
        return r
        
        

            
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
        
