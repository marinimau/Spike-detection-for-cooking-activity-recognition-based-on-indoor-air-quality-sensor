#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_analysis/interval_detector.py
#

import operator

class Interval:
    def __init__(self):
        self.interval_list=[]
        return

    # data una lista di datetime e una di pasti rileva e restituisce gli intervalli
    def detect_interval(self,datetime,pasto):

        open_interval=False
        startInterval=0
        endInterval=0
        minutes=0

        for p in pasto:
            if pasto[minutes] > 0 :
                if not open_interval:
                    open_interval=True
                    startInterval=datetime[minutes]
                endInterval=datetime[minutes]

            if not pasto[minutes]==1.0 and pasto[minutes-1] == 1.0: #se siamo appena usciti da un intervallo salvo nella lista
                self.interval_list.append([(startInterval,endInterval)])
                open_interval=False
            minutes +=1
        return self


    # calcola n intervalli dati i picchi trovati
    def calculate_intervals(self, datetime, co2_peaks, tvoc_peaks, pm25_peaks, temp_peaks, humidity_peaks, max_num_intervals):

        #cerca per co2
        co2_intervals=self.calculate_interval_for_param(co2_peaks, tvoc_peaks, pm25_peaks)
        #cerca per tvoc
        tvoc_intervals = self.calculate_interval_for_param(tvoc_peaks, co2_peaks, pm25_peaks)
        #cerca per pm25
        pm25_intervals = self.calculate_interval_for_param(pm25_peaks, co2_peaks, tvoc_peaks)

        #fai una media degli intervalli trovati
        results_raw = self.calculate_results(((co2_intervals.interval_list) + (tvoc_intervals.interval_list) + (pm25_intervals.interval_list)), 30, 50, max_num_intervals)

        results = self.convert_intervals(results_raw, datetime)

        return results


    # dato un gruppo di picchi di un parametro (che può essere co2, tvoc o pm25)
    # cerca gli intervalli minimi che includono: un punto per ogni parametro.
    def calculate_interval_for_param(self, param1_peaks, param2_peaks, param3_peaks):
        param1_intervals = Interval()
        for param1_p in param1_peaks:
            min_interval_for_point = (0,0)
            current_interval_size = 1440
            for param2_p in param2_peaks:
                for param3_p in param3_peaks:
                    # ordina i punti trovati
                    sorted_points = [param1_p, param2_p, param3_p]
                    sorted_points.sort()
                    #genera intervallo
                    if sorted_points[2]-sorted_points[0] < current_interval_size:
                        min_interval_for_point = (sorted_points[0], sorted_points[1], sorted_points[2])
                        current_interval_size = sorted_points[2] - sorted_points[0]
            param1_intervals.interval_list.append(min_interval_for_point)
        return param1_intervals


    # calcola degli intervalli che sono una media tra quelli vicini e restituisce n intervalli.
    def calculate_results(self,all_intervals, max_disp, max_disp_large, max_num_intervals):

        results=Interval()

        # riordinare gli intervalli in input
        all_intervals.sort(key=operator.itemgetter(1))

        for fst, mdl, lst in all_intervals:
            if abs(fst - mdl) < max_disp:
                results.interval_list.append((fst-20,fst,mdl))
            if abs(fst - lst) < max_disp:
                results.interval_list.append((fst-20,fst,lst))
            if abs(mdl - lst) < max_disp:
                results.interval_list.append((mdl-20, mdl, lst))
            if abs(fst-mdl) < max_disp_large and abs(mdl-lst) < max_disp_large:
                results.interval_list.append((fst-10, mdl, lst+10))

        if len(results.interval_list) > max_num_intervals:
            return self.calculate_results(all_intervals,max_disp-1, max_disp_large-1, max_num_intervals)

        return results.interval_list


    #return binary list given intervals
    def convert_intervals(self, intervals, datetime):

        #creo una lista pulita di zeri della grandezza di datetime
        binary_results = [0] * len(datetime)

        for i in range(len(binary_results)):
            for fst, mdl, lst in intervals:
                if fst <= i <= lst:
                    binary_results[i] = 1
                    break

        return binary_results
