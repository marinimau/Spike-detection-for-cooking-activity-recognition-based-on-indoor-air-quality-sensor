

class Intervals_test:

    # per ogni intervallo trovato controllo se contiene un intervallo reale
    def count_intervals_test(self, found_intervals, real_intervals):

        open_intr = False
        satisfied_intr = False
        satisfied_intr_count = 0

        for i in range(len(found_intervals)):
            if found_intervals[i] == 1:
                # se ho letto il primo 1 apro l'intervallo
                if not open_intr:
                    open_intr = True
                # se ho un intervallo reale dentro quello trovato
                if real_intervals[i] == 1 and not satisfied_intr:
                    satisfied_intr = True
                    satisfied_intr_count +=1
            else:
                # chiudo l'intervallo al primo zero che leggo
                if open_intr:
                    open_intr = False
                    satisfied_intr = False
        return self.calc_n_intervals(found_intervals), self.calc_n_intervals(real_intervals), satisfied_intr_count

    # calcola il numero di intervalli partndo dalla lista binaria
    def calc_n_intervals(self, intervals):
        open_intr = False
        intr_count = 0

        for intr in intervals:
            if intr == 1:
                # se sono appena entrato
                if not open_intr:
                    open_intr = True
                    intr_count += 1
            else:
                # se sono appena uscito
                if open_intr:
                    open_intr = False
        return intr_count