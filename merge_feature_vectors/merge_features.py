#
#   Author: Mauro Marini
#   Project: tesi
#   File: merge_feature_vector/merge_features.py
#
import csv

from data_manager.elaborated_data_extractor import DataSet
from data_manager.raw_data_extractor import RawDataSet
import numpy as np


class Merged_feature:

    def __init__(self):
        self.co2_count_last5 = []
        self.co2_count_next5 = []
        self.co2_count_last10 = []
        self.co2_count_next10 = []
        self.co2_count_last15 = []
        self.co2_count_next15 = []
        self.co2_count_last20 = []
        self.co2_count_next20 = []
        self.co2_count_last25 = []
        self.co2_count_next25 = []
        self.co2_count_last30 = []
        self.co2_count_next30 = []
        self.tvoc_count_last5 = []
        self.tvoc_count_next5 = []
        self.tvoc_count_last10 = []
        self.tvoc_count_next10 = []
        self.tvoc_count_last15 = []
        self.tvoc_count_next15 = []
        self.tvoc_count_last20 = []
        self.tvoc_count_next20 = []
        self.tvoc_count_last25 = []
        self.tvoc_count_next25 = []
        self.tvoc_count_last30 = []
        self.tvoc_count_next30 = []
        self.pm25_count_last5 = []
        self.pm25_count_next5 = []
        self.pm25_count_last10 = []
        self.pm25_count_next10 = []
        self.pm25_count_last15 = []
        self.pm25_count_next15 = []
        self.pm25_count_last20 = []
        self.pm25_count_next20 = []
        self.pm25_count_last25 = []
        self.pm25_count_next25 = []
        self.pm25_count_last30 = []
        self.pm25_count_next30 = []
        self.temp_count_last5 = []
        self.temp_count_next5 = []
        self.temp_count_last10 = []
        self.temp_count_next10 = []
        self.temp_count_last15 = []
        self.temp_count_next15 = []
        self.temp_count_last20 = []
        self.temp_count_next20 = []
        self.temp_count_last25 = []
        self.temp_count_next25 = []
        self.temp_count_last30 = []
        self.temp_count_next30 = []
        self.hum_count_last5 = []
        self.hum_count_next5 = []
        self.hum_count_last10 = []
        self.hum_count_next10 = []
        self.hum_count_last15 = []
        self.hum_count_next15 = []
        self.hum_count_last20 = []
        self.hum_count_next20 = []
        self.hum_count_last25 = []
        self.hum_count_next25 = []
        self.hum_count_last30 = []
        self.hum_count_next30 = []
        self.min_dist_co2 = []
        self.min_dist_tvoc = []
        self.min_dist_pm25 = []
        self.min_dist_temp = []
        self.min_dist_hum = []
        self.max_temperature_last5min = []
        self.min_temperature_last5min = []
        self.avg_temperature_last5min = []
        self.stdev_temperature_last5min = []
        self.max_temperature_next5min = []
        self.min_temperature_next5min = []
        self.avg_temperature_next5min = []
        self.stdev_temperature_next5min = []
        self.diff_temperature_5min = []
        self.diff_temperature_10min = []
        self.diff_temperature_15min = []
        self.diff_temperature_20min = []
        self.diff_temperature_25min = []
        self.s_diff_temperature_5min = []
        self.s_diff_temperature_10min = []
        self.s_diff_temperature_15min = []
        self.s_diff_temperature_20min = []
        self.s_diff_temperature_25min = []
        self.max_humidity_last5min = []
        self.min_humidity_last5min = []
        self.avg_humidity_last5min = []
        self.stdev_humidity_last5min = []
        self.max_humidity_next5min = []
        self.min_humidity_next5min = []
        self.avg_humidity_next5min = []
        self.stdev_humidity_next5min = []
        self.diff_humidity_5min = []
        self.diff_humidity_10min = []
        self.diff_humidity_15min = []
        self.diff_humidity_20min = []
        self.diff_humidity_25min = []
        self.s_diff_humidity_5min = []
        self.s_diff_humidity_10min = []
        self.s_diff_humidity_15min = []
        self.s_diff_humidity_20min = []
        self.s_diff_humidity_25min = []
        self.max_co2_last5min = []
        self.min_co2_last5min = []
        self.avg_co2_last5min = []
        self.stdev_co2_last5min = []
        self.max_co2_next5min = []
        self.min_co2_next5min = []
        self.avg_co2_next5min = []
        self.stdev_co2_next5min = []
        self.diff_co2_5min = []
        self.diff_co2_10min = []
        self.diff_co2_15min = []
        self.diff_co2_20min = []
        self.diff_co2_25min = []
        self.s_diff_co2_5min = []
        self.s_diff_co2_10min = []
        self.s_diff_co2_15min = []
        self.s_diff_co2_20min = []
        self.s_diff_co2_25min = []
        self.max_pm25_last5min = []
        self.min_pm25_last5min = []
        self.avg_pm25_last5min = []
        self.stdev_pm25_last5min = []
        self.max_pm25_next5min = []
        self.min_pm25_next5min = []
        self.avg_pm25_next5min = []
        self.stdev_pm25_next5min = []
        self.diff_pm25_5min = []
        self.diff_pm25_10min = []
        self.diff_pm25_15min = []
        self.diff_pm25_20min = []
        self.diff_pm25_25min = []
        self.s_diff_pm25_5min = []
        self.s_diff_pm25_10min = []
        self.s_diff_pm25_15min = []
        self.s_diff_pm25_20min = []
        self.s_diff_pm25_25min = []
        self.max_tvoc_last5min = []
        self.min_tvoc_last5min = []
        self.avg_tvoc_last5min = []
        self.stdev_tvoc_last5min = []
        self.max_tvoc_next5min = []
        self.min_tvoc_next5min = []
        self.avg_tvoc_next5min = []
        self.stdev_tvoc_next5min = []
        self.diff_tvoc_5min = []
        self.diff_tvoc_10min = []
        self.diff_tvoc_15min = []
        self.diff_tvoc_20min = []
        self.diff_tvoc_25min = []
        self.s_diff_tvoc_5min = []
        self.s_diff_tvoc_10min = []
        self.s_diff_tvoc_15min = []
        self.s_diff_tvoc_20min = []
        self.s_diff_tvoc_25min = []
        self.max_no2_last5min = []
        self.min_no2_last5min = []
        self.avg_no2_last5min = []
        self.stdev_no2_last5min = []
        self.max_no2_next5min = []
        self.min_no2_next5min = []
        self.avg_no2_next5min = []
        self.stdev_no2_next5min = []
        self.diff_no2_5min = []
        self.diff_no2_10min = []
        self.diff_no2_15min = []
        self.diff_no2_20min = []
        self.diff_no2_25min = []
        self.s_diff_no2_5min = []
        self.s_diff_no2_10min = []
        self.s_diff_no2_15min = []
        self.s_diff_no2_20min = []
        self.s_diff_no2_25min = []
        self.datetime = []
        self.max_datetime_last5min = []
        self.min_datetime_last5min = []
        self.max_datetime_next5min = []
        self.min_datetime_next5min = []
        self.is_pasto = []
        return

    def init_csv(self):
        with open('feature_vector_results/merged_feature_vector.csv', mode='w') as feature_vector_file:
            results_writer = csv.writer(feature_vector_file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow(
                [
                    'co2_count_last5',
                    'co2_count_next5',
                    'co2_count_last10',
                    'co2_count_next10',
                    'co2_count_last15',
                    'co2_count_next15',
                    'co2_count_last20',
                    'co2_count_next20',
                    'co2_count_last25',
                    'co2_count_next25',
                    'co2_count_last30',
                    'co2_count_next30',
                    'tvoc_count_last5',
                    'tvoc_count_next5',
                    'tvoc_count_last10',
                    'tvoc_count_next10',
                    'tvoc_count_last15',
                    'tvoc_count_next15',
                    'tvoc_count_last20',
                    'tvoc_count_next20',
                    'tvoc_count_last25',
                    'tvoc_count_next25',
                    'tvoc_count_last30',
                    'tvoc_count_next30',
                    'pm25_count_last5',
                    'pm25_count_next5',
                    'pm25_count_last10',
                    'pm25_count_next10',
                    'pm25_count_last15',
                    'pm25_count_next15',
                    'pm25_count_last20',
                    'pm25_count_next20',
                    'pm25_count_last25',
                    'pm25_count_next25',
                    'pm25_count_last30',
                    'pm25_count_next30',
                    'temp_count_last5',
                    'temp_count_next5',
                    'temp_count_last10',
                    'temp_count_next10',
                    'temp_count_last15',
                    'temp_count_next15',
                    'temp_count_last20',
                    'temp_count_next20',
                    'temp_count_last25',
                    'temp_count_next25',
                    'temp_count_last30',
                    'temp_count_next30',
                    'hum_count_last5',
                    'hum_count_next5',
                    'hum_count_last10',
                    'hum_count_next10',
                    'hum_count_last15',
                    'hum_count_next15',
                    'hum_count_last20',
                    'hum_count_next20',
                    'hum_count_last25',
                    'hum_count_next25',
                    'hum_count_last30',
                    'hum_count_next30',
                    'min_dist_co2',
                    'min_dist_tvoc',
                    'min_dist_pm25',
                    'min_dist_temp',
                    'min_dist_hum',
                    'max_temperature_last5min',
                    'min_temperature_last5min',
                    'avg_temperature_last5min',
                    'stdev_temperature_last5min',
                    'max_temperature_next5min',
                    'min_temperature_next5min',
                    'avg_temperature_next5min',
                    'stdev_temperature_next5min',
                    'diff_temperature_5min',
                    'diff_temperature_10min',
                    'diff_temperature_15min',
                    'diff_temperature_20min',
                    'diff_temperature_25min',
                    's_diff_temperature_5min',
                    's_diff_temperature_10min',
                    's_diff_temperature_15min',
                    's_diff_temperature_20min',
                    's_diff_temperature_25min',
                    'max_humidity_last5min',
                    'min_humidity_last5min',
                    'avg_humidity_last5min',
                    'stdev_humidity_last5min',
                    'max_humidity_next5min',
                    'min_humidity_next5min',
                    'avg_humidity_next5min',
                    'stdev_humidity_next5min',
                    'diff_humidity_5min',
                    'diff_humidity_10min',
                    'diff_humidity_15min',
                    'diff_humidity_20min',
                    'diff_humidity_25min',
                    's_diff_humidity_5min',
                    's_diff_humidity_10min',
                    's_diff_humidity_15min',
                    's_diff_humidity_20min',
                    's_diff_humidity_25min',
                    'max_co2_last5min',
                    'min_co2_last5min',
                    'avg_co2_last5min',
                    'stdev_co2_last5min',
                    'max_co2_next5min',
                    'min_co2_next5min',
                    'avg_co2_next5min',
                    'stdev_co2_next5min',
                    'diff_co2_5min',
                    'diff_co2_10min',
                    'diff_co2_15min',
                    'diff_co2_20min',
                    'diff_co2_25min',
                    's_diff_co2_5min',
                    's_diff_co2_10min',
                    's_diff_co2_15min',
                    's_diff_co2_20min',
                    's_diff_co2_25min',
                    'max_pm25_last5min',
                    'min_pm25_last5min',
                    'avg_pm25_last5min',
                    'stdev_pm25_last5min',
                    'max_pm25_next5min',
                    'min_pm25_next5min',
                    'avg_pm25_next5min',
                    'stdev_pm25_next5min',
                    'diff_pm25_5min',
                    'diff_pm25_10min',
                    'diff_pm25_15min',
                    'diff_pm25_20min',
                    'diff_pm25_25min',
                    's_diff_pm25_5min',
                    's_diff_pm25_10min',
                    's_diff_pm25_15min',
                    's_diff_pm25_20min',
                    's_diff_pm25_25min',
                    'max_tvoc_last5min',
                    'min_tvoc_last5min',
                    'avg_tvoc_last5min',
                    'stdev_tvoc_last5min',
                    'max_tvoc_next5min',
                    'min_tvoc_next5min',
                    'avg_tvoc_next5min',
                    'stdev_tvoc_next5min',
                    'diff_tvoc_5min',
                    'diff_tvoc_10min',
                    'diff_tvoc_15min',
                    'diff_tvoc_20min',
                    'diff_tvoc_25min',
                    's_diff_tvoc_5min',
                    's_diff_tvoc_10min',
                    's_diff_tvoc_15min',
                    's_diff_tvoc_20min',
                    's_diff_tvoc_25min',
                    'max_no2_last5min',
                    'min_no2_last5min',
                    'avg_no2_last5min',
                    'stdev_no2_last5min',
                    'max_no2_next5min',
                    'min_no2_next5min',
                    'avg_no2_next5min',
                    'stdev_no2_next5min',
                    'diff_no2_5min',
                    'diff_no2_10min',
                    'diff_no2_15min',
                    'diff_no2_20min',
                    'diff_no2_25min',
                    's_diff_no2_5min',
                    's_diff_no2_10min',
                    's_diff_no2_15min',
                    's_diff_no2_20min',
                    's_diff_no2_25min',
                    'datetime',
                    'is_pasto'
                ])
            return

    def add_peaks_features(self, dataset):
        counter = 0
        with open('training_sets_results/peaks_feature_{}.csv'.format(dataset), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if counter != 0:
                    self.datetime.append(float(row[0]))
                    self.co2_count_last5.append(float(row[1]))
                    self.co2_count_next5.append(float(row[2]))
                    self.co2_count_last10.append(float(row[3]))
                    self.co2_count_next10.append(float(row[4]))
                    self.co2_count_last15.append(float(row[5]))
                    self.co2_count_next15.append(float(row[6]))
                    self.co2_count_last20.append(float(row[7]))
                    self.co2_count_next20.append(float(row[8]))
                    self.co2_count_last25.append(float(row[9]))
                    self.co2_count_next25.append(float(row[10]))
                    self.co2_count_last30.append(float(row[11]))
                    self.co2_count_next30.append(float(row[12]))
                    self.tvoc_count_last5.append(float(row[13]))

                    self.tvoc_count_next5.append(float(row[14]))
                    self.tvoc_count_last10.append(float(row[15]))
                    self.tvoc_count_next10.append(float(row[16]))
                    self.tvoc_count_last15.append(float(row[17]))
                    self.tvoc_count_next15.append(float(row[18]))
                    self.tvoc_count_last20.append(float(row[19]))
                    self.tvoc_count_next20.append(float(row[20]))
                    self.tvoc_count_last25.append(float(row[21]))
                    self.tvoc_count_next25.append(float(row[22]))
                    self.tvoc_count_last30.append(float(row[23]))
                    self.tvoc_count_next30.append(float(row[24]))

                    self.pm25_count_last5.append(float(row[25]))
                    self.pm25_count_next5.append(float(row[26]))
                    self.pm25_count_last10.append(float(row[27]))
                    self.pm25_count_next10.append(float(row[28]))
                    self.pm25_count_last15.append(float(row[29]))
                    self.pm25_count_next15.append(float(row[30]))
                    self.pm25_count_last20.append(float(row[31]))
                    self.pm25_count_next20.append(float(row[32]))
                    self.pm25_count_last25.append(float(row[33]))
                    self.pm25_count_next25.append(float(row[34]))
                    self.pm25_count_last30.append(float(row[35]))
                    self.pm25_count_next30.append(float(row[36]))

                    self.temp_count_last5.append(float(row[37]))
                    self.temp_count_next5.append(float(row[38]))
                    self.temp_count_last10.append(float(row[39]))
                    self.temp_count_next10.append(float(row[40]))
                    self.temp_count_last15.append(float(row[41]))
                    self.temp_count_next15.append(float(row[42]))
                    self.temp_count_last20.append(float(row[43]))
                    self.temp_count_next20.append(float(row[44]))
                    self.temp_count_last25.append(float(row[45]))
                    self.temp_count_next25.append(float(row[46]))
                    self.temp_count_last30.append(float(row[47]))
                    self.temp_count_next30.append(float(row[48]))

                    self.hum_count_last5.append(float(row[49]))
                    self.hum_count_next5.append(float(row[50]))
                    self.hum_count_last10.append(float(row[51]))
                    self.hum_count_next10.append(float(row[52]))
                    self.hum_count_last15.append(float(row[53]))
                    self.hum_count_next15.append(float(row[54]))
                    self.hum_count_last20.append(float(row[55]))
                    self.hum_count_next20.append(float(row[56]))
                    self.hum_count_last25.append(float(row[57]))
                    self.hum_count_next25.append(float(row[58]))
                    self.hum_count_last30.append(float(row[59]))
                    self.hum_count_next30.append(float(row[60]))

                    self.min_dist_co2.append(float(row[61]))
                    self.min_dist_tvoc.append(float(row[62]))
                    self.min_dist_pm25.append(float(row[63]))
                    self.min_dist_temp.append(float(row[64]))
                    self.min_dist_hum.append(float(row[65]))

                    self.is_pasto.append(row[66])
                counter += 1


    def add_avg_features(self, dataset):
        avg_features = DataSet.extract_data_from_sensor(DataSet(), dataset)
        raw_dataset = RawDataSet.extract_data_from_sensor(RawDataSet(), dataset)  # solo per test

        counter_equals = 0
        counter_difference = 0


        print(len(self.datetime) - len(raw_dataset.datetime))
        for i in range(len(avg_features.datetime)):
            if self.datetime[i] == raw_dataset.datetime[i] and ((self.is_pasto[i] == 'Y' and raw_dataset.activity[i] != 'None') or (self.is_pasto[i] == 'N' and raw_dataset.activity[i] == 'None')):
                counter_equals += 1
            else:  # le tuple dei due feature vector non combaciano
                counter_difference += 1
        print("CONFRONTO CON I DATI GREZZI (data e pasto) | equals: {}, differences: {}".format(counter_equals, counter_difference))

        counter_difference = 0
        counter_equals = 0

        j = 31
        for i in range(len(avg_features.datetime)):
            if self.datetime[j] == avg_features.datetime[i] and ((self.is_pasto[j] == 'Y' and avg_features.is_pasto[i] == 1) or (self.is_pasto[j] == 'N' and avg_features.is_pasto[i] == 0)):
                counter_equals += 1
            else:  # le tuple dei due feature vector non combaciano
                counter_difference += 1
            j += 1
        print("CONFRONTO CON IL FEATURE DELLA COLLEGA (data e pasto) | equals: {}, differences: {}".format(counter_equals, counter_difference))
        if counter_difference == 0:
            self.max_temperature_last5min = avg_features.max_temperature_last5min
            self.min_temperature_last5min = avg_features.min_temperature_last5min
            self.avg_temperature_last5min = avg_features.avg_temperature_last5min
            self.stdev_temperature_last5min = avg_features.stdev_temperature_last5min
            self.max_temperature_next5min = avg_features.max_temperature_next5min
            self.min_temperature_next5min = avg_features.min_temperature_next5min
            self.avg_temperature_next5min = avg_features.avg_temperature_next5min
            self.stdev_temperature_next5min = avg_features.stdev_temperature_next5min
            self.diff_temperature_5min = avg_features.diff_temperature_5min
            self.diff_temperature_10min = avg_features.diff_temperature_10min
            self.diff_temperature_15min = avg_features.diff_temperature_15min
            self.diff_temperature_20min = avg_features.diff_temperature_20min
            self.diff_temperature_25min = avg_features.diff_temperature_25min
            self.s_diff_temperature_5min = avg_features.s_diff_temperature_5min
            self.s_diff_temperature_10min = avg_features.s_diff_temperature_10min
            self.s_diff_temperature_15min = avg_features.s_diff_temperature_15min
            self.s_diff_temperature_20min = avg_features.s_diff_temperature_20min
            self.s_diff_temperature_25min = avg_features.s_diff_temperature_25min
            self.max_humidity_last5min = avg_features.max_humidity_last5min
            self.min_humidity_last5min = avg_features.min_humidity_last5min
            self.avg_humidity_last5min = avg_features.avg_humidity_last5min
            self.stdev_humidity_last5min = avg_features.stdev_humidity_last5min
            self.max_humidity_next5min = avg_features.max_humidity_next5min
            self.min_humidity_next5min = avg_features.min_humidity_next5min
            self.avg_humidity_next5min = avg_features.avg_humidity_next5min
            self.stdev_humidity_next5min = avg_features.stdev_humidity_next5min
            self.diff_humidity_5min = avg_features.diff_humidity_5min
            self.diff_humidity_10min = avg_features.diff_humidity_10min
            self.diff_humidity_15min = avg_features.diff_humidity_15min
            self.diff_humidity_20min = avg_features.diff_humidity_20min
            self.diff_humidity_25min = avg_features.diff_humidity_25min
            self.s_diff_humidity_5min = avg_features.s_diff_humidity_5min
            self.s_diff_humidity_10min = avg_features.s_diff_humidity_10min
            self.s_diff_humidity_15min = avg_features.s_diff_humidity_15min
            self.s_diff_humidity_20min = avg_features.s_diff_humidity_20min
            self.s_diff_humidity_25min = avg_features.s_diff_humidity_25min
            self.max_co2_last5min = avg_features.max_co2_last5min
            self.min_co2_last5min = avg_features.min_co2_last5min
            self.avg_co2_last5min = avg_features.avg_co2_last5min
            self.stdev_co2_last5min = avg_features.stdev_co2_last5min
            self.max_co2_next5min = avg_features.max_co2_next5min
            self.min_co2_next5min = avg_features.min_co2_next5min
            self.avg_co2_next5min = avg_features.avg_co2_next5min
            self.stdev_co2_next5min = avg_features.stdev_co2_next5min
            self.diff_co2_5min = avg_features.diff_co2_5min
            self.diff_co2_10min = avg_features.diff_co2_10min
            self.diff_co2_15min = avg_features.diff_co2_15min
            self.diff_co2_20min = avg_features.diff_co2_20min
            self.diff_co2_25min = avg_features.diff_co2_25min
            self.s_diff_co2_5min = avg_features.s_diff_co2_5min
            self.s_diff_co2_10min = avg_features.s_diff_co2_10min
            self.s_diff_co2_15min = avg_features.s_diff_co2_15min
            self.s_diff_co2_20min = avg_features.s_diff_co2_20min
            self.s_diff_co2_25min = avg_features.s_diff_co2_25min
            self.max_pm25_last5min = avg_features.max_pm25_last5min
            self.min_pm25_last5min = avg_features.min_pm25_last5min
            self.avg_pm25_last5min = avg_features.avg_pm25_last5min
            self.stdev_pm25_last5min = avg_features.stdev_pm25_last5min
            self.max_pm25_next5min = avg_features.max_pm25_next5min
            self.min_pm25_next5min = avg_features.min_pm25_next5min
            self.avg_pm25_next5min = avg_features.avg_pm25_next5min
            self.stdev_pm25_next5min = avg_features.stdev_pm25_next5min
            self.diff_pm25_5min = avg_features.diff_pm25_5min
            self.diff_pm25_10min = avg_features.diff_pm25_10min
            self.diff_pm25_15min = avg_features.diff_pm25_15min
            self.diff_pm25_20min = avg_features.diff_pm25_20min
            self.diff_pm25_25min = avg_features.diff_pm25_25min
            self.s_diff_pm25_5min = avg_features.s_diff_pm25_5min
            self.s_diff_pm25_10min = avg_features.s_diff_pm25_10min
            self.s_diff_pm25_15min = avg_features.s_diff_pm25_15min
            self.s_diff_pm25_20min = avg_features.s_diff_pm25_20min
            self.s_diff_pm25_25min = avg_features.s_diff_pm25_25min
            self.max_tvoc_last5min = avg_features.max_tvoc_last5min
            self.min_tvoc_last5min = avg_features.min_tvoc_last5min
            self.avg_tvoc_last5min = avg_features.avg_tvoc_last5min
            self.stdev_tvoc_last5min = avg_features.stdev_tvoc_last5min
            self.max_tvoc_next5min = avg_features.max_tvoc_next5min
            self.min_tvoc_next5min = avg_features.min_tvoc_next5min
            self.avg_tvoc_next5min = avg_features.avg_tvoc_next5min
            self.stdev_tvoc_next5min = avg_features.stdev_tvoc_next5min
            self.diff_tvoc_5min = avg_features.diff_tvoc_5min
            self.diff_tvoc_10min = avg_features.diff_tvoc_10min
            self.diff_tvoc_15min = avg_features.diff_tvoc_15min
            self.diff_tvoc_20min = avg_features.diff_tvoc_20min
            self.diff_tvoc_25min = avg_features.diff_tvoc_25min
            self.s_diff_tvoc_5min = avg_features.s_diff_tvoc_5min
            self.s_diff_tvoc_10min = avg_features.s_diff_tvoc_10min
            self.s_diff_tvoc_15min = avg_features.s_diff_tvoc_15min
            self.s_diff_tvoc_20min = avg_features.s_diff_tvoc_20min
            self.s_diff_tvoc_25min = avg_features.s_diff_tvoc_25min
            self.max_no2_last5min = avg_features.max_no2_last5min
            self.min_no2_last5min = avg_features.min_no2_last5min
            self.avg_no2_last5min = avg_features.avg_no2_last5min
            self.stdev_no2_last5min = avg_features.stdev_no2_last5min
            self.max_no2_next5min = avg_features.max_no2_next5min
            self.min_no2_next5min = avg_features.min_no2_next5min
            self.avg_no2_next5min = avg_features.avg_no2_next5min
            self.stdev_no2_next5min = avg_features.stdev_no2_next5min
            self.diff_no2_5min = avg_features.diff_no2_5min
            self.diff_no2_10min = avg_features.diff_no2_10min
            self.diff_no2_15min = avg_features.diff_no2_15min
            self.diff_no2_20min = avg_features.diff_no2_20min
            self.diff_no2_25min = avg_features.diff_no2_25min
            self.s_diff_no2_5min = avg_features.s_diff_no2_5min
            self.s_diff_no2_10min = avg_features.s_diff_no2_10min
            self.s_diff_no2_15min = avg_features.s_diff_no2_15min
            self.s_diff_no2_20min = avg_features.s_diff_no2_20min
            self.s_diff_no2_25min = avg_features.s_diff_no2_25min
        return

    def export_to_csv(self):
        with open('feature_vector_results/merged_feature_vector.csv', mode='a+') as feature_vector_file:
            results_writer = csv.writer(feature_vector_file, delimiter=',', quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
            for i in range(30, len(self.datetime) - 61):
                results_writer.writerow(
                    [self.co2_count_last5[i],
                        self.co2_count_next5[i],
                        self.co2_count_last10[i],
                        self.co2_count_next10[i],
                        self.co2_count_last15[i],
                        self.co2_count_next15[i],
                        self.co2_count_last20[i],
                        self.co2_count_next20[i],
                        self.co2_count_last25[i],
                        self.co2_count_next25[i],
                        self.co2_count_last30[i],
                        self.co2_count_next30[i],
                        self.tvoc_count_last5[i],
                        self.tvoc_count_next5[i],
                        self.tvoc_count_last10[i],
                        self.tvoc_count_next10[i],
                        self.tvoc_count_last15[i],
                        self.tvoc_count_next15[i],
                        self.tvoc_count_last20[i],
                        self.tvoc_count_next20[i],
                        self.tvoc_count_last25[i],
                        self.tvoc_count_next25[i],
                        self.tvoc_count_last30[i],
                        self.tvoc_count_next30[i],
                        self.pm25_count_last5[i],
                        self.pm25_count_next5[i],
                        self.pm25_count_last10[i],
                        self.pm25_count_next10[i],
                        self.pm25_count_last15[i],
                        self.pm25_count_next15[i],
                        self.pm25_count_last20[i],
                        self.pm25_count_next20[i],
                        self.pm25_count_last25[i],
                        self.pm25_count_next25[i],
                        self.pm25_count_last30[i],
                        self.pm25_count_next30[i],
                        self.temp_count_last5[i],
                        self.temp_count_next5[i],
                        self.temp_count_last10[i],
                        self.temp_count_next10[i],
                        self.temp_count_last15[i],
                        self.temp_count_next15[i],
                        self.temp_count_last20[i],
                        self.temp_count_next20[i],
                        self.temp_count_last25[i],
                        self.temp_count_next25[i],
                        self.temp_count_last30[i],
                        self.temp_count_next30[i],
                        self.hum_count_last5[i],
                        self.hum_count_next5[i],
                        self.hum_count_last10[i],
                        self.hum_count_next10[i],
                        self.hum_count_last15[i],
                        self.hum_count_next15[i],
                        self.hum_count_last20[i],
                        self.hum_count_next20[i],
                        self.hum_count_last25[i],
                        self.hum_count_next25[i],
                        self.hum_count_last30[i],
                        self.hum_count_next30[i],
                        self.min_dist_co2[i],
                        self.min_dist_tvoc[i],
                        self.min_dist_pm25[i],
                        self.min_dist_temp[i],
                        self.min_dist_hum[i],
                        self.max_temperature_last5min[i],
                        self.min_temperature_last5min[i],
                        self.avg_temperature_last5min[i],
                        self.stdev_temperature_last5min[i],
                        self.max_temperature_next5min[i],
                        self.min_temperature_next5min[i],
                        self.avg_temperature_next5min[i],
                        self.stdev_temperature_next5min[i],
                        self.diff_temperature_5min[i],
                        self.diff_temperature_10min[i],
                        self.diff_temperature_15min[i],
                        self.diff_temperature_20min[i],
                        self.diff_temperature_25min[i],
                        self.s_diff_temperature_5min[i],
                        self.s_diff_temperature_10min[i],
                        self.s_diff_temperature_15min[i],
                        self.s_diff_temperature_20min[i],
                        self.s_diff_temperature_25min[i],
                        self.max_humidity_last5min[i],
                        self.min_humidity_last5min[i],
                        self.avg_humidity_last5min[i],
                        self.stdev_humidity_last5min[i],
                        self.max_humidity_next5min[i],
                        self.min_humidity_next5min[i],
                        self.avg_humidity_next5min[i],
                        self.stdev_humidity_next5min[i],
                        self.diff_humidity_5min[i],
                        self.diff_humidity_10min[i],
                        self.diff_humidity_15min[i],
                        self.diff_humidity_20min[i],
                        self.diff_humidity_25min[i],
                        self.s_diff_humidity_5min[i],
                        self.s_diff_humidity_10min[i],
                        self.s_diff_humidity_15min[i],
                        self.s_diff_humidity_20min[i],
                        self.s_diff_humidity_25min[i],
                        self.max_co2_last5min[i],
                        self.min_co2_last5min[i],
                        self.avg_co2_last5min[i],
                        self.stdev_co2_last5min[i],
                        self.max_co2_next5min[i],
                        self.min_co2_next5min[i],
                        self.avg_co2_next5min[i],
                        self.stdev_co2_next5min[i],
                        self.diff_co2_5min[i],
                        self.diff_co2_10min[i],
                        self.diff_co2_15min[i],
                        self.diff_co2_20min[i],
                        self.diff_co2_25min[i],
                        self.s_diff_co2_5min[i],
                        self.s_diff_co2_10min[i],
                        self.s_diff_co2_15min[i],
                        self.s_diff_co2_20min[i],
                        self.s_diff_co2_25min[i],
                        self.max_pm25_last5min[i],
                        self.min_pm25_last5min[i],
                        self.avg_pm25_last5min[i],
                        self.stdev_pm25_last5min[i],
                        self.max_pm25_next5min[i],
                        self.min_pm25_next5min[i],
                        self.avg_pm25_next5min[i],
                        self.stdev_pm25_next5min[i],
                        self.diff_pm25_5min[i],
                        self.diff_pm25_10min[i],
                        self.diff_pm25_15min[i],
                        self.diff_pm25_20min[i],
                        self.diff_pm25_25min[i],
                        self.s_diff_pm25_5min[i],
                        self.s_diff_pm25_10min[i],
                        self.s_diff_pm25_15min[i],
                        self.s_diff_pm25_20min[i],
                        self.s_diff_pm25_25min[i],
                        self.max_tvoc_last5min[i],
                        self.min_tvoc_last5min[i],
                        self.avg_tvoc_last5min[i],
                        self.stdev_tvoc_last5min[i],
                        self.max_tvoc_next5min[i],
                        self.min_tvoc_next5min[i],
                        self.avg_tvoc_next5min[i],
                        self.stdev_tvoc_next5min[i],
                        self.diff_tvoc_5min[i],
                        self.diff_tvoc_10min[i],
                        self.diff_tvoc_15min[i],
                        self.diff_tvoc_20min[i],
                        self.diff_tvoc_25min[i],
                        self.s_diff_tvoc_5min[i],
                        self.s_diff_tvoc_10min[i],
                        self.s_diff_tvoc_15min[i],
                        self.s_diff_tvoc_20min[i],
                        self.s_diff_tvoc_25min[i],
                        self.max_no2_last5min[i],
                        self.min_no2_last5min[i],
                        self.avg_no2_last5min[i],
                        self.stdev_no2_last5min[i],
                        self.max_no2_next5min[i],
                        self.min_no2_next5min[i],
                        self.avg_no2_next5min[i],
                        self.stdev_no2_next5min[i],
                        self.diff_no2_5min[i],
                        self.diff_no2_10min[i],
                        self.diff_no2_15min[i],
                        self.diff_no2_20min[i],
                        self.diff_no2_25min[i],
                        self.s_diff_no2_5min[i],
                        self.s_diff_no2_10min[i],
                        self.s_diff_no2_15min[i],
                        self.s_diff_no2_20min[i],
                        self.s_diff_no2_25min[i],
                        self.datetime[i],
                        self.is_pasto[i]])
        return

    def merge_by_dataset(self, dataset):
        self.init_csv()
        self.add_peaks_features(dataset)
        self.add_avg_features(dataset)
        self.export_to_csv()
        return
