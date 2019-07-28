#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_analysis/peaks_detector.py
#

from scipy.signal import find_peaks
from params import Params


def get_peaks(data, distance, width, prominence, num_peaks):
    peaks, _ = find_peaks(data, distance=distance, width=width, prominence=prominence)
    if len(peaks) > num_peaks:
        return get_peaks(data, distance, width, prominence+1, num_peaks)
    else:
        results = []
        # necessario perché numpy restituisce un proprio formato, iterabile ma non concatenabile a una lista normale
        for p in peaks:
            results.append(p)
        return results

def get_peaks_changing_width(data, distance, width, prominence, num_peaks):
    peaks, _ = find_peaks(data, distance=distance, width=width, prominence=prominence)
    if len(peaks) > num_peaks:
        if Params.consider_peaks_weight:
            width += 1
        return get_peaks_changing_width(data, distance, width, prominence+1, num_peaks)
    else:
        results = []
        # necessario perché numpy restituisce un proprio formato, iterabile ma non concatenabile a una lista normale
        for p in peaks:
            results.append(p)
        return results


# il pm 2.5 necessita di una funzione particolare
def get_pm25_peaks(data, height, num_peaks):
    peaks, _ = find_peaks(data, height=height)
    if len(peaks) > num_peaks:
        return get_pm25_peaks(data, height+2, num_peaks)
    else:
        return peaks


def get_peaks_with_weight(data, distance, width, prominence, num_peaks):
    peaks = []
    for i in range(num_peaks + 1):
        found_p = get_peaks_changing_width(data, distance, width, prominence, i)
        peaks += found_p
    return peaks


def split_intervals(data, datetime):
    intr1 = []
    intr2 = []
    intr3 = []
    for i in range(len(datetime)):
        if 440 <= datetime[i] <= 540:
            intr1.append(data[i])
        if 745 <= datetime[i] <= 825:
            intr2.append(data[i])
        if 1135 <= datetime[i] <= 1370:
            intr3.append(data[i])
    return intr1, intr2, intr3