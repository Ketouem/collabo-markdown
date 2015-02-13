import logging

from flask import render_template
from flask.ext.socketio import emit

from . import main
from .form import PageDownForm
from collabo import socketio

log = logging.getLogger(__name__)

current_markdown = ''


@main.route('/', methods=['GET', 'POST'])
def index():
    pagedown_form = PageDownForm()
    return render_template('index.html', form=pagedown_form)


@socketio.on('connect', namespace='/test')
def on_connect():
    emit('current markdown', {'data': current_markdown})


@socketio.on('markdown edit', namespace='/test')
def markdown_edit(message):
    global current_markdown
    log.info("Markdown Edit event received: {}".format(message))
    current_markdown = message['markdown']
    emit('markdown modification',
         {'data': current_markdown}, broadcast=True)
