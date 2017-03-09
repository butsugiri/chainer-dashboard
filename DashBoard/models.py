# -*- coding: utf-8 -*-
import json
from datetime import datetime

class LogFile(object):
    def __init__(self, path):
        self.path = path

        raw_datetime = path.split("/")[1]
        self.date = datetime.strptime(raw_datetime, "%Y%m%d_%H_%M_%S")
        self.href = "log/" + raw_datetime

        data = json.load(open(self.path))
        self.epoch = data[-1]['epoch']
        self.elapsed_time = int(data[-1]['elapsed_time'])
