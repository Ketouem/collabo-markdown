# collabo-markdown

A simple application that provides a collaborative markdown editor using [Flask-SocketIO](https://github.com/miguelgrinberg/flask-socketio) and [Flask-PageDown](https://github.com/miguelgrinberg/flask-pagedown).

## Installation

1. Clone this repository.
`git clone https://github.com/Ketouem/collabo-markdown`
2. Install the depedencies inside a virtualenv.
`pip install -r requirements.txt`

## Run the application

- Directly by invoking gunicorn
`gunicorn --worker-clas socketio.sgunicorn.GeventSocketIOWorker manage:app`
- or by using [Foreman](https://github.com/ddollar/foreman) included in the [Heroku toolbelt](https://toolbelt.heroku.com)
`foreman start`.

## Deployment on Heroku

A Procfile is available to deploy the project on Heroku. In order to push it you have to invoke `heroku create` inside the cloned repository then `git push heroku master`.

## TODOs:

- Include a 'run gunicorn' step inside the manage script
- Smart merge
- Better UI/style
- User management
- Markdown download/upload
