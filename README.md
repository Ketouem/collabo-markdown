# collabo-markdown

## Installation

1. Clone this repository
`git clone https://github.com/Ketouem/collabo-markdown`
2. Install the depedencies inside a virtualenv
`pip install -r requirements.txt`
3. Run the application
`gunicorn --worker-clas socketio.sgunicorn.GeventSocketIOWorker manage:app`

## Deployment on Heroku

A Procfile is available to deploy the project on Heroku. In order to push it you have to invoke `heroku create` inside the cloned repository then `git push heroku master`