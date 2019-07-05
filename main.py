from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
from data_manager import extact_data as ex_data



d = ex_data.DataSet
c=d.extract_data_from_sensor(ex_data.DataSet(),1)

#  Le rilevazioni sono più di 1440, quando ci sono tutte ce ne sono 1463, in alcuni giorni però il sensore ne ha misurate meno (talvolta la metà)
e=c.get_data_by_day(2)

style.use('ggplot')


#peaks, _ = find_peaks((avg_co2_last5min + avg_co2_next5min) / 2, width=6, distance=22, rel_height=0.20)
#temp_peaks, _ = find_peaks(avg_temperature_last5min, width=190, distance=22, rel_height=0.9)

plt.title('Prova')
plt.xlabel(' X (time in n° of minutes)')
plt.ylabel('Y')

plt.plot(c.datetime, c.is_pasto * 350)
# plt.plot(datetime,avg_temp_n5m*10)
# plt.plot(datetime,avg_co2_l5m)
# plt.plot(datetime,avg_co2_n5m)
#plt.plot(peaks, avg_co2_last5min[peaks], "x")
#plt.plot(temp_peaks, avg_temperature_last5min[temp_peaks] * 10, "+")
plt.show()
