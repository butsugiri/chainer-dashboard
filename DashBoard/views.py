"""
Routes and views for the flask application.
"""
import os
import glob
import random
import json
from flask import render_template, url_for, jsonify, request

from DashBoard import app
from .settings import APP_STATIC
from .models import LogFile


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
    with open(path, 'r') as fi:
        return fi.read()
