#
#   Author: Mauro Marini
#   Project: tesi
#   main.py
#
from feature_vector.generate_peaks_features import PeaksFeatureVectorGenerator
from merge_feature_vectors.merge_features import Merge_feature
from data_manager.data_prefab import DataPrefab
from params import Params
import pandas as pd

class Main:

    dataset = DataPrefab.generate_data_from_entire_sample(DataPrefab())



    def execute(self):
        PeaksFeatureVectorGenerator.generate(PeaksFeatureVectorGenerator(self.dataset))
        if Params.merge_feature_vector:
            for dataset in Params.SENSOR_list:
                Merge_feature.merge_by_dataset(Merge_feature(), dataset)



Main.execute(Main())