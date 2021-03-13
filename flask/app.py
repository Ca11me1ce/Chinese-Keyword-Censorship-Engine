# Flask application to display model
from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/')
def query_connect():
    print("Conneted to the server")


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=8080, debug=True)