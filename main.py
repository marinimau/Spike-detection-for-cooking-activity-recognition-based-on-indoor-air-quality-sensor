from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

style.use('ggplot')

# I take the data from a csv file that contains (for one day only):
# -timestamps,
# -avg_co2_last_5_min
# -class (integer)
minute,avg_co2, isPasto= np.loadtxt('file/day1_co2_pasto.csv', unpack=True, delimiter=',')

peaks, _ = find_peaks(avg_co2, width=2, rel_height=0.4)

plt.title('Prova')
plt.xlabel('time (n° of minutes)')
plt.ylabel('avg co2 ')

plt.plot(minute,isPasto,avg_co2)
plt.plot(peaks, avg_co2[peaks], "x")
plt.show()

