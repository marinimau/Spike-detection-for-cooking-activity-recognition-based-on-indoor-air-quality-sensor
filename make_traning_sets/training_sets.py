#
#   Author: Mauro Marini
#   Project: tesi
#   File: make_training_sets/training.set
#

from params import Params


class TrainingSet:

    def make_training_set_for_dataset(self, dataset):
        skip_header = False
        for i in range(1, 9):
            if dataset != i:
                training_set = open("training_sets_results/without_{}.csv".format(dataset), "a+")
                if skip_header:
                    f = open("feature_vector_results/by_dataset/peaks_feature_{}.csv".format(i))
                    next(f, None)
                    for line in f:
                        training_set.write(line)
                    f.close()
                    skip_header = True
                else:
                    for line in open("feature_vector_results/by_dataset/peaks_feature_{}.csv".format(i)):
                        training_set.write(line)
                training_set.close()
        return

    def make_all_training_sets(self):
        for dataset in Params.SENSOR_list:
            self.make_training_set_for_dataset(dataset)
        return