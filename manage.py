from flask.ext.script import Manager, Server

from collabo import create_app
from collabo import socketio

app = create_app()
manager = Manager(app)

manager.add_command("debug", Server(use_debugger=True, use_reloader=True))

if __name__ == "__main__":
    socketio.run(app)
    # manager.run()
