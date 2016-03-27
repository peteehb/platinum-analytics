from datetime import datetime
import time
import os


def get_timestamp():
    return datetime.fromtimestamp(time.time()).strftime('_%Y_%m_%d_%H_%M_%S')

def join_cwd(filename):
    return os.path.join(os.getcwd() + filename)
