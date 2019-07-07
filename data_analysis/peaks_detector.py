#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_analysis/peaks_detector.py
#

from scipy.signal import find_peaks

def get_peaks(data, prominence,num_peaks):
    peaks, _ = find_peaks(data, prominence=prominence)
    if len(peaks) > num_peaks:
        return get_peaks(data, prominence+1,num_peaks)
    else:
        return peaks