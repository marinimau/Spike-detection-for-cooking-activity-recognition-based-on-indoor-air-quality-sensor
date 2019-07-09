#
#   Author: Mauro Marini
#   Project: tesi
#   File: main/run_all.py
#

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from data_manager import data_extractor as ex_data, data_adapter as ad_data
from data_analysis.interval_detector import Interval
from data_analysis import peaks_detector as pd
from data_testing.intervals_test import Intervals_test

style.use('ggplot')

class Run_all:

    def run(self, SENSOR, DAY, use_avg, draw_chart, n_peaks_co2_to_find, n_peaks_tvoc_to_find, n_peaks_pm25_to_find, n_peaks_temp_to_find, n_peaks_humidity_to_find, max_num_intervals):

        print(
            "----------------------------------------------------------------------\nSENSOR: {}\tDAY: {}\n----------------------------------------------------------------------".format(
                SENSOR, DAY))

        # ---------------------------------------------------------------------------
        #   recupero i dati richiesti
        # ---------------------------------------------------------------------------

        d = ex_data.DataSet
        sensor_data = d.extract_data_from_sensor(ex_data.DataSet(), SENSOR)
        day_data = sensor_data.get_data_by_day(DAY)

        # ---------------------------------------------------------------------------
        #   cerco e salvo gli intervalli in cui si è cuinato durante una giornata
        # ---------------------------------------------------------------------------

        pasto_intervals = Interval.detect_interval(Interval(), day_data.datetime, day_data.is_pasto)
        print("Intervalli pasto: {}".format(pasto_intervals.interval_list))

        # ---------------------------------------------------------------------------
        #  Le rilevazioni sono più di 1440, quando ci sono tutte ce ne sono 1463,
        #  in alcuni giorni però il sensore ne ha misurate meno (talvolta la metà)
        #  in ogni caso quando ci sono tutte la cardinalità va da 0 a 1440.
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        #  settare le variabili
        # ---------------------------------------------------------------------------

        if use_avg:
            co2 = ad_data.avg(day_data.avg_co2_last5min, day_data.avg_co2_next5min)
            tvoc = ad_data.avg(day_data.avg_tvoc_last5min, day_data.avg_tvoc_next5min)
            pm25 = ad_data.avg(day_data.avg_pm25_last5min, day_data.avg_pm25_next5min)
            temp = ad_data.avg(day_data.avg_temperature_last5min, day_data.avg_temperature_next5min)
            humidity = ad_data.avg(day_data.avg_humidity_last5min, day_data.avg_humidity_next5min)
        else:
            co2 = day_data.avg_co2_last5min
            tvoc = day_data.avg_tvoc_last5min
            pm25 = day_data.avg_pm25_last5min
            temp = day_data.avg_temperature_last5min
            humidity = day_data.avg_humidity_last5min

        # ---------------------------------------------------------------------------
        #  Trovare picchi co2, tvoc, pm25
        # ---------------------------------------------------------------------------

        co2_peaks = pd.get_peaks(co2, 0, n_peaks_co2_to_find)
        tvoc_peaks = pd.get_peaks(tvoc, 0, n_peaks_tvoc_to_find)
        pm25_peaks = pd.get_peaks(pm25, 0, n_peaks_pm25_to_find)
        temp_peaks = pd.get_peaks(temp, 0, n_peaks_temp_to_find)
        humidity_peaks = pd.get_peaks(humidity, 0, n_peaks_humidity_to_find)

        # ---------------------------------------------------------------------------
        #  Raggruppare i picchi dei 3 parametri in intervalli
        # ---------------------------------------------------------------------------

        calculated_intervals = Interval.calculate_intervals(Interval(), day_data.datetime, co2_peaks, tvoc_peaks,
                                                            pm25_peaks, max_num_intervals)

        # get_peaks prende dati, priminenza iniziale, e numero di picchi da trovare,
        # agisce sul valore della prominenza per trovarne il numero richiesto.

        # ---------------------------------------------------------------------------
        #  Disegnare grafico
        # ---------------------------------------------------------------------------

        if len(day_data.datetime) == len(day_data.is_pasto) and draw_chart:
            plt.title('Sensor: {} | Day: {}'.format(SENSOR, DAY))
            plt.xlabel(' X (time in minutes)')
            plt.ylabel('Y')

            # intervals
            plt.plot(day_data.datetime, (ad_data.mul(day_data.is_pasto, 1900)))
            plt.plot(day_data.datetime, (ad_data.mul(calculated_intervals, 1900)))

            # CURVE
            plt.plot(day_data.datetime, co2)
            plt.plot(day_data.datetime, tvoc)
            plt.plot(day_data.datetime, ad_data.mul(pm25, 20))  # moltiplico solo per rendere visibili le variazioni nel grafico
            plt.plot(day_data.datetime, ad_data.mul(temp, 20))
            plt.plot(day_data.datetime, humidity)

            # PICCHI
            plt.plot(co2_peaks, (np.rint(co2))[co2_peaks], "o")
            plt.plot(tvoc_peaks, (np.rint(tvoc))[tvoc_peaks], "o")
            plt.plot(pm25_peaks, (np.rint(ad_data.mul(pm25, 20)))[pm25_peaks], "o")
            plt.plot(temp_peaks, (np.rint(ad_data.mul(temp, 20)))[temp_peaks], "o")
            plt.plot(humidity_peaks, (np.rint(humidity))[humidity_peaks], "o")

            plt.show()

        # ---------------------------------------------------------------------------
        #  Testare il tutto
        # ---------------------------------------------------------------------------

        # test PRECISION -> p is in intervallo_pasto?
        (fi, ri, si) = Intervals_test.precision_test(Intervals_test(), calculated_intervals, day_data.is_pasto)
        print("Precision test (founded_intr:  {}, real_intr: {}, satisfied_founded_intr: {})".format(fi, ri, si))

        #  test RECAL ogni intervallo_pasto ha p?
        (ri, fi, si) = Intervals_test.recall_test(Intervals_test(), calculated_intervals, day_data.is_pasto)
        print("Recall test (real_intr:  {}, founded_intr: {}, satisfied_real_intr: {})".format(ri, fi, si))
        #   -test DISTANZA MINIMA




