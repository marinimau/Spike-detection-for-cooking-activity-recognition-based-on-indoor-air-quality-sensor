#
#   Author: Mauro Marini
#   Project: tesi
#   File: main.py
#

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
from data_manager import data_extractor as ex_data, data_adapter as ad_data
from data_analysis.interval_detector import Interval

style.use('ggplot')

# ---------------------------------------------------------------------------
#   usare queste costanti per scegliere il campione
# ---------------------------------------------------------------------------
SENSOR=7 # [1-8]
DAY=3
use_avg=True

d = ex_data.DataSet
sensor_data=d.extract_data_from_sensor(ex_data.DataSet(),SENSOR)
day_data=sensor_data.get_data_by_day(DAY)

# ---------------------------------------------------------------------------
#   cerco e salvo gli intervalli in cui si è cuinato durante una giornata
# ---------------------------------------------------------------------------


pasto_intervals=Interval.detect_interval(Interval(),day_data.datetime,day_data.is_pasto)

print("Intervalli pasto: {}".format(pasto_intervals.interval_list))

# ---------------------------------------------------------------------------
#  Le rilevazioni sono più di 1440, quando ci sono tutte ce ne sono 1463,
#  in alcuni giorni però il sensore ne ha misurate meno (talvolta la metà)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
#  Trovare picchi co2, tvoc
# ---------------------------------------------------------------------------

if len(day_data.datetime) == len(day_data.is_pasto):
    plt.title('Sensor: {} | Day: {}'.format(SENSOR,DAY))
    plt.xlabel(' X (time in minutes)')
    plt.ylabel('Y')
    plt.plot(day_data.datetime, (ad_data.mul(day_data.is_pasto, 1900)))

    if use_avg:
        plt.plot(day_data.datetime, ad_data.avg(day_data.avg_co2_last5min, day_data.avg_co2_next5min))
        plt.plot(day_data.datetime, ad_data.avg(day_data.avg_tvoc_last5min, day_data.avg_tvoc_next5min))
        plt.plot(day_data.datetime, ad_data.mul(ad_data.avg(day_data.avg_pm25_last5min, day_data.avg_pm25_next5min),20)) #moltiplico solo per rendere visibili le variazioni nel grafico
    else:
        plt.plot(day_data.datetime, day_data.avg_co2_last5min)
        plt.plot(day_data.datetime, day_data.avg_tvoc_last5min)
        plt.plot(day_data.datetime, ad_data.mul(day_data.avg_pm25_last5min),20) #moltiplico solo per rendere visibili le variazioni nel grafico

    plt.show()


# 1. trovare i picchi di co2, tvoc, pm25
# 2. fare i modo che i picchi non siano mai troppi o troppo pochi
# 3. tracciare un intervallo che raggruppa i picchi dei 3 parametri
# 4. alla fine devo avere da 2 a 5 picchi
#


# peaks,_ = find_peaks((avg_co2_last5min + avg_co2_next5min) / 2, width=6, distance=22, rel_height=0.20)
# temp_peaks, _ = find_peaks(avg_temperature_last5min, width=190, distance=22, rel_height=0.9)


# plt.plot(datetime,avg_temp_n5m*10)
# plt.plot(datetime,avg_co2_l5m)
# plt.plot(datetime,avg_co2_n5m)
# plt.plot(peaks, avg_co2_last5min[peaks], "x")
# plt.plot(temp_peaks, avg_temperature_last5min[temp_peaks] * 10, "+")

# ---------------------------------------------------------------------------
#  Testare il tutto
# ---------------------------------------------------------------------------

# test.run_test(PICCHI_RISULTATO,intervalli_pasto)
#   -test PRECISION -> p is in intervallo_pasto?
#   -test RECAL ogni intervallo_pasto ha p?
#   -test DISTANZA MINIMA
