from app import app, socketio

app.debug = True

if __name__ == "__main__":
    socketio.run(app)
