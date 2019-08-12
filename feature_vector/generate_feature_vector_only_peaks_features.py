#
#   Author: Mauro Marini
#   Project: tesi
#   feature_vector/generate_feature_vector_only_peaks_features.py
#
from data_manager.data_prefab import DataPrefab
from data_analysis import peaks_detector as pd
from data_manager import data_adapter as ad_data
from data_analysis.find_min_dist import DistFinder
from params import Params
import csv

use_incomplete_sample = Params.use_incomplete_sample

n_peaks_co2_to_find = Params.n_peaks_co2_feature_vector
n_peaks_tvoc_to_find = Params.n_peaks_tvoc_feature_vector
n_peaks_pm25_to_find = Params.n_peaks_pm25_feature_vector
n_peaks_temp_to_find = Params.n_peaks_temp_feature_vector
n_peaks_humidity_to_find = Params.n_peaks_humidity_feature_vector

day_intr = (1, 32)


class PeaksFeatureVectorGenerator:

    def __init__(self, dataset):
        self.dataset = dataset
        return

    def init_csv_file(self, sensor):
        if sensor == 0:
            name = 'feature_vector_results/complete_feature_vector.csv'
        else:
            name = 'training_sets_results/peaks_feature_{}.csv'.format(sensor)
        with open(name, mode='w') as feature_vector_file:
            results_writer = csv.writer(feature_vector_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow(
                ['datetime', 'n_co2_peaks_last5', 'n_co2_peaks_next5', 'n_co2_peaks_last10',
                 'n_co2_peaks_next10', 'n_co2_peaks_last15', 'n_co2_peaks_next15', 'n_co2_peaks_last20',
                 'n_co2_peaks_next20', 'n_co2_peaks_last25', 'n_co2_peaks_next25', 'n_co2_peaks_last30',
                 'n_co2_peaks_next30', 'n_tvoc_peaks_last5', 'n_tvoc_peaks_next5', 'n_tvoc_peaks_last10',
                 'n_tvoc_peaks_next10', 'n_tvoc_peaks_last15', 'n_tvoc_peaks_next15', 'n_tvoc_peaks_last20',
                 'n_tvoc_peaks_next20', 'n_tvoc_peaks_last25', 'n_tvoc_peaks_next25', 'n_tvoc_peaks_last30',
                 'n_tvoc_peaks_next30', 'n_pm25_peaks_last5', 'n_pm25_peaks_next5', 'n_pm25_peaks_last10',
                 'n_pm25_peaks_next10', 'n_pm25_peaks_last15', 'n_pm25_peaks_next15', 'n_pm25_peaks_last20',
                 'n_pm25_peaks_next20', 'n_pm25_peaks_last25', 'n_pm25_peaks_next25', 'n_pm25_peaks_last30',
                 'n_pm25_peaks_next30', 'n_temp_peaks_last5', 'n_temp_peaks_next5', 'n_temp_peaks_last10',
                 'n_temp_peaks_next10', 'n_temp_peaks_last15', 'n_temp_peaks_next15', 'n_temp_peaks_last20',
                 'n_temp_peaks_next20', 'n_temp_peaks_last25', 'n_temp_peaks_next25', 'n_temp_peaks_last30',
                 'n_temp_peaks_next30', 'n_hum_peaks_last5', 'n_hum_peaks_next5', 'n_hum_peaks_last10',
                 'n_hum_peaks_next10', 'n_hum_peaks_last15', 'n_hum_peaks_next15', 'n_hum_peaks_last20',
                 'n_hum_peaks_next20', 'n_hum_peaks_last25', 'n_hum_peaks_next25', 'n_hum_peaks_last30',
                 'n_hum_peaks_next30', 'min_dist_co2', 'min_dist_tvoc',
                 'min_dist_pm25', 'min_dist_temp', 'min_dist_hum', 'pasto'])
        return

    def get_data(self, SENSOR, DAY):
        day_data = DataPrefab.get_data_by_sensor_and_day(self.dataset, SENSOR, DAY)
        n_rilevazioni = len(day_data.datetime)
        if n_rilevazioni >= 1000 or use_incomplete_sample:
            return day_data
        return

    def make_avg(self, data):

        return

    def find_peaks(self, data):
        avg_co2 = data.co2
        avg_tvoc = data.tvoc
        avg_pm25 = data.pm25
        avg_temp = data.temperature
        avg_hum = data.humidity

        if Params.consider_peaks_weight:
            co2_peaks = pd.get_peaks_with_weight(avg_co2, 60, 0.6, 1, n_peaks_co2_to_find)
            tvoc_peaks = pd.get_peaks_with_weight(avg_tvoc, 60, 0.9, 1, n_peaks_tvoc_to_find)
            temp_peaks = pd.get_peaks_with_weight(avg_temp, 20, 10, 1, n_peaks_temp_to_find)
        else:
            co2_peaks = pd.get_peaks(avg_co2, 60, 0.6, 1, n_peaks_co2_to_find)
            tvoc_peaks = pd.get_peaks(avg_tvoc, 60, 0.9, 1, n_peaks_tvoc_to_find)
            temp_peaks = pd.get_peaks(avg_temp, 20, 10, 1, n_peaks_temp_to_find)

        humidity_peaks = pd.get_peaks(avg_hum, 60, [10, 30], 1, n_peaks_humidity_to_find)
        pm25_peaks = pd.get_pm25_peaks(avg_pm25, 70, n_peaks_pm25_to_find)
        return co2_peaks, tvoc_peaks, pm25_peaks, temp_peaks, humidity_peaks

    def find_peak_using_intervals(self, data):
        avg_co2 = data.co2
        avg_tvoc = data.tvoc
        avg_pm25 = data.pm25
        avg_temp = data.temperature
        avg_hum = data.humidity

        co2_peaks = []
        tvoc_peaks = []
        pm25_peaks = []
        temp_peaks = []
        hum_peaks = []

        # considera solo 3: colazione, pranzo e cena, anziché l'intera giornata
        co2_intervals = pd.split_intervals(avg_co2, data.datetime)
        tvoc_intervals = pd.split_intervals(avg_tvoc, data.datetime)
        pm25_intervals = pd.split_intervals(avg_pm25, data.datetime)
        temp_intervals = pd.split_intervals(avg_temp, data.datetime)
        hum_intervals = pd.split_intervals(avg_hum, data.datetime)

        # per ogni parametro e per ogni intervallo, trova i picchi e concatena
        for i in range(3):
            if Params.consider_peaks_weight:
                co2_peaks += pd.get_peaks_with_weight(co2_intervals[i], 1, 1, 1, Params.n_peaks_co2_by_interval[i])
                tvoc_peaks += pd.get_peaks_with_weight(tvoc_intervals[i], 1, 1, 1,
                                                       Params.n_peaks_tvoc_by_interval[i])
                temp_peaks += pd.get_peaks_with_weight(temp_intervals[i], 1, 1, 1, Params.n_peaks_temp_by_interval[i])
                hum_peaks += pd.get_peaks_with_weight(hum_intervals[i], 1, 1, 1,
                                                      Params.n_peaks_humidity_by_interval[i])
                pm25_peaks += pd.get_peaks_with_weight(pm25_intervals[i], 1, 1, 1, Params.n_peaks_pm25_by_interval[i])
            else:
                co2_peaks += pd.get_peaks(co2_intervals[i], 1, 0.6, 1, Params.n_peaks_co2_by_interval[i])  # DEFAULT 1. 0.6, 1
                tvoc_peaks += pd.get_peaks(tvoc_intervals[i], 1, 0.9, 1, Params.n_peaks_tvoc_by_interval[i]) # DEFAULT  1, 0.9. 1
                temp_peaks += pd.get_peaks(temp_intervals[i], 1, 10, 1, Params.n_peaks_temp_by_interval[i]) # DEFAULT  1, 10. 1
                hum_peaks += pd.get_peaks(hum_intervals[i], 1, 1, 1,
                                          Params.n_peaks_humidity_by_interval[i])  # DEFAULT  1, 1, 1
                pm25_peaks += pd.get_peaks(pm25_intervals[i], 10, 1, 1, Params.n_peaks_pm25_by_interval[i]) # DEFAULT  10, 1. 1
        return co2_peaks, tvoc_peaks, pm25_peaks, temp_peaks, hum_peaks

    def count_peaks_in_inteval(self, peaks, minute, interval):
        counter_last = 0
        counter_next = 0

        for p in peaks:
            if minute - interval <= p <= minute:
                counter_last += 1
            if minute <= p <= minute + interval:
                counter_next += 1
        return counter_last, counter_next

    def get_pasto_by_minute(self, day_data, minute):
        counter = 0
        for i in range(len(day_data.datetime)-1):
            if day_data.datetime[i] == minute:
                break
            counter += 1
        # scelgo se usare tutte le attività o solo quelle che includono un fornello
        if Params.use_only_cooker_actvity:
            pasto = day_data.fornello
        else:
            pasto = day_data.activity
        if pasto[counter] == 0:
            return 'N'
        else:
            return 'Y'

    def print_feature(self, sensor, co2_p, tvoc_p, pm25_p, temp_p, hum_p, day_data):
        for i in range(len(day_data.datetime)):
            # conto i picchi di co2 nei vari intervalli
            co2_count_last5, co2_count_next5 = self.count_peaks_in_inteval(co2_p, day_data.datetime[i], 5)
            co2_count_last10, co2_count_next10 = self.count_peaks_in_inteval(co2_p, day_data.datetime[i], 10)
            co2_count_last15, co2_count_next15 = self.count_peaks_in_inteval(co2_p, day_data.datetime[i], 15)
            co2_count_last20, co2_count_next20 = self.count_peaks_in_inteval(co2_p, day_data.datetime[i], 20)
            co2_count_last25, co2_count_next25 = self.count_peaks_in_inteval(co2_p, day_data.datetime[i], 25)
            co2_count_last30, co2_count_next30 = self.count_peaks_in_inteval(co2_p, day_data.datetime[i], 30)

            tvoc_count_last5, tvoc_count_next5 = self.count_peaks_in_inteval(tvoc_p, day_data.datetime[i], 5)
            tvoc_count_last10, tvoc_count_next10 = self.count_peaks_in_inteval(tvoc_p, day_data.datetime[i], 10)
            tvoc_count_last15, tvoc_count_next15 = self.count_peaks_in_inteval(tvoc_p, day_data.datetime[i], 15)
            tvoc_count_last20, tvoc_count_next20 = self.count_peaks_in_inteval(tvoc_p, day_data.datetime[i], 20)
            tvoc_count_last25, tvoc_count_next25 = self.count_peaks_in_inteval(tvoc_p, day_data.datetime[i], 25)
            tvoc_count_last30, tvoc_count_next30 = self.count_peaks_in_inteval(tvoc_p, day_data.datetime[i], 30)

            pm25_count_last5, pm25_count_next5 = self.count_peaks_in_inteval(pm25_p, day_data.datetime[i], 5)
            pm25_count_last10, pm25_count_next10 = self.count_peaks_in_inteval(pm25_p, day_data.datetime[i], 10)
            pm25_count_last15, pm25_count_next15 = self.count_peaks_in_inteval(pm25_p, day_data.datetime[i], 15)
            pm25_count_last20, pm25_count_next20 = self.count_peaks_in_inteval(pm25_p, day_data.datetime[i], 20)
            pm25_count_last25, pm25_count_next25 = self.count_peaks_in_inteval(pm25_p, day_data.datetime[i], 25)
            pm25_count_last30, pm25_count_next30 = self.count_peaks_in_inteval(pm25_p, day_data.datetime[i], 30)

            temp_count_last5, temp_count_next5 = self.count_peaks_in_inteval(temp_p, day_data.datetime[i], 5)
            temp_count_last10, temp_count_next10 = self.count_peaks_in_inteval(temp_p, day_data.datetime[i], 10)
            temp_count_last15, temp_count_next15 = self.count_peaks_in_inteval(temp_p, day_data.datetime[i], 15)
            temp_count_last20, temp_count_next20 = self.count_peaks_in_inteval(temp_p, day_data.datetime[i], 20)
            temp_count_last25, temp_count_next25 = self.count_peaks_in_inteval(temp_p, day_data.datetime[i], 25)
            temp_count_last30, temp_count_next30 = self.count_peaks_in_inteval(temp_p, day_data.datetime[i], 30)

            hum_count_last5, hum_count_next5 = self.count_peaks_in_inteval(hum_p, day_data.datetime[i], 5)
            hum_count_last10, hum_count_next10 = self.count_peaks_in_inteval(hum_p, day_data.datetime[i], 10)
            hum_count_last15, hum_count_next15 = self.count_peaks_in_inteval(hum_p, day_data.datetime[i], 15)
            hum_count_last20, hum_count_next20 = self.count_peaks_in_inteval(hum_p, day_data.datetime[i], 20)
            hum_count_last25, hum_count_next25 = self.count_peaks_in_inteval(hum_p, day_data.datetime[i], 25)
            hum_count_last30, hum_count_next30 = self.count_peaks_in_inteval(hum_p, day_data.datetime[i], 30)

            min_dist_co2, min_dist_tvoc, min_dist_pm25, min_dist_temp, min_dist_hum = DistFinder.evaluate_dist(
                DistFinder(), day_data.datetime[i], co2_p, tvoc_p, pm25_p, temp_p, hum_p)

            pasto = self.get_pasto_by_minute(day_data, day_data.datetime[i])

            with open('feature_vector_results/complete_feature_vector.csv', mode='a+') as feature_vector_file:
                results_writer = csv.writer(feature_vector_file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                results_writer.writerow(
                    [day_data.datetime[i], co2_count_last5, co2_count_next5,
                     co2_count_last10, co2_count_next10,
                     co2_count_last15, co2_count_next15, co2_count_last20, co2_count_next20, co2_count_last25,
                     co2_count_next25, co2_count_last30, co2_count_next30, tvoc_count_last5, tvoc_count_next5,
                     tvoc_count_last10, tvoc_count_next10, tvoc_count_last15, tvoc_count_next15, tvoc_count_last20,
                     tvoc_count_next20, tvoc_count_last25, tvoc_count_next25, tvoc_count_last30, tvoc_count_next30,
                     pm25_count_last5, pm25_count_next5, pm25_count_last10, pm25_count_next10, pm25_count_last15,
                     pm25_count_next15, pm25_count_last20, pm25_count_next20, pm25_count_last25, pm25_count_next25,
                     pm25_count_last30, pm25_count_next30, temp_count_last5, temp_count_next5, temp_count_last10,
                     temp_count_next10, temp_count_last15, temp_count_next15, temp_count_last20, temp_count_next20,
                     temp_count_last25, temp_count_next25, temp_count_last30, temp_count_next30, hum_count_last5,
                     hum_count_next5, hum_count_last10, hum_count_next10, hum_count_last15, hum_count_next15,
                     hum_count_last20, hum_count_next20, hum_count_last25, hum_count_next25, hum_count_last30,
                     hum_count_next30, min_dist_co2, min_dist_tvoc,
                     min_dist_pm25, min_dist_temp, min_dist_hum, pasto])
                feature_vector_file.close()

            with open('training_sets_results/peaks_feature_{}.csv'.format(sensor), mode='a+') as single_feature_vector_file:
                results_writer = csv.writer(single_feature_vector_file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                results_writer.writerow(
                    [day_data.datetime[i], co2_count_last5, co2_count_next5,
                     co2_count_last10, co2_count_next10,
                     co2_count_last15, co2_count_next15, co2_count_last20, co2_count_next20, co2_count_last25,
                     co2_count_next25, co2_count_last30, co2_count_next30, tvoc_count_last5, tvoc_count_next5,
                     tvoc_count_last10, tvoc_count_next10, tvoc_count_last15, tvoc_count_next15, tvoc_count_last20,
                     tvoc_count_next20, tvoc_count_last25, tvoc_count_next25, tvoc_count_last30, tvoc_count_next30,
                     pm25_count_last5, pm25_count_next5, pm25_count_last10, pm25_count_next10, pm25_count_last15,
                     pm25_count_next15, pm25_count_last20, pm25_count_next20, pm25_count_last25, pm25_count_next25,
                     pm25_count_last30, pm25_count_next30, temp_count_last5, temp_count_next5, temp_count_last10,
                     temp_count_next10, temp_count_last15, temp_count_next15, temp_count_last20, temp_count_next20,
                     temp_count_last25, temp_count_next25, temp_count_last30, temp_count_next30, hum_count_last5,
                     hum_count_next5, hum_count_last10, hum_count_next10, hum_count_last15, hum_count_next15,
                     hum_count_last20, hum_count_next20, hum_count_last25, hum_count_next25, hum_count_last30,
                     hum_count_next30, min_dist_co2, min_dist_tvoc,
                     min_dist_pm25, min_dist_temp, min_dist_hum, pasto])
                single_feature_vector_file.close()

        return

    def convert_peaks(self, datetime, co2_p, tvoc_p, pm25_p, temp_p, hum_p):
        return self.do_convert(datetime, co2_p), self.do_convert(datetime, tvoc_p), self.do_convert(datetime, pm25_p), self.do_convert(datetime, temp_p), self.do_convert(datetime, hum_p)

    def do_convert(self, datetime, peaks):
        converted_peaks = []
        for p in peaks:
            converted_peaks.append(datetime[p])
        return converted_peaks

    def generate(self):
        self.init_csv_file(0)
        for sensor in Params.SENSOR_list:
            self.init_csv_file(sensor)
            for day in range(Params.DAY_intr[0], Params.DAY_intr[1]):
                day_data = self.get_data(sensor, day)
                if not day_data is None:
                    # recupero i picchi
                    if Params.find_peaks_by_intervals:
                        co2_p, tvoc_p, pm25_p, temp_p, hum_p = self.find_peak_using_intervals(day_data)
                    else:
                        co2_p, tvoc_p, pm25_p, temp_p, hum_p = self.find_peaks(day_data)
                    converted_co2, converted_tvoc, converted_pm25, converted_temp, converted_hum = self.convert_peaks(day_data.datetime, co2_p, tvoc_p, pm25_p, temp_p, hum_p)
                    self.print_feature(sensor, converted_co2, converted_tvoc, converted_pm25, converted_temp, converted_hum, day_data)
        return
