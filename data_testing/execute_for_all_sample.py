#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_testing/execute_for_all_sample.py
#

from main_loop.run_all import Run_all
from statistiche.evaluate_results import Evaluate

import csv


class Main:
    use_avg = True
    draw_chart = False
    auto = True
    SENSOR = 1
    DAY = 2

    SENSOR_INTERVAL = (1, 2)
    DAY_INTERVAL = (1,32)

    # quanti intervalli trovare al massimo? diventa più severo sull'allineamento dei picchi
    max_num_intervals = 7  # default 10

    def run(self, file_statistiche, dataset, np_co2, np_tvoc, np_pm25, np_temp, np_humidity, max_disp_small, max_disp_large, n_peaks_for_large_tollerance):

        # quanti picchi per ciascun parametro cercare
        n_peaks_co2_to_find = np_co2
        n_peaks_tvoc_to_find = np_tvoc
        n_peaks_pm25_to_find = np_pm25
        n_peaks_temp_to_find = np_temp
        n_peaks_humidity_to_find = np_humidity

        recall_test = 0
        precision_test = 0
        min_dist_tot = 0
        count_test = 0

        if self.auto:
            for i in range(self.SENSOR_INTERVAL[0], self.SENSOR_INTERVAL[1]):
                SENSOR = i
                for j in range(self.DAY_INTERVAL[0], self.DAY_INTERVAL[1]):
                    DAY = j
                    fi, ri, si, min_dist = Run_all.run(Run_all(), dataset, SENSOR, DAY, self.use_avg, self.draw_chart, n_peaks_co2_to_find, n_peaks_tvoc_to_find, n_peaks_pm25_to_find, n_peaks_temp_to_find, n_peaks_humidity_to_find, self.max_num_intervals, max_disp_small, max_disp_large, n_peaks_for_large_tollerance)  # (flag: use_avg, draw_chart)
                    with open('results.csv', mode='a+') as results_file:
                        results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        results_writer.writerow([fi, ri, si])
                        if (fi, ri, si) != (0, 0, 0):  # scarto eventuali giorni vuoti che farebbero salire la media del test
                            recall_test += Evaluate.recall(Evaluate(), fi, ri, si)
                            precision_test += Evaluate.precision(Evaluate(), fi, ri, si)
                            count_test += 1
                            min_dist_tot += min_dist
            with open('risultati_test/stat{}.txt'.format(file_statistiche), mode='a+') as stat_file:
                stat_writer = csv.writer(stat_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                stat_writer.writerow([n_peaks_co2_to_find, n_peaks_tvoc_to_find, n_peaks_pm25_to_find, n_peaks_temp_to_find,
                                         n_peaks_humidity_to_find, max_disp_small, max_disp_large, n_peaks_for_large_tollerance])
                stat_writer.writerow(["Recall test: {}".format(recall_test/count_test)])
                stat_writer.writerow(["Precision test: {}".format(precision_test/count_test)])
                stat_writer.writerow(["Avg min dist: {}".format(min_dist_tot / count_test)])
                stat_writer.writerow(["---------------------------------------------------"])
        else:
            Run_all.run(Run_all(), dataset, self.SENSOR, self.DAY , self.use_avg, self.draw_chart, n_peaks_co2_to_find, n_peaks_tvoc_to_find, n_peaks_pm25_to_find, n_peaks_temp_to_find, n_peaks_humidity_to_find, self.max_num_intervals, max_disp_small, max_disp_large, n_peaks_for_large_tollerance)  # (flag: use_avg, draw_chart)

        return
