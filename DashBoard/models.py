# -*- coding: utf-8 -*-
import os
import json
import random
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
        def __init__(self, file_name, data, x, y):
            self.file_name = file_name
            self.data = data
            self.x = x
            self.y = y

        def create_png(self):
            fig, ax = plt.subplots()
            ax.set_title(u'hogehoge')

            df = pd.DataFrame(self.data)
            df.plot(ax=ax, x=self.x, y=self.y)

            # ax.plot(x_ax, y_ax)
            fig.savefig(os.path.join(os.path.dirname(__file__), 'static', 'image', self.file_name))

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass
