#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_manager/data_adapter.py
#

import numpy as np

def mul(datalist, n):
    results=[]
    for data in datalist:
        results.append(data*n)
    return results

def avg(datalist1, datalist2):
    results=[]
    i=0
    for data in datalist1:
        results.append((datalist1[i]+datalist2[i])/2)
        i+=1
    return results