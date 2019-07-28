#
#   Author: Mauro Marini
#   Project: tesi
#   params.py
#

class Params:
    # ---------------------------------------------------------------------------
    #  Lanciare i test
    # ---------------------------------------------------------------------------
    run_test = False
    auto_run = True
    # ---------------------------------------------------------------------------
    #  Generare il feature vector
    # ---------------------------------------------------------------------------
    generate_feature_vector = False
    feature_vector_dataset = 2
    # ---------------------------------------------------------------------------
    #  Generare il complete feature vector  --> solo se use_raw_data = True
    # ---------------------------------------------------------------------------
    use_only_cooker_actvity = False
    generate_complete_feature_vector = False
    consider_peaks_weight = False
    evaluate_distance_in_complete_feature_vector = True  # questo
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
    n_peaks_co2_by_interval = (1, 1, 1)
    n_peaks_tvoc_by_interval = (1, 1, 1)
    n_peaks_pm25_by_interval = (1, 1, 1)
    n_peaks_temp_by_interval = (1, 1, 1)
    n_peaks_humidity_by_interval = (1, 1, 1)
    # ---------------------------------------------------------------------------
    #   Confusion matrix   ---> solo se run_test = True
    # ---------------------------------------------------------------------------
    write_confusion_matrix = True
    # ---------------------------------------------------------------------------
    #  Parametri grafico
    # ---------------------------------------------------------------------------
    draw_chart = False
    print_curve = False
    auto = True
    print_picchi = False
    print_picchi_allineati = True
    # ---------------------------------------------------------------------------
    #  Parametri dati
    # ---------------------------------------------------------------------------
    use_raw_data = True
    use_incomplete_sample = False
    use_avg = True
    # ---------------------------------------------------------------------------
    #  Intervallo dati
    # ---------------------------------------------------------------------------
    SENSOR_intr = (2, 3)
    DAY_intr = (1, 32)
    # ---------------------------------------------------------------------------
    #  Dati per singola misurazione
    # ---------------------------------------------------------------------------
    SENSOR = SENSOR_intr[0]
    DAY = 1
    # ---------------------------------------------------------------------------
    #  Parametri per trovare gli intervalli
    # ---------------------------------------------------------------------------
    max_num_intervals = 7