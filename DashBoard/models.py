# -*- coding: utf-8 -*-
import os
import json
import random
import string
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

class LogFile(object):
    def __init__(self, path):
        self.path = path

        raw_datetime = path.split("/")[-2]
        self.href = raw_datetime
        self.date = datetime.strptime(raw_datetime, "%Y%m%d_%H_%M_%S")

        self.data = json.load(open(self.path))
        self.total_epoch = self.data[-1]['epoch']
        self.total_time = int(self.data[-1]['elapsed_time'])

class ParamFile(object):
    def __init__(self, path):
        self.path = path
        self.data = json.load(open(path))

class TempImage(object):
        def __init__(self, data):
            self.data = data

        def create_png(self, x, y):
            chars = string.digits + string.ascii_lowercase
            self.file_name = ''.join(random.choice(chars) for i in range(64)) + '.png'

            fig, ax = plt.subplots()
            df = pd.DataFrame(self.data)
            df.plot(ax=ax, x=x, y=y, legend=False)
            plt.xlabel(x)
            plt.ylabel(y)

            fig.savefig(os.path.join(os.path.dirname(__file__), 'static', 'images', self.file_name))
            plt.close()
