#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_analysis/peaks_detector.py
#

from scipy.signal import find_peaks

def get_peaks(data, distance, width, prominence,num_peaks):
    peaks, _ = find_peaks(data, distance=distance, width=width, prominence=prominence)
    if len(peaks) > num_peaks:
        return get_peaks(data, distance, width, prominence+0.5, num_peaks)
    else:
        return peaks

# il pm 2.5 necessita di una funzione particolare
def get_pm25_peaks(data, height ,num_peaks):
    peaks, _ = find_peaks(data, height=height)
    if len(peaks) > num_peaks:
        return get_pm25_peaks(data, height+2, num_peaks)
    else:
        return peaks