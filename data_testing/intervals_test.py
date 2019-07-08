

class Intervals_test:

    # per ogni intervallo trovato controllo se contiene un intervallo reale
    def precision_test(self, founded_intervals, real_intervals):

        open_intr = False
        satisfied_intr = False
        satisfied_intr_count = 0

        for i in range(len(founded_intervals)):
            if founded_intervals[i] == 1:
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
        return self.calc_n_intervals(founded_intervals), self.calc_n_intervals(real_intervals), satisfied_intr_count

    # per ogni intervallo reale controllo che ce ne sia almeno uno trovato dentro
    def recall_test(self, founded_intervals, real_intervals):
        open_intr = False
        satisfied_intr = False
        satisfied_intr_count = 0

        for i in range(len(real_intervals)):
            if real_intervals[i] == 1:
                # se ho letto il primo 1 apro l'intervallo
                if not open_intr:
                    open_intr = True
                # se ho un intervallo reale dentro quello trovato
                if founded_intervals[i] == 1 and not satisfied_intr:
                    satisfied_intr = True
                    satisfied_intr_count += 1
            else:
                # chiudo l'intervallo al primo zero che leggo
                if open_intr:
                    open_intr = False
                    satisfied_intr = False
        return self.calc_n_intervals(real_intervals), self.calc_n_intervals(founded_intervals), satisfied_intr_count

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