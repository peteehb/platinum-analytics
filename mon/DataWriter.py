from abc import abstractmethod
import csv
import urllib2
import requests
import utils

class DataWriter:

    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def open(self, **kwargs):
        pass

    @abstractmethod
    def verify_writer_accessible(self, **kwargs):
        pass

    @abstractmethod
    def write(self, **kwargs):
        pass


class CsvDataWriter(DataWriter):

    def __init__(self, **kwargs):
        DataWriter.__init__(self, **kwargs)
        self.filename = kwargs.get('filename')
        self.file_header = kwargs.get('file_header')
        self.file_writer = self.open()
        self.accessible = self.verify_writer_accessible()

    def open(self):
        csv_file = None
        file_writer = None
        timestamp = utils.get_timestamp()
        new_file = self.filename + timestamp
        try:
            csv_file = open('logs/' + new_file, 'w+')
        except Exception, e:
            pass

        if csv_file:
            try:
                file_writer = csv.DictWriter(csv_file, self.file_header)
                file_writer.writeheader()
            except Exception, e:
                pass
        return file_writer

    def verify_writer_accessible(self):
        writer_accessible = False
        writer = self.open()
        if writer:
            writer_accessible = True
        return writer_accessible

    def write(self, **kwargs):
        write_success = False
        data = kwargs.get('data')
        try:
            self.file_writer.writerow(data)
            write_success = True
        except Exception, e:
            pass
        return write_success


class DatabaseDataWriter(DataWriter):

    def __init__(self, **kwargs):
        DataWriter.__init__(self, **kwargs)
        self.remote_url = kwargs.get('remote_url')
        self.accessible = self.verify_writer_accessible()

    def open(self, **kwargs):
        pass

    def verify_writer_accessible(self, **kwargs):
        db_accessible = False
        if self.remote_url:
            try:
                response = urllib2.urlopen(self.remote_url)
                if response:
                    db_accessible = True
            except urllib2.URLError:
                pass
        return db_accessible

    def write(self, **kwargs):
        write_success = False
        data = kwargs.get('data')
        if self.accessible:
            try:
                r = requests.post(self.remote_url, data)
                if r.status_code == 201:
                    write_success = True
            except Exception, e:
                pass
        return write_success
