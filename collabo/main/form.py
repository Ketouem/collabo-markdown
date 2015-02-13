from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField


class PageDownForm(Form):
    pagedown = PageDownField('Input your markdown')
