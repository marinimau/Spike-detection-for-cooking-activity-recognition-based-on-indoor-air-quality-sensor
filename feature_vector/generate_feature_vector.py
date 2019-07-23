#
#   Author: Mauro Marini
#   Project: tesi
#   feature_vector/generate_feature_vector.py
#
from data_manager.data_prefab import DataPrefab
from data_analysis import peaks_detector as pd
from data_manager import data_adapter as ad_data
from params import Params
import csv

use_incomplete_sample = True

n_peaks_co2_to_find = Params.n_peaks_co2_feature_vector
n_peaks_tvoc_to_find = Params.n_peaks_tvoc_feature_vector
n_peaks_pm25_to_find = Params.n_peaks_pm25_feature_vector
n_peaks_temp_to_find = Params.n_peaks_temp_feature_vector
n_peaks_humidity_to_find = Params.n_peaks_humidity_feature_vector

day_intr = (1, 32)


class FeatureVectorGenerator:

    def __init__(self, dataset):
        self.dataset = dataset
        return

    def init_csv_file(self):
        with open('feature_vector_results/feature_vector.csv', mode='w') as feature_vector_file:
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
                 'n_hum_peaks_next30', 'pasto'])
        return

    def get_data(self, DAY):
        day_data = DataPrefab.get_data_by_sensor_and_day(self.dataset, 1, DAY)
        n_rilevazioni = len(day_data.datetime)
        if n_rilevazioni >= 1000 or use_incomplete_sample:
            return day_data
        return

    def make_avg(self, data):

        return

    def find_peaks(self, data):

        if Params.use_raw_data:
            avg_co2 = data.co2
            avg_tvoc = data.tvoc
            avg_pm25 = data.pm25
            avg_temp = data.temperature
            avg_hum = data.humidity
        else:
            avg_co2, avg_tvoc, avg_pm25, avg_temp, avg_hum = ad_data.make_avg_of_param(data)

        co2_peaks = pd.get_peaks(avg_co2, 60, 0.6, 1, n_peaks_co2_to_find)
        tvoc_peaks = pd.get_peaks(avg_tvoc, 60, 0.9, 1, n_peaks_tvoc_to_find)
        pm25_peaks = pd.get_pm25_peaks(avg_pm25, 70, n_peaks_pm25_to_find)
        temp_peaks = pd.get_peaks(avg_temp, 20, 10, 1, n_peaks_temp_to_find)
        humidity_peaks = pd.get_peaks(avg_hum, 60, [10, 30], 1, n_peaks_humidity_to_find)
        return co2_peaks, tvoc_peaks, pm25_peaks, temp_peaks, humidity_peaks


    def count_peaks_in_inteval(self, peaks, value, interval):
        counter_last = 0
        counter_next = 0

        for p in peaks:
            if value - interval <= p <= value:
                counter_last += 1
            if value <= p <= value + interval:
                counter_next += 1
        return counter_last, counter_next


    def get_pasto_by_minute(self, day_data, minute):
        counter = 0
        for i in range(len(day_data.datetime)-1):
            counter += 1
            if day_data.datetime[i] == minute:
                break
        if Params.use_raw_data:
            if day_data.activity[counter] == 0:
                return 'N'
            else:
                return 'Y'
        else:
            if day_data.is_pasto[counter] == 0:
                return 'N'
            else:
                return 'Y'

    def print_feature(self, co2_p, tvoc_p, pm25_p, temp_p, hum_p, day_data):
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

            pasto = self.get_pasto_by_minute(day_data, day_data.datetime[i])

            with open('feature_vector_results/feature_vector.csv', mode='a+') as feature_vector_file:
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
                     hum_count_next30, pasto])
        return


    def generate(self):
        self.init_csv_file()
        for day in range(Params.DAY_intr[0], Params.DAY_intr[1]):
            day_data = self.get_data(day)
            if not day_data is None:
                # recupero i picchi
                co2_p, tvoc_p, pm25_p, temp_p, hum_p = self.find_peaks(day_data)
                self.print_feature(co2_p, tvoc_p, pm25_p, temp_p, hum_p, day_data)
        return
