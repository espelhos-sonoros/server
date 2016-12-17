from espelhos_sonoros import *

import flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

def main():
    app = flask.Flask('espelhos_sonoros')
    app.config.from_object('config.Config')

    socketio = SocketIO(app)
    db = SQLAlchemy(app)

    espelhos_sonoros(app, socketio, db)

    socketio.run(app, host='0.0.0.0')

if __name__ == '__main__':
    main()
