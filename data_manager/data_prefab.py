#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_manager/data_prefab.py
#

from data_manager.elaborated_data_extractor import DataSet
from data_manager.raw_data_extractor import RawDataSet
from params import Params

class DataPrefab:
    def __init__(self):
        self.data = []
        return

    def generate_data_from_entire_sample(self):
        for sensor in Params.SENSOR_list:
            for day in range(Params.DAY_intr[0], Params.DAY_intr[1]):
                sensor_data = RawDataSet.extract_data_from_sensor(RawDataSet(), sensor)
                day_data = sensor_data.get_data_by_day(day)
                index = sensor*100+day
                print("Index: {}".format(index))
                self.data += [(index, day_data)]
        return self

    def get_data_by_sensor_and_day(self, sensor, day):
        result = RawDataSet()
        for index, dataset in self.data:
            request = sensor*100+day
            if index == request:
                result = dataset
        return result