import numpy as np


class DataSet:
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

        prev_datetime=0
        current_day=1
        rel_for_day=0

        for current_datetime in self.datetime:
            if current_datetime<prev_datetime:
                current_day+=1
            prev_datetime=current_datetime

            if current_day==given_day:
                rel_for_day+=1

        print(rel_for_day)
        return day_data


