import subprocess
import re
import time


class BluetoothMonitor(object):

    def __init__(self):
        self.bluetooth_monitor_process = subprocess.Popen('sudo btmon', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        self.bluetooth_scan_process = subprocess.Popen('sudo hcitool lescan', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)

    def read_stdout(self, process):
        line = process.stdout.readline().lstrip()
        return line

    def read_stderr(self, process):
        line = process.stderr.readline().lstrip()
        return line

    def write_stdin(self, process, input):
        process.stdin.writeline(input)

    def get_next_reading(self):
        next_reading = False
        data = {}
        while not next_reading:
            line = self.read_stdout(self.bluetooth_monitor_process)
            if line.startswith('> HCI Event'):
                data = {}
            if line.startswith('Address:'):
                data['mac_address'] = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line).group(0)
            if line.startswith('RSSI:'):
                linestripped = line.split('RSSI: ')[1]
                rssi_string = re.search(r'^.*?dBm', linestripped).group(0)
                rssi = int(rssi_string.rstrip(' dBm'))
                data['rssi'] = rssi
                data['timestamp'] = int(time.time() * 100)
                data['distance'] = self.get_distance_from_rssi(rssi)
                next_reading = True
        return data

    def get_distance_from_rssi(self, _rssi):
        rssi_at_one_meter = -40
        pathloss_exponent = 4.2
        distance = 10 * ((rssi_at_one_meter - _rssi) / (10 * pathloss_exponent))
        return round(distance, 2)
