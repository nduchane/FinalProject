from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/pc')
def pc():
    return "<h1>pc</h1>"

@views.route('/printer')
def printer():
    return "<h1>printer</h1>"

@views.route('/phone')
def phone():
    return "<h1>phone</h1>"