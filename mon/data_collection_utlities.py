import csv
from datetime import datetime
import time
import requests
from requests.exceptions import RequestException, ConnectionError


class DataCollectionUtilities(object):
    def __init__(self, save_locally_to_csv, csv_file, save_remote, remote_url=None):
        self.save_locally_to_csv = save_locally_to_csv or False
        self.csv_file = csv_file
        self.save_remote = save_remote or False
        self.remote_url = remote_url
        self.db_conn = self.check_db_connection()
        self.internet_connection = self.check_internet_connection()

    def check_db_connection(self):
        is_connection_live = False
        if self.remote_url:
            try:
                r = requests.get(self.remote_url)
                if r.status_code == 200:
                    is_connection_live = True
            except RequestException, e:
                print e
        return is_connection_live

    def post_reading(self, data):
        status_code = ''
        if self.db_conn:
            r = requests.post(self.remote_url, data)
            status_code = r.status_code
        return status_code

    def open_csv_file_writer(self, fieldnames):
        csv_name = self.csv_file.split('.csv')[0] + self.get_human_readable_timestamp() + '.csv'
        csvfile = open(csv_name, 'w+')
        try:
            output_csv = csv.DictWriter(csvfile, fieldnames)
            output_csv.writeheader()
        except Exception, e:
            raise RuntimeError("Could not open csv file for writing '{0}'".format(e))
        return output_csv

    def save_reading_to_csv(self, csv_writer, data):
        try:
            csv_writer.writerow(data)
        except csv.Error, e:
            raise RuntimeError("Could not write to local csv file '{0}'".format(e))

    def check_internet_connection(self):
        connection = False
        try:
            response = requests.get('http://example.com')
            if response == 200:
                connection = True
        except requests.exceptions.Timeout, e:
            raise ConnectionError("Connection timed out. '{0}'".format(e))
        except requests.exceptions.TooManyRedirects, e:
            raise ConnectionError("Too many redirects. '{0}'".format(e))
        except requests.exceptions.RequestException, e:
            raise ConnectionError("Connection failed. '{0}'".format(e))
        return connection

    def get_human_readable_timestamp(self):
        return datetime.fromtimestamp(time.time()).strftime('_%Y_%m_%d_%H_%M_%S')
