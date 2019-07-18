#
#   Author: Mauro Marini
#   Project: tesi
#   data_testing/run_test_in_parallel.py
#

from data_testing.execute_for_all_sample import Main
from multiprocessing import Pool

class Run:
    def __init__(self, dataset):
        self.dataset = dataset
        return

    def test_fun(self, doc, intr_co2, intr_tvoc, intr_pm25, intr_temp, intr_hum, small_intr, large_intr, n_peaks):
        for p_co2 in range(intr_co2[0],intr_co2[1]):
            for p_tvoc in range(intr_tvoc[0], intr_tvoc[1]):
                for p_pm25 in range(intr_pm25[0],intr_pm25[1]):
                    for p_temp in range (intr_temp[0],intr_temp[1]):
                        for p_hum in range (intr_hum[0],intr_hum[1]):
                            for small_intr_tol in range(small_intr[0], small_intr[1]):
                                for large_intr_tol in range(small_intr_tol+1,large_intr[1]):
                                    for n_peaks_large_intr in range(n_peaks[0],n_peaks[1]):
                                        Main.run(Main(), doc, self.dataset, p_co2, p_tvoc, p_pm25, p_temp, p_hum, small_intr_tol, large_intr_tol, n_peaks_large_intr)
        return

    def f1(self):
        self.test_fun(1, (4, 5), (3, 4), (2, 3), (1, 2), (1, 2), (7, 8), (14, 15), (3, 4))
        return

    def f2(self):
        self.test_fun(2, (3, 4), (4, 5), (2, 3), (1, 2), (1, 2), (9, 10), (21, 22), (3, 4))
        return

    def f3(self):
        self.test_fun(3, (3, 4), (4, 5), (2, 3), (1, 2), (1, 2), (9, 10), (21, 22), (3, 4))
        return

    def f4(self):
        self.test_fun(4, (15, 16), (7, 8), (1, 2), (1, 2), (2, 3), (9, 10), (10, 11), (3, 4))
        return

    # eseguo in parallelo i test
    def run_in_parallel(self):
        pool = Pool()
        pool.apply_async(self.f1)
        pool.apply_async(self.f2)
        pool.apply_async(self.f3)
        pool.apply_async(self.f4)
        return

