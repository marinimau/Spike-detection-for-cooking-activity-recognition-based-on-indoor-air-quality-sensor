#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_manager/data_adapter.py
#


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

def make_avg_of_param(dataset):
    co2 = avg(dataset.avg_co2_last5min, dataset.avg_co2_next5min)
    tvoc = avg(dataset.avg_tvoc_last5min, dataset.avg_tvoc_next5min)
    pm25 = avg(dataset.avg_pm25_last5min, dataset.avg_pm25_next5min)
    temp = avg(dataset.avg_temperature_last5min, dataset.avg_temperature_next5min)
    humidity = avg(dataset.avg_humidity_last5min, dataset.avg_humidity_next5min)
    return co2, tvoc, pm25, temp, humidity