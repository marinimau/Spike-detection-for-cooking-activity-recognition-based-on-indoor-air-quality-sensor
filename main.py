#
#   Author: Mauro Marini
#   Project: tesi
#   File: main.py
#

from main.run_all import Run_all

auto = True
SENSOR = 1
DAY = 200

SENSOR_INTERVAL = (1,7)
DAY_INTERVAL = (2,10)

# quanti picchi per ciascun parametro cercare
n_peaks_co2_to_find = 9   # default 7
n_peaks_tvoc_to_find = 5    # default 7
n_peaks_pm25_to_find = 4  # default 7

# quanti intervalli trovare al massimo? diventa più severo sull'allineamento dei picchi
max_num_intervals = 8  # default 10

if auto:
    for i in range(SENSOR_INTERVAL[0], SENSOR_INTERVAL[1]):
        SENSOR = i
        for j in range(DAY_INTERVAL[0], DAY_INTERVAL[1]):
            DAY = j
            Run_all.run(Run_all(), SENSOR, DAY , True, True, n_peaks_co2_to_find, n_peaks_tvoc_to_find, n_peaks_pm25_to_find, max_num_intervals)  # (flag: use_avg, draw_chart)
else:
    Run_all.run(Run_all(), SENSOR, DAY , True, True, n_peaks_co2_to_find, n_peaks_tvoc_to_find, n_peaks_pm25_to_find, max_num_intervals)  # (flag: use_avg, draw_chart)

