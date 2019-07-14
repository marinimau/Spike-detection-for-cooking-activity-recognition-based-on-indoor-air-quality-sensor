#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_analysis/interval_finder.py
#

import operator


class PredictedInterval:
    def __init__(self):
        self.interval_list=[]
        return

    def predict_intervals(self, peaks_list, datetime, max_num_intervals, small_tollerance, hight_tollerance , n_peaks_large_tollerance):
        for i in range(len(peaks_list) - 1):
            if abs(peaks_list[i] - peaks_list[i + 1]) < small_tollerance:
                self.interval_list += [(peaks_list[i] - 30, peaks_list[i + 1] + 10)]
            else:
                if self.filterInterval(peaks_list, i,
                                       hight_tollerance) >= n_peaks_large_tollerance and self.get_neighbour_distance(peaks_list[i], self.interval_list, 20):
                    self.interval_list += [(peaks_list[i] - 30, peaks_list[i + 1] + 10)]

            # mergia eventuali intervalli ravvicinati per evitare che che ne vengano contati separatamente
            self.interval_list = self.merge_intervals(self.interval_list)
        if self.count_predicted_intervals(self.interval_list) > max_num_intervals:
            return self.predict_intervals(peaks_list, datetime, max_num_intervals, small_tollerance - 0.5, hight_tollerance - 0.5, n_peaks_large_tollerance)
        else:
            print("Intervalli trovati: {}".format(self.interval_list))
            return self.interval_list, self.convert_to_binary(self.interval_list, datetime)


    def filterInterval(self, peaks_list, position, tollerance):
        counter = 0
        for item in peaks_list:
            if abs(peaks_list[position] - item) <= tollerance:
                counter += 1
        return counter


    def count_predicted_intervals(self, interval_list):
        counter = 0
        open_interval = False

        for i in interval_list:
            if i == 0:
                if open_interval:
                    open_interval = False
                    counter += 1
            else:
                if not open_interval:
                    open_interval = True
        #se esco che ho un intervallo da chiudere
        if open_interval:
            counter += 1
        return counter


    def convert_to_binary(self, intervals, datetime):
        binary_list = []
        find_interval = False

        for minute in datetime:
            for start, end in intervals:
                if minute >= start and minute <= end:
                    binary_list += [1]
                    find_interval = True
                    break
            if not find_interval:
                binary_list += [0]
            find_interval=False
        return binary_list


    def get_neighbour_distance(self, value, intervals, distance):
        for start, end in intervals:
            if not (abs(start - value) < distance and abs(end - value) < distance):
                return False
        return True


    def merge_intervals(self, intervals):
        merged_intervals_raw = []
        merged_intervals = []
        # metto in fila gli elemnti degli intervalli
        for start, end in intervals:
            merged_intervals_raw += [start]
            merged_intervals_raw += [end]
        # li ordino
        merged_intervals_raw.sort()
        merged = merged_intervals_raw.copy()
        # rimuovo eventuali estremi di intervalli vicini
        for i in range(len(merged_intervals_raw) - 1):
            if i % 2 == 1 and (merged_intervals_raw[i+1] - merged_intervals_raw[i] < 20):
                merged.remove(merged_intervals_raw[i])
                merged.remove(merged_intervals_raw[i+1])
        # ricreo le tuple
        for i in range(len(merged) - 1):
            if i % 2 == 0:
                merged_intervals += [(merged[i], merged[i+1])]
        return merged_intervals