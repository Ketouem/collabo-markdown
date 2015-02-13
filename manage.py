from flask.ext.script import Manager, Server, Command

from collabo import create_app
from collabo import socketio

app = create_app()
manager = Manager(app)


class Run(Command):

    def __init__(self, app):
        self._app = app

    def run(self):
        socketio.run(self._app)

manager.add_command("debug", Server(use_debugger=True, use_reloader=True))
manager.add_command("run", Run(app))

if __name__ == "__main__":
    manager.run()
