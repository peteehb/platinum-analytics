import os
import requests
import urllib2
import csv

class SyncLocalFiles(object):
    def __init__(self):
        self.url = 'http://130.255.72.102:8000/sensor-reading/'
        self.local_files_path = os.path.join(os.getcwd() + '/readings/')
        self.url_accessible = self.check_url()

    def run(self):
        if self.url_accessible:
            files = self.get_local_files()
            for file in files:
                readings_file = csv.DictReader(open(os.path.join(f.local_files_path, file), 'r'))
                all_readings_posted = True
                for reading in readings_file:
                    post_success = self.post_reading(reading)
                    if not post_success:
                        all_readings_posted = False
                        break
                if all_readings_posted:
                    file.close()
                    os.remove(file)

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

if __name__=='__main__':
    f = SyncLocalFiles()
    f.run()
