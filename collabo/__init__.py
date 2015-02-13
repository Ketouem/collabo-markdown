from os.path import dirname, abspath, join

from flask import Flask
from flask.ext.pagedown import PageDown
from flask.ext.socketio import SocketIO

from config import config
from logger import init_logger

pagedown = PageDown()
socketio = SocketIO()


def create_app(config_name='development'):
    conf_path = join(dirname(abspath(__file__)), 'logger', 'logging.conf')
    init_logger(conf_path)

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    pagedown.init_app(app)
    socketio.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
