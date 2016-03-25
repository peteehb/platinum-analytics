
from BluetoothMonitor import BluetoothMonitor
from utils import DataCollectionUtilities

def main():
    btmon = BluetoothMonitor()

    utils = DataCollectionUtilities(save_locally_to_csv=True, csv_file='SensorReading.csv', save_remote=False)

    fields = ['rssi', 'mac_address', 'timestamp', 'distance']
    csv_outputfile = utils.open_csv_file_writer(fields)

    while True:
        reading = btmon.get_next_reading()

        # Save local
        utils.save_reading_to_csv(csv_outputfile, reading)
        print(reading)

        # Post to DB


if __name__ == '__main__':
    main()
