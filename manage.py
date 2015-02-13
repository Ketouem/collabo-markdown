from flask.ext.script import Shell, Manager

from collabo import create_app

app = create_app()
manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
