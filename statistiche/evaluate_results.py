class Evaluate:
    def evaluate_results(self, fi, ri, si):
        if ri == 0 and fi == 0 and si == 0:
            return 1
        elif ri == 0 and fi != 0:
            return 0
        elif ri != 0 and si == 0:
            return 0
        else:
            return si/ri