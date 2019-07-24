#
#   Author: Mauro Marini
#   Project: tesi
#   File: confusion_matrix/generate_confusion_matrix.py
#
import csv


class Confusion_matrix:

    def __init__(self):
        self.a_a = 0
        self.a_b = 0
        self.b_a = 0
        self.b_b = 0
        return

    def calculate_confusion_matrix(self, real_intr_bin, found_intr_bin):
        if len(real_intr_bin) == len(found_intr_bin):
            for i in range(0, len(real_intr_bin)):
                if real_intr_bin[i] == 1:
                    if found_intr_bin[i] == 1:
                        self.b_b += 1
                    else:
                        self.b_a += 1
                else:
                    if found_intr_bin[i] == 1:
                        self.a_b += 1
                    else:
                        self.a_a += 1
        return self

    def print_confusion_matrix(self, params):
        with open('confusion_matrix_results/confusion_matrix.txt', mode='a+') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow(["----------------------------------------------------------------------"])
            results_writer.writerow([params])
            results_writer.writerow(["a\t\tb\t<--classified as"])
            results_writer.writerow(["{}\t{}\t\ta".format(self.a_a, self.a_b)])
            results_writer.writerow(["{}\t\t{}\t\tb".format(self.b_a, self.b_b)])
            results_writer.writerow(["\n\n"])
        results_file.close()
        return

    def print_confusion_matrix_no_params(self, file_statistiche):
        with open('risultati_test/stat{}.txt'.format(file_statistiche), mode='a+') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow(["Confusion matrix of dataset:\n\n"])
            results_writer.writerow(["a\t\tb\t<--classified as"])
            results_writer.writerow(["{}\t{}\t\ta".format(self.a_a, self.a_b)])
            results_writer.writerow(["{}\t\t{}\t\tb".format(self.b_a, self.b_b)])
            results_writer.writerow(["\n\n"])
        results_file.close()
        return

    def sum_confusion_matrix(self, other_matrix):
        self.a_a += other_matrix.a_a
        self.a_b += other_matrix.a_b
        self.b_a += other_matrix.b_a
        self.b_b += other_matrix.b_b
        return self

