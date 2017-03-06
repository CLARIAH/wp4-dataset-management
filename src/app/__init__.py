from flask import Flask
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

socketio = SocketIO(app)


import views
