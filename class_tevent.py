#-*- coding: utf-8 -*-

# Класс, который описывает событие


#level_of_event = ["школа", "город", "регион", "страна", "мир"]
#type_of_event = ["очное", "заочное"]

class TEvent():
        def detect_level(stroka):
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
        def detect_type(stroka):
            type_of_event = 1
            if stroka.lower().find("заочн")!=-1:
                type_of_event = 0
            return type_of_event
        def __init__(self,data):
                self.name = data[0] #название
                self.date = data[1] #дата проведения
                self.level = data[2] #уровень из описания
                x=" ".join(self.name,self.level)
                self.level_of_event = self.detect_level(x)
                                        # уровень мероприятия [0 - "школа", 1 - "город", 2 - "регион", 3 - "страна", 4 - "мир"]
                self.type_of_event = self.detect_type(x)
                                        # тип мероприятия [0 - "очное", 1 - "заочное"]
                self.place = data[3] #место проведения
                self.school_class = data[4] #класс ученика на момент проведения события
                self.tutor = data[5] #руководитель
                self.place_of_event = data[6] #результат ученика
                self.description = data[7] #описание
        def __str__(self):
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
        
def main():
    data = ["Конкурс по математике «Эврика 3-4 класс»","20.12.2013","Всероссийский открытый заочный конкурс «Интеллект-экспресс»","Мурманск",3,"Малахова Елена Геннадьевна","Диплом за 2 место"]
    event=TEvent(data)
    print(event)

main()


        
