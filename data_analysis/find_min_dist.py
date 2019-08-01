#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_analysis/dist_finder.py
#

from params import Params

class DistFinder:

    def evaluate_dist(self, current_min, co2_peaks, tvoc_peaks, pm25_peaks, temp_peaks, hum_peaks):
        co2_dist = self.find_dist(current_min, co2_peaks)
        tvoc_dist = self.find_dist(current_min, tvoc_peaks)
        pm25_dist = self.find_dist(current_min, pm25_peaks)
        temp_dist = self.find_dist(current_min, temp_peaks)
        hum_dist = self.find_dist(current_min, hum_peaks)
        return co2_dist, tvoc_dist, pm25_dist, temp_dist, hum_dist

    def find_dist(self, current_min, peaks):
        dist = 10000000
        for p in peaks:
            if abs(current_min - p) <= abs(dist):
                dist = current_min - p
        return dist