'''
    Author: Mauro Marini
    Project: tesi
    File: data_manager/data_adapter.py
'''

import numpy as np

def mul(datalist,n):
    results=[]
    for data in datalist:
        results.append(data*n)
    return results