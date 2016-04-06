from abc import abstractmethod
import csv
import urllib2
import requests
import utils
from utils import join_cwd
from ProcessManager import Process
import config

class DataWriter(object):
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

    @abstractmethod
    def close(self, **kwargs):
        pass


class CsvDataWriter(DataWriter):
    def __init__(self, **kwargs):
        DataWriter.__init__(self, **kwargs)
        self.rel_path = kwargs.get('rel_path')
        self.filename = kwargs.get('filename')
        self.file_header = kwargs.get('file_header')
        self.csv_file = None
        self.file_writer = self.open()
        self.accessible = self.verify_writer_accessible()
        self.write_count = 0
        self.new_file = None
        self.logs_dir = config.mon_dir + '/logs/'
        self.readings_dir = config.mon_dir + '/readings/'

    def open(self):
        self.csv_file = None
        file_writer = None
        timestamp = utils.get_timestamp()
        self.new_file = self.filename + timestamp + '.csv'
        csv_absolute_path = config.mon_dir + self.rel_path + self.new_file
        try:
            self.csv_file = open(csv_absolute_path, 'wb+')
        except Exception, e:
            import ipdb;ipdb.set_trace()
        if self.csv_file:
            try:
                file_writer = csv.DictWriter(self.csv_file, self.file_header)
                file_writer.writeheader()
            except Exception, e:
                raise Exception
        return file_writer

    def verify_writer_accessible(self):
        writer_accessible = False
        try:
            writer = self.open()
        except Exception, e:
            raise Exception
        if writer:
            writer_accessible = True
        return writer_accessible

    def write(self, **kwargs):
        write_success = False
        if self.write_count > 99:
            self.close()
            self.file_writer = self.open()
            self.write_count = 0
        data = kwargs.get('data')
        try:
            self.file_writer.writerow(data)
            write_success = True
            self.write_count += 1
        except Exception, e:
            raise ValueError(e)
        return write_success

    def close(self):
        self.csv_file.close()
        command = 'sudo mv ' + self.rel_path + self.new_file + ' ' + self.readings_dir + self.new_file
        Process(command)


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
                raise Exception
        return write_success

    def close(self):
        pass
