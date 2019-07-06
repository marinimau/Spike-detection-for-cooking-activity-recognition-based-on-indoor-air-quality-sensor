'''
    Author: Mauro Marini
    Project: tesi
    File: data_manager/data_extractor.py
'''

import numpy as np

class DataSet:

    def __init__(self):
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

    def create(self, max_temperature_last5min, min_temperature_last5min, avg_temperature_last5min,
               stdev_temperature_last5min, max_temperature_next5min, min_temperature_next5min,
               avg_temperature_next5min, stdev_temperature_next5min, diff_temperature_5min,
               diff_temperature_10min, diff_temperature_15min, diff_temperature_20min, diff_temperature_25min,
               s_diff_temperature_5min, s_diff_temperature_10min, s_diff_temperature_15min,
               s_diff_temperature_20min, s_diff_temperature_25min, max_humidity_last5min,
               min_humidity_last5min, avg_humidity_last5min, stdev_humidity_last5min, max_humidity_next5min,
               min_humidity_next5min, avg_humidity_next5min, stdev_humidity_next5min, diff_humidity_5min,
               diff_humidity_10min, diff_humidity_15min, diff_humidity_20min, diff_humidity_25min,
               s_diff_humidity_5min, s_diff_humidity_10min, s_diff_humidity_15min, s_diff_humidity_20min,
               s_diff_humidity_25min, max_co2_last5min, min_co2_last5min, avg_co2_last5min, stdev_co2_last5min,
               max_co2_next5min, min_co2_next5min, avg_co2_next5min, stdev_co2_next5min, diff_co2_5min,
               diff_co2_10min, diff_co2_15min, diff_co2_20min, diff_co2_25min, s_diff_co2_5min,
               s_diff_co2_10min, s_diff_co2_15min, s_diff_co2_20min, s_diff_co2_25min, max_pm25_last5min,
               min_pm25_last5min, avg_pm25_last5min, stdev_pm25_last5min, max_pm25_next5min, min_pm25_next5min,
               avg_pm25_next5min, stdev_pm25_next5min, diff_pm25_5min, diff_pm25_10min, diff_pm25_15min,
               diff_pm25_20min, diff_pm25_25min, s_diff_pm25_5min, s_diff_pm25_10min, s_diff_pm25_15min,
               s_diff_pm25_20min, s_diff_pm25_25min, max_tvoc_last5min, min_tvoc_last5min, avg_tvoc_last5min,
               stdev_tvoc_last5min, max_tvoc_next5min, min_tvoc_next5min, avg_tvoc_next5min,
               stdev_tvoc_next5min, diff_tvoc_5min, diff_tvoc_10min, diff_tvoc_15min, diff_tvoc_20min,
               diff_tvoc_25min, s_diff_tvoc_5min, s_diff_tvoc_10min, s_diff_tvoc_15min, s_diff_tvoc_20min,
               s_diff_tvoc_25min, max_no2_last5min, min_no2_last5min, avg_no2_last5min, stdev_no2_last5min,
               max_no2_next5min, min_no2_next5min, avg_no2_next5min, stdev_no2_next5min, diff_no2_5min,
               diff_no2_10min, diff_no2_15min, diff_no2_20min, diff_no2_25min, s_diff_no2_5min,
               s_diff_no2_10min, s_diff_no2_15min, s_diff_no2_20min, s_diff_no2_25min, datetime,
               max_datetime_last5min, min_datetime_last5min, max_datetime_next5min, min_datetime_next5min,
               is_pasto):
        self.max_temperature_last5min = max_temperature_last5min
        self.min_temperature_last5min = min_temperature_last5min
        self.avg_temperature_last5min = avg_temperature_last5min
        self.stdev_temperature_last5min = stdev_temperature_last5min
        self.max_temperature_next5min = max_temperature_next5min
        self.min_temperature_next5min = min_temperature_next5min
        self.avg_temperature_next5min = avg_temperature_next5min
        self.stdev_temperature_next5min = stdev_temperature_next5min
        self.diff_temperature_5min = diff_temperature_5min
        self.diff_temperature_10min = diff_temperature_10min
        self.diff_temperature_15min = diff_temperature_15min
        self.diff_temperature_20min = diff_temperature_20min
        self.diff_temperature_25min = diff_temperature_25min
        self.s_diff_temperature_5min = s_diff_temperature_5min
        self.s_diff_temperature_10min = s_diff_temperature_10min
        self.s_diff_temperature_15min = s_diff_temperature_15min
        self.s_diff_temperature_20min = s_diff_temperature_20min
        self.s_diff_temperature_25min = s_diff_temperature_25min
        self.max_humidity_last5min = max_humidity_last5min
        self.min_humidity_last5min = min_humidity_last5min
        self.avg_humidity_last5min = avg_humidity_last5min
        self.stdev_humidity_last5min = stdev_humidity_last5min
        self.max_humidity_next5min = max_humidity_next5min
        self.min_humidity_next5min = min_humidity_next5min
        self.avg_humidity_next5min = avg_humidity_next5min
        self.stdev_humidity_next5min = stdev_humidity_next5min
        self.diff_humidity_5min = diff_humidity_5min
        self.diff_humidity_10min = diff_humidity_10min
        self.diff_humidity_15min = diff_humidity_15min
        self.diff_humidity_20min = diff_humidity_20min
        self.diff_humidity_25min = diff_humidity_25min
        self.s_diff_humidity_5min = s_diff_humidity_5min
        self.s_diff_humidity_10min = s_diff_humidity_10min
        self.s_diff_humidity_15min = s_diff_humidity_15min
        self.s_diff_humidity_20min = s_diff_humidity_20min
        self.s_diff_humidity_25min = s_diff_humidity_25min
        self.max_co2_last5min = max_co2_last5min
        self.min_co2_last5min = min_co2_last5min
        self.avg_co2_last5min = avg_co2_last5min
        self.stdev_co2_last5min = stdev_co2_last5min
        self.max_co2_next5min = max_co2_next5min
        self.min_co2_next5min = min_co2_next5min
        self.avg_co2_next5min = avg_co2_next5min
        self.stdev_co2_next5min = stdev_co2_next5min
        self.diff_co2_5min = diff_co2_5min
        self.diff_co2_10min = diff_co2_10min
        self.diff_co2_15min = diff_co2_15min
        self.diff_co2_20min = diff_co2_20min
        self.diff_co2_25min = diff_co2_25min
        self.s_diff_co2_5min = s_diff_co2_5min
        self.s_diff_co2_10min = s_diff_co2_10min
        self.s_diff_co2_15min = s_diff_co2_15min
        self.s_diff_co2_20min = s_diff_co2_20min
        self.s_diff_co2_25min = s_diff_co2_25min
        self.max_pm25_last5min = max_pm25_last5min
        self.min_pm25_last5min = min_pm25_last5min
        self.avg_pm25_last5min = avg_pm25_last5min
        self.stdev_pm25_last5min = stdev_pm25_last5min
        self.max_pm25_next5min = max_pm25_next5min
        self.min_pm25_next5min = min_pm25_next5min
        self.avg_pm25_next5min = avg_pm25_next5min
        self.stdev_pm25_next5min = stdev_pm25_next5min
        self.diff_pm25_5min = diff_pm25_5min
        self.diff_pm25_10min = diff_pm25_10min
        self.diff_pm25_15min = diff_pm25_15min
        self.diff_pm25_20min = diff_pm25_20min
        self.diff_pm25_25min = diff_pm25_25min
        self.s_diff_pm25_5min = s_diff_pm25_5min
        self.s_diff_pm25_10min = s_diff_pm25_10min
        self.s_diff_pm25_15min = s_diff_pm25_15min
        self.s_diff_pm25_20min = s_diff_pm25_20min
        self.s_diff_pm25_25min = s_diff_pm25_25min
        self.max_tvoc_last5min = max_tvoc_last5min
        self.min_tvoc_last5min = min_tvoc_last5min
        self.avg_tvoc_last5min = avg_tvoc_last5min
        self.stdev_tvoc_last5min = stdev_tvoc_last5min
        self.max_tvoc_next5min = max_tvoc_next5min
        self.min_tvoc_next5min = min_tvoc_next5min
        self.avg_tvoc_next5min = avg_tvoc_next5min
        self.stdev_tvoc_next5min = stdev_tvoc_next5min
        self.diff_tvoc_5min = diff_tvoc_5min
        self.diff_tvoc_10min = diff_tvoc_10min
        self.diff_tvoc_15min = diff_tvoc_15min
        self.diff_tvoc_20min = diff_tvoc_20min
        self.diff_tvoc_25min = diff_tvoc_25min
        self.s_diff_tvoc_5min = s_diff_tvoc_5min
        self.s_diff_tvoc_10min = s_diff_tvoc_10min
        self.s_diff_tvoc_15min = s_diff_tvoc_15min
        self.s_diff_tvoc_20min = s_diff_tvoc_20min
        self.s_diff_tvoc_25min = s_diff_tvoc_25min
        self.max_no2_last5min = max_no2_last5min
        self.min_no2_last5min = min_no2_last5min
        self.avg_no2_last5min = avg_no2_last5min
        self.stdev_no2_last5min = stdev_no2_last5min
        self.max_no2_next5min = max_no2_next5min
        self.min_no2_next5min = min_no2_next5min
        self.avg_no2_next5min = avg_no2_next5min
        self.stdev_no2_next5min = stdev_no2_next5min
        self.diff_no2_5min = diff_no2_5min
        self.diff_no2_10min = diff_no2_10min
        self.diff_no2_15min = diff_no2_15min
        self.diff_no2_20min = diff_no2_20min
        self.diff_no2_25min = diff_no2_25min
        self.s_diff_no2_5min = s_diff_no2_5min
        self.s_diff_no2_10min = s_diff_no2_10min
        self.s_diff_no2_15min = s_diff_no2_15min
        self.s_diff_no2_20min = s_diff_no2_20min
        self.s_diff_no2_25min = s_diff_no2_25min
        self.datetime = datetime
        self.max_datetime_last5min = max_datetime_last5min
        self.min_datetime_last5min = min_datetime_last5min
        self.max_datetime_next5min = max_datetime_next5min
        self.min_datetime_next5min = min_datetime_next5min
        self.is_pasto = is_pasto
        return self

    #extracts all data of given sensor
    def extract_data_from_sensor(self, sensor):
        max_temperature_last5min, min_temperature_last5min, avg_temperature_last5min, stdev_temperature_last5min, max_temperature_next5min, min_temperature_next5min, avg_temperature_next5min, stdev_temperature_next5min, diff_temperature_5min, diff_temperature_10min, diff_temperature_15min, diff_temperature_20min, diff_temperature_25min, s_diff_temperature_5min, s_diff_temperature_10min, s_diff_temperature_15min, s_diff_temperature_20min, s_diff_temperature_25min, max_humidity_last5min, min_humidity_last5min, avg_humidity_last5min, stdev_humidity_last5min, max_humidity_next5min, min_humidity_next5min, avg_humidity_next5min, stdev_humidity_next5min, diff_humidity_5min, diff_humidity_10min, diff_humidity_15min, diff_humidity_20min, diff_humidity_25min, s_diff_humidity_5min, s_diff_humidity_10min, s_diff_humidity_15min, s_diff_humidity_20min, s_diff_humidity_25min, max_co2_last5min, min_co2_last5min, avg_co2_last5min, stdev_co2_last5min, max_co2_next5min, min_co2_next5min, avg_co2_next5min, stdev_co2_next5min, diff_co2_5min, diff_co2_10min, diff_co2_15min, diff_co2_20min, diff_co2_25min, s_diff_co2_5min, s_diff_co2_10min, s_diff_co2_15min, s_diff_co2_20min, s_diff_co2_25min, max_pm25_last5min, min_pm25_last5min, avg_pm25_last5min, stdev_pm25_last5min, max_pm25_next5min, min_pm25_next5min, avg_pm25_next5min, stdev_pm25_next5min, diff_pm25_5min, diff_pm25_10min, diff_pm25_15min, diff_pm25_20min, diff_pm25_25min, s_diff_pm25_5min, s_diff_pm25_10min, s_diff_pm25_15min, s_diff_pm25_20min, s_diff_pm25_25min, max_tvoc_last5min, min_tvoc_last5min, avg_tvoc_last5min, stdev_tvoc_last5min, max_tvoc_next5min, min_tvoc_next5min, avg_tvoc_next5min, stdev_tvoc_next5min, diff_tvoc_5min, diff_tvoc_10min, diff_tvoc_15min, diff_tvoc_20min, diff_tvoc_25min, s_diff_tvoc_5min, s_diff_tvoc_10min, s_diff_tvoc_15min, s_diff_tvoc_20min, s_diff_tvoc_25min, max_no2_last5min, min_no2_last5min, avg_no2_last5min, stdev_no2_last5min, max_no2_next5min, min_no2_next5min, avg_no2_next5min, stdev_no2_next5min, diff_no2_5min, diff_no2_10min, diff_no2_15min, diff_no2_20min, diff_no2_25min, s_diff_no2_5min, s_diff_no2_10min, s_diff_no2_15min, s_diff_no2_20min, s_diff_no2_25min, datetime, max_datetime_last5min, min_datetime_last5min, max_datetime_next5min, min_datetime_next5min, is_pasto = np.loadtxt(
            'file/{}.csv'.format(sensor), unpack=True, delimiter=',')
        return self.create(max_temperature_last5min, min_temperature_last5min, avg_temperature_last5min,
                           stdev_temperature_last5min, max_temperature_next5min, min_temperature_next5min,
                           avg_temperature_next5min, stdev_temperature_next5min, diff_temperature_5min,
                           diff_temperature_10min, diff_temperature_15min, diff_temperature_20min,
                           diff_temperature_25min,
                           s_diff_temperature_5min, s_diff_temperature_10min, s_diff_temperature_15min,
                           s_diff_temperature_20min, s_diff_temperature_25min, max_humidity_last5min,
                           min_humidity_last5min, avg_humidity_last5min, stdev_humidity_last5min, max_humidity_next5min,
                           min_humidity_next5min, avg_humidity_next5min, stdev_humidity_next5min, diff_humidity_5min,
                           diff_humidity_10min, diff_humidity_15min, diff_humidity_20min, diff_humidity_25min,
                           s_diff_humidity_5min, s_diff_humidity_10min, s_diff_humidity_15min, s_diff_humidity_20min,
                           s_diff_humidity_25min, max_co2_last5min, min_co2_last5min, avg_co2_last5min,
                           stdev_co2_last5min,
                           max_co2_next5min, min_co2_next5min, avg_co2_next5min, stdev_co2_next5min, diff_co2_5min,
                           diff_co2_10min, diff_co2_15min, diff_co2_20min, diff_co2_25min, s_diff_co2_5min,
                           s_diff_co2_10min, s_diff_co2_15min, s_diff_co2_20min, s_diff_co2_25min, max_pm25_last5min,
                           min_pm25_last5min, avg_pm25_last5min, stdev_pm25_last5min, max_pm25_next5min,
                           min_pm25_next5min,
                           avg_pm25_next5min, stdev_pm25_next5min, diff_pm25_5min, diff_pm25_10min, diff_pm25_15min,
                           diff_pm25_20min, diff_pm25_25min, s_diff_pm25_5min, s_diff_pm25_10min, s_diff_pm25_15min,
                           s_diff_pm25_20min, s_diff_pm25_25min, max_tvoc_last5min, min_tvoc_last5min,
                           avg_tvoc_last5min,
                           stdev_tvoc_last5min, max_tvoc_next5min, min_tvoc_next5min, avg_tvoc_next5min,
                           stdev_tvoc_next5min, diff_tvoc_5min, diff_tvoc_10min, diff_tvoc_15min, diff_tvoc_20min,
                           diff_tvoc_25min, s_diff_tvoc_5min, s_diff_tvoc_10min, s_diff_tvoc_15min, s_diff_tvoc_20min,
                           s_diff_tvoc_25min, max_no2_last5min, min_no2_last5min, avg_no2_last5min, stdev_no2_last5min,
                           max_no2_next5min, min_no2_next5min, avg_no2_next5min, stdev_no2_next5min, diff_no2_5min,
                           diff_no2_10min, diff_no2_15min, diff_no2_20min, diff_no2_25min, s_diff_no2_5min,
                           s_diff_no2_10min, s_diff_no2_15min, s_diff_no2_20min, s_diff_no2_25min, datetime,
                           max_datetime_last5min, min_datetime_last5min, max_datetime_next5min, min_datetime_next5min,
                           is_pasto)





    #split dataset object and returns data of one given day
    def get_data_by_day(self,given_day):
        day_data=DataSet()

        prev_datetime=0 #init the prev daytime
        current_day=1 #save the current day
        rel_for_day=0 #count the number rows for each day
        current_row=0 #references all the rows

        for current_datetime in self.datetime:
            if current_datetime<prev_datetime:
                current_day+=1
            prev_datetime=current_datetime

            if current_day==given_day:
                rel_for_day+=1
                day_data.add_tuple(self, current_row)
            current_row+=1
        print("Tuple presenti: {}".format(rel_for_day))
        return day_data



    def add_tuple(self,parent,row):
        self.max_temperature_last5min.append(parent.max_temperature_last5min[row])
        self.min_temperature_last5min.append(parent.min_temperature_last5min[row])
        self.avg_temperature_last5min.append(parent.avg_temperature_last5min[row])
        self.stdev_temperature_last5min.append(parent.stdev_temperature_last5min[row])
        self.max_temperature_next5min.append(parent.max_temperature_next5min[row])
        self.min_temperature_next5min.append(parent.min_temperature_next5min[row])
        self.avg_temperature_next5min.append(parent.avg_temperature_next5min[row])
        self.stdev_temperature_next5min.append(parent.stdev_temperature_next5min[row])
        self.diff_temperature_5min.append(parent.diff_temperature_5min[row])
        self.diff_temperature_10min.append(parent.diff_temperature_10min[row])
        self.diff_temperature_15min.append(parent.diff_temperature_15min[row])
        self.diff_temperature_20min.append(parent.diff_temperature_20min[row])
        self.diff_temperature_25min.append(parent.diff_temperature_25min[row])
        self.s_diff_temperature_5min.append(parent.s_diff_temperature_5min[row])
        self.s_diff_temperature_10min.append(parent.s_diff_temperature_10min[row])
        self.s_diff_temperature_15min.append(parent.s_diff_temperature_15min[row])
        self.s_diff_temperature_20min.append(parent.s_diff_temperature_20min[row])
        self.s_diff_temperature_25min.append(parent.s_diff_temperature_25min[row])
        self.max_humidity_last5min.append(parent.max_humidity_last5min[row])
        self.min_humidity_last5min.append(parent.min_humidity_last5min[row])
        self.avg_humidity_last5min.append(parent.avg_humidity_last5min[row])
        self.stdev_humidity_last5min.append(parent.stdev_humidity_last5min[row])
        self.max_humidity_next5min.append(parent.max_humidity_next5min[row])
        self.min_humidity_next5min.append(parent.min_humidity_next5min[row])
        self.avg_humidity_next5min.append(parent.avg_humidity_next5min[row])
        self.stdev_humidity_next5min.append(parent.stdev_humidity_next5min[row])
        self.diff_humidity_5min.append(parent.diff_humidity_5min[row])
        self.diff_humidity_10min.append(parent.diff_humidity_10min[row])
        self.diff_humidity_15min.append(parent.diff_humidity_15min[row])
        self.diff_humidity_20min.append(parent.diff_humidity_20min[row])
        self.diff_humidity_25min.append(parent.diff_humidity_25min[row])
        self.s_diff_humidity_5min.append(parent.s_diff_humidity_5min[row])
        self.s_diff_humidity_10min.append(parent.s_diff_humidity_10min[row])
        self.s_diff_humidity_15min.append(parent.s_diff_humidity_15min[row])
        self.s_diff_humidity_20min.append(parent.s_diff_humidity_20min[row])
        self.s_diff_humidity_25min.append(parent.s_diff_humidity_25min[row])
        self.max_co2_last5min.append(parent.max_co2_last5min[row])
        self.min_co2_last5min.append(parent.min_co2_last5min[row])
        self.avg_co2_last5min.append(parent.avg_co2_last5min[row])
        self.stdev_co2_last5min.append(parent.stdev_co2_last5min[row])
        self.max_co2_next5min.append(parent.max_co2_next5min[row])
        self.min_co2_next5min.append(parent.min_co2_next5min[row])
        self.avg_co2_next5min.append(parent.avg_co2_next5min[row])
        self.stdev_co2_next5min.append(parent.stdev_co2_next5min[row])
        self.diff_co2_5min.append(parent.diff_co2_5min[row])
        self.diff_co2_10min.append(parent.diff_co2_10min[row])
        self.diff_co2_15min.append(parent.diff_co2_15min[row])
        self.diff_co2_20min.append(parent.diff_co2_20min[row])
        self.diff_co2_25min.append(parent.diff_co2_25min[row])
        self.s_diff_co2_5min.append(parent.s_diff_co2_5min[row])
        self.s_diff_co2_10min.append(parent.s_diff_co2_10min[row])
        self.s_diff_co2_15min.append(parent.s_diff_co2_15min[row])
        self.s_diff_co2_20min.append(parent.s_diff_co2_20min[row])
        self.s_diff_co2_25min.append(parent.s_diff_co2_25min[row])
        self.max_pm25_last5min.append(parent.max_pm25_last5min[row])
        self.min_pm25_last5min.append(parent.min_pm25_last5min[row])
        self.avg_pm25_last5min.append(parent.avg_pm25_last5min[row])
        self.stdev_pm25_last5min.append(parent.stdev_pm25_last5min[row])
        self.max_pm25_next5min.append(parent.max_pm25_next5min[row])
        self.min_pm25_next5min.append(parent.min_pm25_next5min[row])
        self.avg_pm25_next5min.append(parent.avg_pm25_next5min[row])
        self.stdev_pm25_next5min.append(parent.stdev_pm25_next5min[row])
        self.diff_pm25_5min.append(parent.diff_pm25_5min[row])
        self.diff_pm25_10min.append(parent.diff_pm25_10min[row])
        self.diff_pm25_15min.append(parent.diff_pm25_15min[row])
        self.diff_pm25_20min.append(parent.diff_pm25_20min[row])
        self.diff_pm25_25min.append(parent.diff_pm25_25min[row])
        self.s_diff_pm25_5min.append(parent.s_diff_pm25_5min[row])
        self.s_diff_pm25_10min.append(parent.s_diff_pm25_10min[row])
        self.s_diff_pm25_15min.append(parent.s_diff_pm25_15min[row])
        self.s_diff_pm25_20min.append(parent.s_diff_pm25_20min[row])
        self.s_diff_pm25_25min.append(parent.s_diff_pm25_25min[row])
        self.max_tvoc_last5min.append(parent.max_tvoc_last5min[row])
        self.min_tvoc_last5min.append(parent.min_tvoc_last5min[row])
        self.avg_tvoc_last5min.append(parent.avg_tvoc_last5min[row])
        self.stdev_tvoc_last5min.append(parent.stdev_tvoc_last5min[row])
        self.max_tvoc_next5min.append(parent.max_tvoc_next5min[row])
        self.min_tvoc_next5min.append(parent.min_tvoc_next5min[row])
        self.avg_tvoc_next5min.append(parent.avg_tvoc_next5min[row])
        self.stdev_tvoc_next5min.append(parent.stdev_tvoc_next5min[row])
        self.diff_tvoc_5min.append(parent.diff_tvoc_5min[row])
        self.diff_tvoc_10min.append(parent.diff_tvoc_10min[row])
        self.diff_tvoc_15min.append(parent.diff_tvoc_15min[row])
        self.diff_tvoc_20min.append(parent.diff_tvoc_20min[row])
        self.diff_tvoc_25min.append(parent.diff_tvoc_25min[row])
        self.s_diff_tvoc_5min.append(parent.s_diff_tvoc_5min[row])
        self.s_diff_tvoc_10min.append(parent.s_diff_tvoc_10min[row])
        self.s_diff_tvoc_15min.append(parent.s_diff_tvoc_15min[row])
        self.s_diff_tvoc_20min.append(parent.s_diff_tvoc_20min[row])
        self.s_diff_tvoc_25min.append(parent.s_diff_tvoc_25min[row])
        self.max_no2_last5min.append(parent.max_no2_last5min[row])
        self.min_no2_last5min.append(parent.min_no2_last5min[row])
        self.avg_no2_last5min.append(parent.avg_no2_last5min[row])
        self.stdev_no2_last5min.append(parent.stdev_no2_last5min[row])
        self.max_no2_next5min.append(parent.max_no2_next5min[row])
        self.min_no2_next5min.append(parent.min_no2_next5min[row])
        self.avg_no2_next5min.append(parent.avg_no2_next5min[row])
        self.stdev_no2_next5min.append(parent.stdev_no2_next5min[row])
        self.diff_no2_5min.append(parent.diff_no2_5min[row])
        self.diff_no2_10min.append(parent.diff_no2_10min[row])
        self.diff_no2_15min.append(parent.diff_no2_15min[row])
        self.diff_no2_20min.append(parent.diff_no2_20min[row])
        self.diff_no2_25min.append(parent.diff_no2_25min[row])
        self.s_diff_no2_5min.append(parent.s_diff_no2_5min[row])
        self.s_diff_no2_10min.append(parent.s_diff_no2_10min[row])
        self.s_diff_no2_15min.append(parent.s_diff_no2_15min[row])
        self.s_diff_no2_20min.append(parent.s_diff_no2_20min[row])
        self.s_diff_no2_25min.append(parent.s_diff_no2_25min[row])
        self.datetime.append(parent.datetime[row])
        self.max_datetime_last5min.append(parent.max_datetime_last5min[row])
        self.min_datetime_last5min.append(parent.min_datetime_last5min[row])
        self.max_datetime_next5min.append(parent.max_datetime_next5min[row])
        self.min_datetime_next5min.append(parent.min_datetime_next5min[row])
        self.is_pasto.append(parent.is_pasto[row])
        return
