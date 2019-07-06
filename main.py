'''
    Author: Mauro Marini
    Project: tesi
    File: main.py
'''

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
from data_manager import data_extractor as ex_data, data_adapter as ad_data
from data_analysis.interval_detector import Interval

style.use('ggplot')

#---------------------------------------------------------------------------
#   usare queste costanti per scegliere il campione
#---------------------------------------------------------------------------
SENSOR=4
DAY=6

d = ex_data.DataSet
sensor_data=d.extract_data_from_sensor(ex_data.DataSet(),SENSOR)
day_data=sensor_data.get_data_by_day(DAY)

#---------------------------------------------------------------------------
#   cerco e salvo gli intervalli in cui si è cuinato durante una giornata
#---------------------------------------------------------------------------


pasto_intervals=Interval.detect_interval(Interval(),day_data.datetime,day_data.is_pasto)

print("Intervalli pasto: {}".format(pasto_intervals.interval_list))

#---------------------------------------------------------------------------
#  Le rilevazioni sono più di 1440, quando ci sono tutte ce ne sono 1463,
#  in alcuni giorni però il sensore ne ha misurate meno (talvolta la metà)
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#  Trovare picchi co2 e tvoc
#---------------------------------------------------------------------------

#co2_peaks, _ = find_peaks(day_data.avg_co2_last5min, width=6, distance=22, rel_height=0.20)
#temp_peaks, _ = find_peaks(avg_temperature_last5min, width=190, distance=22, rel_height=0.9)

if len(day_data.datetime) == len(day_data.is_pasto):
    plt.title('Prova')
    plt.xlabel(' X (time in minutes)')
    plt.ylabel('Y')
    plt.plot(day_data.datetime, (ad_data.mul(day_data.is_pasto, 1900)))
    plt.plot(day_data.datetime, day_data.avg_co2_last5min)
    plt.plot(day_data.datetime, day_data.avg_tvoc_last5min)

    #stampo i picchi
    #plt.plot(co2_peaks, day_data.avg_co2_last5min[co2_peaks], "x")
    plt.show()



#peaks, _ = find_peaks((avg_co2_last5min + avg_co2_next5min) / 2, width=6, distance=22, rel_height=0.20)
#temp_peaks, _ = find_peaks(avg_temperature_last5min, width=190, distance=22, rel_height=0.9)




# plt.plot(datetime,avg_temp_n5m*10)
# plt.plot(datetime,avg_co2_l5m)
# plt.plot(datetime,avg_co2_n5m)
#plt.plot(peaks, avg_co2_last5min[peaks], "x")
#plt.plot(temp_peaks, avg_temperature_last5min[temp_peaks] * 10, "+")

