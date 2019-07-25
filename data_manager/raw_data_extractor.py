#
#   Author: Mauro Marini
#   Project: tesi
#   File: data_manager/raw_data_extractor.py
#

import csv

class RawDataSet:

    def __init__(self):
        self.datetime = []
        self.temperature = []
        self.humidity = []
        self.pm25 = []
        self.tvoc = []
        self.co2 = []
        self.co = []
        self.pressure = []
        self.ozone = []
        self.no2 = []
        self.activity = []
        self.caffe = []
        self.croissant = []
        self.pasta = []
        self.legumi = []
        self.piatti_freddi = []
        self.sugo = []
        self.panino = []
        self.carne_in_padella = []
        self.carne_in_umido = []
        self.merendina = []
        self.latte = []
        self.verdure_cotte = []
        self.pesce = []
        self.yogurt = []
        self.riso = []
        self.window = []
        self.fornello = []
        self.altro = []
        self.micronde = []
        return

    def convert_daytime(self, datetime_string):
        converted_daytime = 0
        splited=datetime_string.split(' ', -1)
        time = splited[1]
        time_splitted = time.split(':', -1)
        hh = int(time_splitted[0])
        mm = int(time_splitted[1])
        converted_daytime = hh*60 + mm
        return converted_daytime

    # extracts all data of given sensor
    def extract_data_from_sensor(self, sensor):
        with open('data_files/raw_data_files/{}.csv'.format(sensor), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.datetime.append(self.convert_daytime(row[0]))
                self.temperature.append(float(row[1]))
                self.humidity.append(float(row[2]))
                self.pm25.append(float(row[3]))
                self.tvoc.append(float(row[4]))
                self.co2.append(float(row[5]))
                self.co.append(float(row[6]))
                self.pressure.append(float(row[7]))
                self.ozone.append(float(row[8]))
                self.no2.append(float(row[9]))
                self.activity.append(row[10])
                self.caffe.append(float(row[11]))
                self.croissant.append(float(row[12]))
                self.pasta.append(float(row[13]))
                self.legumi.append(float(row[14]))
                self.piatti_freddi.append(float(row[15]))
                self.sugo.append(float(row[16]))
                self.panino.append(float(row[17]))
                self.carne_in_padella.append(float(row[18]))
                self.carne_in_umido.append(float(row[19]))
                self.merendina.append(float(row[20]))
                self.latte.append(float(row[21]))
                self.verdure_cotte.append(float(row[22]))
                self.pesce.append(float(row[23]))
                self.yogurt.append(float(row[24]))
                self.riso.append(float(row[25]))
                self.window.append(row[26])
                self.fornello.append(float(row[27]))
                self.altro.append(float(row[28]))
                self.micronde.append(float(row[29]))

            return self

    # split dataset object and returns data of one given day
    def get_data_by_day(self, given_day):
        day_data = RawDataSet()

        prev_datetime = 0  # init the prev daytime
        current_day = 1  # save the current day
        rel_for_day = 0  # count the number rows for each day
        current_row = 0  # references all the rows

        for current_datetime in self.datetime:
            if current_datetime < prev_datetime:
                current_day += 1
            prev_datetime = current_datetime

            if current_day == given_day:
                rel_for_day += 1
                day_data.add_tuple(self, current_row)
            current_row += 1
        print("Tuple presenti nel campione: {}".format(rel_for_day))
        return day_data


    def add_tuple(self, parent, row):
        self.datetime.append(parent.datetime[row])
        self.temperature.append(parent.temperature[row])
        self.humidity.append(parent.humidity[row])
        self.pm25.append(parent.pm25[row])
        self.tvoc.append(parent.tvoc[row])
        self.co2.append(parent.co2[row])
        self.co.append(parent.co[row])
        self.pressure.append(parent.pressure[row])
        self.ozone.append(parent.ozone[row])
        self.no2.append(parent.no2[row])

        if parent.activity[row] != 'None':
            self.activity.append(1)
        else:
            self.activity.append(0)

        self.caffe.append(parent.caffe[row])
        self.croissant.append(parent.croissant[row])
        self.pasta.append(parent.pasta[row])
        self.legumi.append(parent.legumi[row])
        self.piatti_freddi.append(parent.piatti_freddi[row])
        self.sugo.append(parent.sugo[row])
        self.panino.append(parent.panino[row])
        self.carne_in_padella.append(parent.carne_in_padella[row])
        self.carne_in_umido.append(parent.carne_in_umido[row])
        self.merendina.append(parent.merendina[row])
        self.latte.append(parent.latte[row])
        self.verdure_cotte.append(parent.verdure_cotte[row])
        self.pesce.append(parent.pesce[row])
        self.yogurt.append(parent.yogurt[row])
        self.riso.append(parent.riso[row])
        self.window.append(parent.window[row])
        self.fornello.append(parent.fornello[row])
        self.altro.append(parent.altro[row])
        self.micronde.append(parent.micronde[row])
        return
