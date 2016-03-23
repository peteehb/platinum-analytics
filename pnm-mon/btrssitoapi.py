import subprocess
import requests
import re
import time
import csv


class Bluetooth_RSSI_Reader(object):

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def run(self):

        proc = subprocess.Popen('sudo btmon', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        while True:
            line = proc.stdout.readline().lstrip()
            if line.startswith('> HCI Event'):
                print line
            if line.startswith('Address:'):
                mac_address = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line).group(0)
                print mac_address
            if line.startswith('RSSI:'):
                line = line.split('RSSI: ')[1]
                import ipdb; ipdb.set_trace()
                rssi_str = re.search(r'^.*?dBm', line).group(0)
                rssi = int(rssi_str.rstrip(' dBm'))
                print rssi
                t1 = int(time.time() * 100)
                self.post_reading(rssi, mac_address, t1)

    def post_reading(self, _rssi, _mac_address, t1):
        distance = self.rssi_to_meters(_rssi)
        data = {"rssi": _rssi,
                "mac_address": _mac_address,
                "timestamp": t1,
                "receiver": 1,
                "distance": distance}

        r = requests.post("http://127.0.0.1:8000/sensor-reading/", data=data)
        print r.status_code

    def save_reading_to_local_file(self, _rssi, _mac_address, t1, output_csv):
        distance = self.rssi_to_meters(_rssi)

        output_csv.writerow(
            {"rssi": _rssi,
             "mac_address": _mac_address,
             "timestamp": t1,
             "receiver": 1,
             "distance": distance
             }
        )

    def open_output_csv_file(out_file):
        try:
            output_csv = csv.DictReader(out_file)
        except Exception, e:
            raise RuntimeError("Could not open csv file for writing, '{0}'".format(e))
        return output_csv

    def rssi_to_meters(self, _rssi):
        rssi_at_one_meter = -40
        pathloss_exponent = 2.2
        distance = 10 * ((rssi_at_one_meter - _rssi) / (10 * pathloss_exponent))
        return round(distance, 2)
