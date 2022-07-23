from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/pc')
def pc():
    return render_template("pc.html")


@views.route('/printer')
def printer():
    return render_template("printer.html")


@views.route('/phone')
def phone():
    return render_template("phone.html")
