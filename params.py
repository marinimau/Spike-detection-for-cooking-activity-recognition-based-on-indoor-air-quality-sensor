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
    # ---------------------------------------------------------------------------
    #  Generare il feature vector
    # ---------------------------------------------------------------------------
    generate_feature_vector = False
    feature_vector_dataset = 2
    # ---------------------------------------------------------------------------
    #  Generare il complete feature vector  --> solo se use_raw_data = True
    # ---------------------------------------------------------------------------
    use_only_cooker_actvity = False
    generate_complete_feature_vector = True
    consider_peaks_weight = False
    # ---------------------------------------------------------------------------
    #  Feature vector params
    # ---------------------------------------------------------------------------
    n_peaks_co2_feature_vector = 7
    n_peaks_tvoc_feature_vector = 7
    n_peaks_pm25_feature_vector = 2
    n_peaks_temp_feature_vector = 1
    n_peaks_humidity_feature_vector = 5
    # ---------------------------------------------------------------------------
    #   Confusion matrix   ---> solo se run_test = True
    # ---------------------------------------------------------------------------
    write_confusion_matrix = True
    # ---------------------------------------------------------------------------
    #  Parametri grafico
    # ---------------------------------------------------------------------------
    draw_chart = False
    print_curve = False
    print_picchi = False
    print_picchi_allineati = True
    # ---------------------------------------------------------------------------
    #  Parametri dati
    # ---------------------------------------------------------------------------
    use_raw_data = True
    auto = True
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
    SENSOR = 2
    DAY = 1
    # ---------------------------------------------------------------------------
    #  Parametri per trovare gli intervalli
    # ---------------------------------------------------------------------------
    max_num_intervals = 7