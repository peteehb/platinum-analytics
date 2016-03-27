import os
import sys
from ProcessManager import Process
from BluetoothMonitor import BluetoothMonitor
import urllib2
from DataWriter import CsvDataWriter, DatabaseDataWriter
import settings

class StartProgram(object):
    def __init__(self, ble_mon_id, run_locally):
        self.ble_mon_id = ble_mon_id
        self.run_locally = run_locally
        self.monitor = BluetoothMonitor(mon_id=ble_mon_id)

        internet = self.check_connection_to_internet()
        if internet and not run_locally:
            self.writer = DatabaseDataWriter(remote_url='http://130.255.72.102:8000/sensor-reading/')
        else:
            self.writer = CsvDataWriter(rel_path='/logs/', filename='SensorReadings',
                                        file_header=['rssi', 'mac_address', 'timestamp', 'distance', 'receiver'])

    def run(self):
        if self.writer.verify_writer_accessible():
            while True:
                reading = self.monitor.get_next_reading()
                reading_saved = self.writer.write(data=reading)
                if not reading_saved:
                    import ipdb;ipdb.set_trace()
                    break
                print reading

    def check_connection_to_internet(self):
        con = Process('sudo ifconfig wlan0 up')
        dhclient = Process('sudo dhclient')
        conn_established = False
        internet_established = False
        p = Process('sudo ip route ls')
        if p.get_error():
            conn_established = False
        if p.get_output():
            conn_established = True

        if conn_established:
            try:
                response = urllib2.urlopen('http://216.58.198.68')
                if response:
                    internet_established = True
            except urllib2.URLError:
                pass

        return internet_established


def exit(rc=1):
    os._exit(rc)


def cli():
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        exit()

    ble_mon_id = sys.argv[1]
    run_locally = sys.argv[2]

    bluetooth_monitor = StartProgram(ble_mon_id=ble_mon_id, run_locally=run_locally)
    bluetooth_monitor.run()

if __name__ == '__main__':
    cli()
