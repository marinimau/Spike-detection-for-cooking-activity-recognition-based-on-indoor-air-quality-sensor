'''
    Author: Mauro Marini
    Project: tesi
    File: data_analysis/interval_detector.py
'''

class Interval:
    def __init__(self):
        self.interval_list=[]
        return

    #data una lista di datetime e una di pasti (combacianti) rileva e restituisce gli intervalli
    def detect_interval(self,datetime,pasto):

        open_interval=False
        startInterval=0
        endInterval=0
        minutes=0

        for p in pasto:
            if pasto[minutes]>0:
                if not open_interval:
                    open_interval=True
                    startInterval=datetime[minutes]
                endInterval=datetime[minutes]

            if not pasto[minutes]==1.0 and pasto[minutes-1] == 1.0: #se siamo appena usciti da un intervallo salvo nella lista
                self.interval_list.append([(startInterval,endInterval)])
                open_interval=False
            minutes +=1
        return self

