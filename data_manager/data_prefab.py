#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_manager/data_prefab.py
#

from data_manager.data_extractor import DataSet

class DataPrefab:
    def __init__(self):
        self.data = []
        return

    def generate_data_from_entire_sample(self):
        for sensor in range(1, 9):
            for day in range(16, 22):
                sensor_data = DataSet.extract_data_from_sensor(DataSet(), sensor)
                day_data = sensor_data.get_data_by_day(day)
                index = sensor*100+day
                print("Index: {}".format(index))
                self.data += [(sensor*100+day, day_data)] # simile alla numerazione delle camere degli alberghi
        return self


    def get_data_by_sensor_and_day(self,sensor, day):
        result = DataSet()
        for index, dataset in self.data:
            request = sensor*100+day
            if index == request:
                result = dataset
        return result