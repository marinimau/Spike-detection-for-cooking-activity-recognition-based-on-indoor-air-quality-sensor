#
#   Author: Mauro Marini
#   Project: tesi
#   params.py
#

class Params:
    # ---------------------------------------------------------------------------
    #  Generare il complete feature vector
    # ---------------------------------------------------------------------------
    use_only_cooker_actvity = False
    consider_peaks_weight = True
    merge_feature_vector = True
    # ---------------------------------------------------------------------------
    #  Feature vector params
    # ---------------------------------------------------------------------------
    n_peaks_co2_feature_vector = 7
    n_peaks_tvoc_feature_vector = 7
    n_peaks_pm25_feature_vector = 2
    n_peaks_temp_feature_vector = 1
    n_peaks_humidity_feature_vector = 5
    # ---------------------------------------------------------------------------
    #  Find peaks by interval
    # ---------------------------------------------------------------------------
    find_peaks_by_intervals = True
    n_peaks_co2_by_interval = (1, 1, 1)  # default 1, 1, 1
    n_peaks_tvoc_by_interval = (1, 1, 1)  # default 1, 1, 1
    n_peaks_pm25_by_interval = (1, 1, 1)  # default 1, 1, 1
    n_peaks_temp_by_interval = (1, 1, 1)  # default 1, 1, 1
    n_peaks_humidity_by_interval = (1, 1, 1)  # default 1, 1, 1
    # ---------------------------------------------------------------------------
    #   Intervalli pasto
    # ---------------------------------------------------------------------------
    colazione = (440, 540)  # default (440, 540)
    pranzo = (740, 825)  # default (745, 825)
    cena = (1135, 1370)  # default (1135, 1370)
    # ---------------------------------------------------------------------------
    #  Intervallo dati
    # ---------------------------------------------------------------------------
    SENSOR_list = [2]  # [1, 2, 3, 4, 5, 6, 7, 8]
    DAY_intr = (1, 41)