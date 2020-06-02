# Spike detection per il riconoscimento dei pasti in base a sensori di qualità dell’aria

Lo scopo dell'applicazione è quello di costruire un feature vector per la predizione dei pasti in base a valori registrati da sensori di qualità dell'aria.
Le feature prodotte verranno automaticamente unite a feature statistiche già presenti in alcuni files. Per la classificazione utilizzare il Knowledge Flow Enviroment di Weka impostato nel file allegato.
Il feature vector si può considerare composto di due parti:
- la prima, già implementata, viene recuperata in "./data_files/elaborated_data_files/".
- la seconda, invece, contiene le feature legate ai picchi.

L'intera applicazione si concentra sull'implementazione della seconda parte.

## Dataset
L'applicazione contiene al suo interno sia i dataset grezzi, sia i file contenenti le feature già implementate. 
Rispettivamente:

Dati grezzi:
```bash
./data_files/raw_data_files/[NUM_DATASET].csv
```


Feature esistenti:
```bash
./data_files/elaborated_data_files/[NUM_DATASET].csv
```

In entrambi i casi ci si riferisce ai dataset con numeri che vanno da 1 a 8. L'ordine dei dataset è dato dall'ordine alfabetico dei loro nomi orginali:

- uHooB.csv     --> 1.csv
- uHooD.csv     --> 2.csv
- uHooDM.csv    --> 3.csv
- uHooFe.csv    --> 4.csv
- uHooFr.csv    --> 5.csv
- uHooMo.csv    --> 6.csv
- uHooSil.csv   --> 7.csv
- uHooSim.csv   --> 8.csv

è consigliabile non spostare ne rinominare i file.

## Dipendenze

Per il corretto funzionamento, è necessario Python 3. Installare le seguenti liberie:
- cycler
- kiwisolver 
- matplotlip
- numpy
- pandas
- pyparsing 
- python-dateutil 
- pytz 
- scipy 
- six

## Struttura del codice

Il codice è strutturato come segue:

```text
+ root
|
|---+ data analysis
|   |
|   |---+ find_min_dist.py                  # ricerca della distanza dal picco più vicino
|   |
|   |---+ peaks_detector.py                 # funzioni per la ricerca dei picchi
|
|
|---+ data files
|   |
|   |---+ elaborated_data_files             # directory contenente i file con le feature già esistenti
|   |
|   |---+ raw_data_files                    # directory contentente i file con i dati grezzi
|
|
|---+ data_manager
|   |
|   |---+ data prefab.py                    # classe che comanda l'estrazione dei dati grezzi e li divide per giorno
|   |
|   |---+ elaborated_data_extractor.py      # esegue materialmente l'estrazione delle feature esistenti
|   |
|   |---+ raw_data_extractor.py             # esegue materialmente l'estrazione dei dati grezzi
|
|
|---+ feature vector
|   |
|   |---+ generate_peaks_features.py        # classe main per quanto riguarda la creazione delle nuove features 
|
|
|---+ feature_vector_results                # contiene i feature vector finiti (completi di entrambe le parti)
|
|
|---+ merge_feature_vectors
|   |
|   |---+ merge_features.py                 # unisce le feature esistenti con quelle calcolate dall'applicazione
|
|
|---+ peaks_features_results                # contiene le feature legate ai picchi, che poi andranno unite alle features già presenti
|
|
|--+ main.py                                # lancia l'intera applicazione
|
|
|--+ params.py                              # contiene i parametri che consentono di settare l'applicazione

```

## Utilizzo

Tutti i parametri che possono essere modificati, si trovano nel file params.py:


Considerare solo i pasti che utilizzano un fornello:
```text
use_only_cooker_actvity = <bool> 
```

Attribuire un peso ai picchi in base all'ordine in cui vengono trovati:
```text
consider_peaks_weight = <bool>
```

Unire le feature esistenti con quelle calcolate dall'applicazione:
```text
merge_feature_vector = <bool>
```

Specificare quanti picchi per ogni parametro cercare nell'intera giornata:
```text
n_peaks_co2_feature_vector = <int>
n_peaks_tvoc_feature_vector = <int>
n_peaks_pm25_feature_vector = <int>
n_peaks_temp_feature_vector = <int>
n_peaks_humidity_feature_vector = <int>
```

Cercare i picchi solo all'interno degli intervalli di colazione, pranzo e cena:
```text
find_peaks_by_intervals  = <bool>
```

Se i picchi vengono cercati solo nei 3 intervalli, specificare quanti picchi per ogni parametro cercare in ciascun intervallo:
```text
n_peaks_co2_by_interval = <(int, int, int)>
n_peaks_tvoc_by_interval = <(int, int, int)>
n_peaks_pm25_by_interval = <(int, int, int)>
n_peaks_temp_by_interval = <(int, int, int)>
n_peaks_humidity_by_interval = (<(int, int, int)>
```

Specificare il minuto in qui iniziano e finiscono gli intervalli di colazione, pranzo e cena. Per minuto si intende il numero di minuti trascorsi dalla mezzanotte.
```text
colazione = <(int, int)> 
pranzo = <(int, int)>
cena = <(int, int)>
```

Specificare quali dataset usare, basta aggiungere il numero del dataset alla lista.
```text
SENSOR_list = <[int, int, ...]>
```

Specificare i giorni da utilizzare, valgono per tutti i dataset. Il primo intero indica il giorno di partenza, che è compreso. Il secondo intero indica il giorno in cui fermarsi, che non è compreso.
```text
DAY_intr = <(int, int)>
```

Una volta impostati i parametri è sufficiente lanciare l'applicazione. A esecuzione terminata recuperare i feature_vectors nei percorsi indicati.
