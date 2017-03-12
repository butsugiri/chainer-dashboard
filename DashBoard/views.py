"""
Routes and views for the flask application.
"""
import os
import glob
import random
import json
from flask import render_template, url_for, jsonify, request, send_file

from DashBoard import app
from .settings import APP_STATIC
from .models import LogFile, ParamFile, TempImage


@app.route('/')
def root_page():
    """Renders the home page."""
    log_files = [LogFile(x) for x in sorted(glob.glob("result/*/log"))]

    return render_template(
        'index.jinja2',
        log_files=log_files,
    )


@app.route('/log/<date_time>')
def show_log(date_time):
    path = os.path.join(os.getcwd(), "result", date_time, "log")
    log_file = LogFile(path)
    labels = sorted([x.replace("/", "-") for x in log_file.data[0].keys() if x != 'epoch' and x != 'iteration'])

    path = os.path.join(os.getcwd(), "result", date_time, "settings.json")
    param_file = ParamFile(path)

    epoch_so_far = len(log_file.data)
    total_epoch = param_file.data['epoch']
    return render_template(
        'detail.jinja2',
        param_file=param_file,
        date_time=date_time,
        labels=labels,
        epoch_so_far=epoch_so_far,
        total_epoch=total_epoch
    )

@app.route('/plot', methods=["POST"])
def plot_graph():
    posted_data = json.loads(request.data.decode('utf-8'))
    path = os.path.join(os.getcwd(), "result", posted_data['dateTime'], "log")
    log_file = LogFile(path)

    img = TempImage(log_file.data)
    img.create_png(x='epoch', y=posted_data['yAxis'].replace("-", "/"))

    return json.dumps(url_for("static", filename=os.path.join('images', img.file_name)))

@app.route('/details', methods=["POST"])
def details():
    posted_data = json.loads(request.data.decode('utf-8'))
    path = os.path.join(os.getcwd(), "result", posted_data['dateTime'], "log")
    log_file = LogFile(path)
    key = posted_data["yAxis"].replace("-", "/")
    out = [x[key] for x in log_file.data]
    return json.dumps(out)
