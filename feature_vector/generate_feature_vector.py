#
#   Author: Mauro Marini
#   Project: tesi
#   feature_vector/generate_feature_vector.py
#
from data_manager.data_prefab import DataPrefab

class FeatureVectorGenerator:

    n_co2_peaks = 10

    def __init__(self, dataset):
        self.dataset = dataset
        return


    def get_data(self, DAY):

        use_incomplete_sample = False
        dataset = DataPrefab.generate_data_from_entire_sample(DataPrefab())

        day_data = DataPrefab.get_data_by_sensor_and_day(dataset, 1, DAY)
        n_rilevazioni = len(day_data.datetime)
        if n_rilevazioni >= 1000 or use_incomplete_sample:
            print(day_data.is_pasto)
            return day_data
        return


    def generate(self):
        return