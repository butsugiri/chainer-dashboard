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

    path = os.path.join(os.getcwd(), "result", date_time, "settings.json")
    param_file = ParamFile(path)

    return render_template(
        'detail.jinja2',
        param_file=param_file,
        date_time=date_time
    )
    # with open(path, 'r') as fi:
    #     return fi.read()

@app.route('/plot', methods=["POST"])
def plot_graph():
    posted_data = json.loads(request.data.decode('utf-8'))
    path = os.path.join(os.getcwd(), "result", posted_data['dateTime'], "log")
    log_file = LogFile(path)

    img_name = 'hoge.png'
    x = 'epoch'
    y = 'main/loss'

    with TempImage(img_name, log_file.data, x, y) as img:
        img.create_png()
        return json.dumps(url_for("static", filename=os.path.join('image', img_name)))
