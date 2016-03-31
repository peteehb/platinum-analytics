import os
import requests
import urllib2
import csv
from DataWriter import CsvDataWriter
import config


class SyncLocalFiles(object):
    def __init__(self):
        self.url = 'http://130.255.72.102:8000/sensor-reading/'
        self.local_files_path = format(config.mon_dir, '/readings/')
        self.url_accessible = self.check_url()

    def run(self):
        if self.url_accessible:
            files = self.get_local_files()
            for file in files:
                readings_file_path = self.local_files_path + file
                readings_file = csv.DictReader(open(readings_file_path, 'r'))

                readings_failed_to_post = []

                for reading in readings_file:
                    post_success = self.post_reading(reading)
                    if post_success is False:
                        readings_failed_to_post.append(reading)

                if len(readings_failed_to_post) > 0:
                    failed_readings_writer = CsvDataWriter(rel_path=format(config.mon_dir + '/readings/'), filename='SensorReadingsFailed',
                                                           file_header=readings_file._fieldnames)
                    for reading in readings_failed_to_post:
                        failed_readings_writer.write(data=reading)

                os.remove(readings_file_path)

    def check_url(self):
        url_accessible = False
        try:
            urllib2.urlopen(self.url)
            url_accessible = True
        except Exception, e:
            pass
        return url_accessible

    def get_local_files(self):
        files = []
        for file in os.listdir(self.local_files_path):
            files.append(file)
        return files

    def post_reading(self, reading):
        post_successful = False
        r = requests.post(self.url, data=reading)
        if r.status_code == 201:
            post_successful = True
        return post_successful


if __name__ == '__main__':
    f = SyncLocalFiles()
    f.run()
