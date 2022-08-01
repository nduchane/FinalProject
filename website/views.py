from flask import Blueprint, render_template, request, flash, redirect
from .models import PersonalComputer, Printer, Phone
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")



@views.route('/pc', methods=['GET', 'POST'])
def pc():
    if request.method == 'POST':
        if request.form.get('submit') == 'Add Asset':
            asset = request.form.get('asset')
            date = request.form.get('date')
            user = request.form.get('user')
            sn = request.form.get('sn')
            try:
                new_asset = PersonalComputer(asset=asset, date=date, user=user, sn=sn)
                db.session.add(new_asset)
                db.session.commit()
                return redirect("pc")
            except:
                return redirect("pc")
        elif request.form.get('submit') != 'Add Asset':
            try:
                deleteid = request.form.get('submit')
                PersonalComputer.query.filter(PersonalComputer.asset == deleteid).delete()
                db.session.commit()
                return redirect("pc")
            except:
                return redirect("pc")
    else:
        data = PersonalComputer.query.order_by(PersonalComputer.asset)
        return render_template("pc.html", data=data)


@views.route('/printer', methods=['GET', 'POST'])
def printer():
    if request.method == 'POST':
        if request.form.get('submit') == 'Add Asset':
            asset = request.form.get('asset')
            date = request.form.get('date')
            sn = request.form.get('sn')
            location = request.form.get('location')
            ipaddress = request.form.get('ipaddress')
            printer = request.form.get('printer')
            try:
                new_asset = Printer(asset=asset, date=date, sn=sn, location=location, ipaddress=ipaddress, printer=printer)
                db.session.add(new_asset)
                db.session.commit()
                return redirect("printer")
            except:
                return redirect("printer")
        elif request.form.get('submit') != 'Add Asset':
            try:
                deleteid = request.form.get('submit')
                Printer.query.filter(Printer.asset == deleteid).delete()
                db.session.commit()
                return redirect("printer")
            except:
                return redirect("printer")
    else:
        data = Printer.query.order_by(Printer.asset)
        return render_template("printer.html", data=data)


@views.route('/phone', methods=['GET', 'POST'])
def phone():
    if request.method == 'POST':
        if request.form.get('submit') == 'Add Asset':
            asset = request.form.get('asset')
            date = request.form.get('date')
            user = request.form.get('user')
            sn = request.form.get('sn')
            phone = request.form.get('phone')
            try:
                new_asset = Phone(asset=asset, date=date, user=user, sn=sn, phone=phone)
                db.session.add(new_asset)
                db.session.commit()
                return redirect("phone")
            except:
                return redirect("phone")
        elif request.form.get('submit') != 'Add Asset':
            try:
                deleteid = request.form.get('submit')
                Phone.query.filter(Phone.asset == deleteid).delete()
                db.session.commit()
                return redirect("phone")
            except:
                return redirect("phone")
    else:
        data = Phone.query.order_by(Phone.asset)
        return render_template("phone.html", data=data)
