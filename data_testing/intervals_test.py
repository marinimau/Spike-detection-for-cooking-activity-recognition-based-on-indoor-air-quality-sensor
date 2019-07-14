#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_testing/intervals_test.py
#

class Intervals_test:

    # per ogni intervallo trovato controllo se contiene un intervallo reale
    def count_intervals_test(self, found_intervals, real_intervals):

        open_intr = False
        satisfied_intr = False
        satisfied_intr_count = 0

        for i in range(len(found_intervals)):
            if found_intervals[i] == 1:
                # se ho letto il primo 1 apro l'intervallo
                if not open_intr:
                    open_intr = True
                # se ho un intervallo reale dentro quello trovato
                if real_intervals[i] == 1 and not satisfied_intr:
                    satisfied_intr = True
                    satisfied_intr_count +=1
            else:
                # chiudo l'intervallo al primo zero che leggo
                if open_intr:
                    open_intr = False
                    satisfied_intr = False
        return self.calc_n_intervals(found_intervals), self.calc_n_intervals(real_intervals), satisfied_intr_count


    # calcola il numero di intervalli partndo dalla lista binaria
    def calc_n_intervals(self, intervals):
        open_intr = False
        intr_count = 0

        for intr in intervals:
            if intr == 1:
                # se sono appena entrato
                if not open_intr:
                    open_intr = True
                    intr_count += 1
            else:
                # se sono appena uscito
                if open_intr:
                    open_intr = False
        return intr_count


    def count_avg_min_dist(self, found_intervals, real_intervals):
        print("real intervals: {}".format(real_intervals))
        min_dist_tot = 0
        min_dist = 0
        found_intervals_count = len(found_intervals) # in questo caso non uso il formato binario e posso usare len
        if found_intervals_count == 0:
            return 0
        for start_found, end_found in found_intervals:
            min_dist=1440
            for start_real, end_real in real_intervals:
                if not(start_found <= start_real <= end_found or start_found <= start_real <= end_found): # se gli intervalli non si incontrano
                    #calcolo la distanza minima
                    if abs(start_real - end_found) < abs(start_found - end_real):
                        if min_dist > abs(start_real - end_found):
                            min_dist = abs(start_real - end_found)
                    else:
                        if min_dist > abs(start_found - end_real):
                            min_dist = abs(start_found - end_real)
                else: # se gli intervalli si incrociano in almeno un punto
                    min_dist = 0
                    break
            min_dist_tot += min_dist
        if min_dist_tot == 0:
            return 0
        return min_dist_tot / found_intervals_count