#
#   Author: Mauro Marini
#   Project: tesi
#   File: main_loop/run_all.py
#

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from data_manager import elaborated_data_extractor as ex_data, data_adapter as ad_data
from data_analysis.interval_detector import Interval
from data_analysis.intervals_finder import PredictedInterval
from data_analysis import peaks_detector as pd
from data_testing.intervals_test import Intervals_test
from data_manager.data_prefab import DataPrefab
from params import Params
from confusion_matrix.generate_confusion_matrix import Confusion_matrix

style.use('ggplot')

class Run_all:

    def run(self, dataset, SENSOR, DAY, n_peaks_co2_to_find, n_peaks_tvoc_to_find, n_peaks_pm25_to_find, n_peaks_temp_to_find, n_peaks_humidity_to_find, max_num_intervals, max_small_tollerance, max_large_tollerance, n_peaks_large_tollerance):

        print_curve = Params.print_curve
        print_picchi = Params.print_picchi
        print_picchi_allineati = Params.print_picchi_allineati
        use_incomplete_sample = Params.use_incomplete_sample
        use_avg = Params.use_avg
        draw_chart = Params.draw_chart

        print(
            "----------------------------------------------------------------------\nSENSOR: {}\tDAY: {}\n----------------------------------------------------------------------".format(
                SENSOR, DAY))

        # ---------------------------------------------------------------------------
        #   recupero i dati richiesti
        # ---------------------------------------------------------------------------
        day_data = DataPrefab.get_data_by_sensor_and_day(dataset, SENSOR, DAY)

        n_rilevazioni = len(day_data.datetime)

        if(n_rilevazioni >= 1000 or use_incomplete_sample):

            # ---------------------------------------------------------------------------
            #   cerco e salvo gli intervalli in cui si è cuinato durante una giornata
            # ---------------------------------------------------------------------------
            if Params.use_raw_data:
                pasto_intervals = Interval.detect_interval(Interval(), day_data.datetime, day_data.activity)
            else:
                pasto_intervals = Interval.detect_interval(Interval(), day_data.datetime, day_data.is_pasto)
            print("Intervalli pasto: {}".format(pasto_intervals.interval_list))

            # ---------------------------------------------------------------------------
            #  Le rilevazioni sono più di 1440, quando ci sono tutte ce ne sono 1463,
            #  in alcuni giorni però il sensore ne ha misurate meno (talvolta la metà)
            #  in ogni caso quando ci sono tutte la cardinalità va da 0 a 1440.
            # ---------------------------------------------------------------------------

            # ---------------------------------------------------------------------------
            #  Se non uso i dati grezzi, uso una media
            # ---------------------------------------------------------------------------
            if not Params.use_raw_data:
                if use_avg:
                    co2, tvoc, pm25, temp, humidity = ad_data.make_avg_of_param(day_data)
                else:
                    co2 = day_data.avg_co2_last5min
                    tvoc = day_data.avg_tvoc_last5min
                    pm25 = day_data.avg_pm25_last5min
                    temp = day_data.avg_temperature_last5min
                    humidity = day_data.avg_humidity_last5min
            # ---------------------------------------------------------------------------
            #  Se uso i dati grezzi
            # ---------------------------------------------------------------------------
            else:
                co2 = day_data.co2
                tvoc = day_data.tvoc
                pm25 = day_data.pm25
                temp = day_data.temperature
                humidity = day_data.humidity

            # ---------------------------------------------------------------------------
            #  Trovare picchi co2, tvoc, pm25
            # ---------------------------------------------------------------------------

            peaks_list = []

            co2_peaks = pd.get_peaks(co2, 60, 0.6, 1, n_peaks_co2_to_find)
            tvoc_peaks = pd.get_peaks(tvoc, 60, 0.9, 1, n_peaks_tvoc_to_find)
            pm25_peaks = pd.get_pm25_peaks(pm25, 70, n_peaks_pm25_to_find)
            temp_peaks = pd.get_peaks(temp, 20, 10, 1, n_peaks_temp_to_find)
            humidity_peaks = pd.get_peaks(humidity, 60, [10, 30], 1, n_peaks_humidity_to_find)

            peaks_list= self.add_to_list((self.add_to_list((self.add_to_list((self.add_to_list((self.add_to_list(peaks_list,humidity_peaks)),temp_peaks)), pm25_peaks)), tvoc_peaks)), co2_peaks)
            peaks_list.sort()

            # ---------------------------------------------------------------------------
            #  Raggruppare i picchi dei 3 parametri in intervalli
            # ---------------------------------------------------------------------------
            start_small_tollerance = max_small_tollerance
            start_high_tollerance = max_large_tollerance

            calculated_intervals, calculated_intervals_bin = PredictedInterval.predict_intervals(PredictedInterval(), peaks_list, day_data.datetime, max_num_intervals, start_small_tollerance, start_high_tollerance, n_peaks_large_tollerance)

            # ---------------------------------------------------------------------------
            #   Scrivere la matrice di confusione
            # ---------------------------------------------------------------------------
            if Params.write_confusion_matrix:
                if Params.use_raw_data:
                    confusion_matrix = Confusion_matrix.calculate_confusion_matrix(Confusion_matrix(), day_data.activity, calculated_intervals_bin)
                else:
                    confusion_matrix = Confusion_matrix.calculate_confusion_matrix(Confusion_matrix(), day_data.is_pasto, calculated_intervals_bin)
                params = "PARAMS: {}, {}, {}, {}, {}, {}, {}, {}".format(n_peaks_co2_to_find, n_peaks_tvoc_to_find, n_peaks_pm25_to_find, n_peaks_temp_to_find, n_peaks_humidity_to_find, max_small_tollerance, max_large_tollerance, n_peaks_large_tollerance)
                Confusion_matrix.print_confusion_matrix(confusion_matrix, params)


            # ---------------------------------------------------------------------------
            #  Disegnare grafico
            # ---------------------------------------------------------------------------

            if ((not Params.use_raw_data and len(day_data.datetime) == len(day_data.is_pasto)) or (Params.use_raw_data and len(day_data.datetime) == len(day_data.activity))) and draw_chart:
                plt.title('Sensor: {} | Day: {}'.format(SENSOR, DAY))
                plt.xlabel(' X (time in minutes)')
                plt.ylabel('Y')

                # intervals
                if Params.use_raw_data:
                    plt.plot(day_data.datetime, (ad_data.mul(day_data.activity, 1900)))
                else:
                    plt.plot(day_data.datetime, (ad_data.mul(day_data.is_pasto, 1900)))

                plt.plot(day_data.datetime, (ad_data.mul(calculated_intervals_bin, 1900)))

                # CURVE
                if print_curve:
                    plt.plot(day_data.datetime, co2)
                    plt.plot(day_data.datetime, tvoc)
                    plt.plot(day_data.datetime, pm25)
                    plt.plot(day_data.datetime, ad_data.mul(temp, 20))
                    plt.plot(day_data.datetime, ad_data.mul(humidity, 10))

                # PICCHI
                if print_picchi:
                    plt.plot(co2_peaks, (np.rint(co2))[co2_peaks], "o")
                    plt.plot(tvoc_peaks, (np.rint(tvoc))[tvoc_peaks], "o")
                    plt.plot(pm25_peaks, (np.rint(pm25))[pm25_peaks], "o")
                    plt.plot(temp_peaks, (np.rint(ad_data.mul(temp, 20)))[temp_peaks], "o")
                    plt.plot(humidity_peaks, (np.rint(ad_data.mul(humidity, 10)))[humidity_peaks], "o")

                # PICCHI ALLINEATI IN ALTEZZA PER VEDERE MEGLIO L'ALLINEAMENTO TRA DI ESSI

                allinea = []
                for d in  day_data.datetime:
                    allinea.append(1)

                if print_picchi_allineati:
                    plt.plot(co2_peaks, (np.rint(ad_data.mul(allinea, 750)))[co2_peaks], "o")
                    plt.plot(tvoc_peaks, (np.rint(ad_data.mul(allinea, 700)))[tvoc_peaks], "o")
                    plt.plot(pm25_peaks, (np.rint(ad_data.mul(allinea, 650)))[pm25_peaks], "o")
                    plt.plot(temp_peaks, (np.rint(ad_data.mul(allinea, 600)))[temp_peaks], "o")
                    plt.plot(humidity_peaks, (np.rint(ad_data.mul(allinea, 550)))[humidity_peaks], "o")

                plt.show()

            # ---------------------------------------------------------------------------
            #  Testare il tutto
            # ---------------------------------------------------------------------------

            #test PRECISION -> p è in intervallo_pasto?
            if Params.use_raw_data:
                (fi, ri, si) = Intervals_test.count_intervals_test(Intervals_test(), calculated_intervals_bin, day_data.activity)
            else:
                (fi, ri, si) = Intervals_test.count_intervals_test(Intervals_test(), calculated_intervals_bin, day_data.is_pasto)
            min_dist = Intervals_test.count_avg_min_dist(Intervals_test(), calculated_intervals, pasto_intervals.interval_list)
            return fi, ri, si, min_dist
        return 0, 0, 0, 0


    def add_to_list(self,parent_list, to_append):
        for item in to_append:
            parent_list.append(item)
        return parent_list

