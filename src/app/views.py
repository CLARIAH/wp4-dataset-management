from app import app, socketio
from flask import render_template
from client import get_datasets
from flask_socketio import send, emit

ENDPOINT = "YOUR ENDPOINT HERE"

@app.route("/")
def index():
    datasets = get_datasets()

    # app.logger.debug(datasets)
    return render_template('index.html', datasets=datasets, endpoint=ENDPOINT)
