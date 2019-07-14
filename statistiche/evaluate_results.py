#
#   Author: Mauro Marini
#   Project: tesi
#   File: statistiche/evaluate_results.py
#

class Evaluate:
    def precision(self, fi, ri, si):
        if ri == 0 and fi == 0 and si == 0:
            return 1
        elif fi == 0 and ri != 0:
            return 0
        elif fi != 0 and fi == 0:
            return 0
        else:
            return si/fi

    def recall(self, fi, ri, si):
        if ri == 0 and fi == 0 and si == 0:
            return 1
        elif ri == 0 and fi != 0:
            return 0
        elif ri != 0 and si == 0:
            return 0
        else:
            return si/ri