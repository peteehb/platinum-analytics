import subprocess
import re
import time

from ProcessManager import Process


def get_distance_from_rssi(_rssi):
    rssi_at_one_meter = -40
    pathloss_exponent = 4.2
    distance = 10 * ((rssi_at_one_meter - _rssi) / (10 * pathloss_exponent))
    return round(distance, 2)


def extract_mac_address(line):
    mac_address = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line).group(0)
    return mac_address


def extract_rssi_reading(line):
    linestripped = line.split('RSSI: ')[1]
    rssi_string = re.search(r'^.*?dBm', linestripped).group(0)
    rssi = int(rssi_string.rstrip(' dBm'))
    return rssi


class BluetoothMonitor(object):

    def __init__(self, mon_id):
        self.mon_id = mon_id
        self.bluetooth_scanner = Process('sudo hcitool lescan --duplicates')
        self.bluetooth_monitor = Process('sudo btmon')
        self.ble_reading = {}

    def get_next_reading(self):
        next_reading = False
        while not next_reading:
            line = self.bluetooth_monitor.get_output()
            if line.startswith('> HCI Event'):
                self.ble_reading = {}
            if line.startswith('Address:'):
                self.ble_reading['mac_address'] = extract_mac_address(line)
            if line.startswith('RSSI:'):
                self.ble_reading['rssi'] = extract_rssi_reading(line)
                self.compile_reading()
                next_reading = True
        return self.ble_reading

    def compile_reading(self):
        rssi = self.ble_reading['rssi']
        self.ble_reading['timestamp'] = int(time.time() * 100)
        self.ble_reading['receiver'] = self.mon_id
        self.ble_reading['distance'] = get_distance_from_rssi(rssi)
