from datetime import datetime
import time


def get_timestamp():
    return datetime.fromtimestamp(time.time()).strftime('_%Y_%m_%d_%H_%M_%S')
