#
#   Author: Mauro Marini
#   Project: tesi
#   main.py
#
from data_testing.run_test_in_parallel import Run
from feature_vector.generate_feature_vector import FeatureVectorGenerator
from feature_vector.generate_complete_feature_vector import CompleteFeatureVectorGenerator
from data_manager.data_prefab import DataPrefab
from params import Params

class Main:

    dataset = DataPrefab.generate_data_from_entire_sample(DataPrefab())



    def execute(self):
        if Params.run_test:
            Run.run_in_parallel(Run(self.dataset))
        if Params.generate_feature_vector:
            FeatureVectorGenerator.generate(FeatureVectorGenerator(self.dataset))
        if Params.generate_complete_feature_vector and Params.use_raw_data:
            CompleteFeatureVectorGenerator.generate(CompleteFeatureVectorGenerator(self.dataset))



Main.execute(Main())