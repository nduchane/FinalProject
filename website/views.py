from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>home</h1>"

@views.route('/pc')
def pc():
    return "<h1>pc</h1>"

@views.route('/printer')
def printer():
    return "<h1>printer</h1>"

@views.route('/phone')
def phone():
    return "<h1>phone</h1>"