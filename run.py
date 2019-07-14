from execute_for_all_sample import Main
from data_manager.data_prefab import DataPrefab
from multiprocessing import Pool
import _thread

dataset = DataPrefab.generate_data_from_entire_sample(DataPrefab())


class Run:

    def test_fun(self, doc, intr_co2, intr_tvoc, intr_pm25, intr_temp, intr_hum, small_intr, large_intr, n_peaks):
        for p_co2 in range(intr_co2[0],intr_co2[1]):
            for p_tvoc in range(intr_tvoc[0], intr_tvoc[1]):
                for p_pm25 in range(intr_pm25[0],intr_pm25[1]):
                    for p_temp in range (intr_temp[0],intr_temp[1]):
                        for p_hum in range (intr_hum[0],intr_hum[1]):
                            for small_intr_tol in range(small_intr[0], small_intr[1]):
                                for large_intr_tol in range(small_intr_tol+1,large_intr[1]):
                                    for n_peaks_large_intr in range(n_peaks[0],n_peaks[1]):
                                        Main.run(Main(), doc, dataset, p_co2, p_tvoc, p_pm25, p_temp, p_hum, small_intr_tol, large_intr_tol, n_peaks_large_intr)
        return

    def f1(self):
        self.test_fun(1, (3, 6), (1, 3), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f2(self):
        self.test_fun(2, (6, 9), (1, 3), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f3(self):
        self.test_fun(3, (9, 12), (1, 3), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f4(self):
        self.test_fun(4, (12, 15), (1, 3), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f5(self):
        self.test_fun(5, (15, 18), (1, 3), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f6(self):
        self.test_fun(6, (18, 21), (1, 3), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f7(self):
        self.test_fun(7, (3, 6), (3, 6), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f8(self):
        self.test_fun(8, (6, 9), (3, 6), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f9(self):
        self.test_fun(9, (9, 12), (3, 6), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f10(self):
        self.test_fun(10, (12, 15), (3, 6), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f11(self):
        self.test_fun(11, (15, 18), (3, 6), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f12(self):
        self.test_fun(12, (18, 21), (3, 6), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f13(self):
        self.test_fun(13, (3, 6), (6, 9), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f14(self):
        self.test_fun(14, (6, 9), (6, 9), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f15(self):
        self.test_fun(15, (9, 12), (6, 9), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f16(self):
        self.test_fun(16, (12, 15), (6, 9), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f17(self):
        self.test_fun(17, (15, 18), (6, 9), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f18(self):
        self.test_fun(18, (18, 21), (6, 9), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f19(self):
        self.test_fun(19, (3, 6), (9, 12), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f20(self):
        self.test_fun(20, (6, 9), (9, 12), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f21(self):
        self.test_fun(21, (9, 12), (9, 12), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f22(self):
        self.test_fun(22, (12, 15), (9, 12), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f23(self):
        self.test_fun(23, (15, 18), (9, 12), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f24(self):
        self.test_fun(24, (18, 21), (9, 12), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f25(self):
        self.test_fun(25, (3, 6), (12, 15), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f26(self):
        self.test_fun(26, (6, 9), (12, 15), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f27(self):
        self.test_fun(27, (9, 12), (12, 15), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f28(self):
        self.test_fun(28, (12, 15), (12, 15), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f29(self):
        self.test_fun(29, (15, 18), (12, 15), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f30(self):
        self.test_fun(30, (18, 21), (12, 15), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f31(self):
        self.test_fun(31, (3, 6), (15, 18), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f32(self):
        self.test_fun(32, (6, 9), (15, 18), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f33(self):
        self.test_fun(33, (9, 12), (15, 18), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f34(self):
        self.test_fun(34, (12, 15), (15, 18), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f35(self):
        self.test_fun(35, (15, 18), (15, 18), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    def f36(self):
        self.test_fun(36, (18, 21), (15, 18), (1, 20), (1, 10), (1, 10), (2, 10), (1, 30), (3, 5))
        return

    # eseguo in parallelo le funzioni
    def run_in_parallel(self):
        pool = Pool()
        pool.apply_async(self.f1)
        pool.apply_async(self.f2)
        pool.apply_async(self.f3)
        pool.apply_async(self.f4)
        pool.apply_async(self.f5)
        pool.apply_async(self.f6)
        pool.apply_async(self.f7)
        pool.apply_async(self.f8)
        pool.apply_async(self.f9)
        pool.apply_async(self.f10)
        pool.apply_async(self.f11)
        pool.apply_async(self.f12)
        pool.apply_async(self.f13)
        pool.apply_async(self.f14)
        pool.apply_async(self.f15)
        pool.apply_async(self.f16)
        pool.apply_async(self.f17)
        pool.apply_async(self.f18)
        pool.apply_async(self.f19)
        pool.apply_async(self.f20)
        pool.apply_async(self.f21)
        pool.apply_async(self.f22)
        pool.apply_async(self.f23)
        pool.apply_async(self.f24)
        pool.apply_async(self.f25)
        pool.apply_async(self.f26)
        pool.apply_async(self.f27)
        pool.apply_async(self.f28)
        pool.apply_async(self.f29)
        pool.apply_async(self.f30)
        pool.apply_async(self.f31)
        pool.apply_async(self.f32)
        pool.apply_async(self.f33)
        pool.apply_async(self.f34)
        pool.apply_async(self.f35)
        pool.apply_async(self.f36)
        return

    def run_in_parallel_thread(self):
        try:
            _thread.start_new_thread(self.f1, None)
            _thread.start_new_thread(self.f2, None)
            _thread.start_new_thread(self.f3, None)
            _thread.start_new_thread(self.f4, None)
            _thread.start_new_thread(self.f5, None)
            _thread.start_new_thread(self.f6, None)
            _thread.start_new_thread(self.f7, None)
            _thread.start_new_thread(self.f8, None)
            _thread.start_new_thread(self.f9, None)
            _thread.start_new_thread(self.f10, None)
            _thread.start_new_thread(self.f11, None)
            _thread.start_new_thread(self.f12, None)
            _thread.start_new_thread(self.f13, None)
            _thread.start_new_thread(self.f14, None)
            _thread.start_new_thread(self.f15, None)
            _thread.start_new_thread(self.f16, None)
            _thread.start_new_thread(self.f17, None)
            _thread.start_new_thread(self.f18, None)
            _thread.start_new_thread(self.f19, None)
            _thread.start_new_thread(self.f20, None)
            _thread.start_new_thread(self.f21, None)
            _thread.start_new_thread(self.f22, None)
            _thread.start_new_thread(self.f23, None)
            _thread.start_new_thread(self.f24, None)
            _thread.start_new_thread(self.f25, None)
            _thread.start_new_thread(self.f26, None)
            _thread.start_new_thread(self.f27, None)
            _thread.start_new_thread(self.f28, None)
            _thread.start_new_thread(self.f29, None)
            _thread.start_new_thread(self.f30, None)
            _thread.start_new_thread(self.f31, None)
            _thread.start_new_thread(self.f32, None)
            _thread.start_new_thread(self.f33, None)
            _thread.start_new_thread(self.f34, None)
            _thread.start_new_thread(self.f35, None)
            _thread.start_new_thread(self.f36, None)
        except:
            print("Errore in run_in_parallel__thread")
        return
