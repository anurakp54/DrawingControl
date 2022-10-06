import sqlite3

from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime
import qrcode
from qrcode_reader import qrcode_reader
# Runserver using the below command
# python3 app.py

app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drawings.db'
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
PATH: str = "/Users/mbpro/PycharmProjects/flask/data/"

db = SQLAlchemy(app1)
db.init_app(app1)

# in Terminal $ python3
# from app1 import db
# db.create_all() # it will generate drawings.db

class drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dwg_num = db.Column(db.String(12))
    revision = db.Column(db.String(3))
    created = db.Column(db.Date, default=datetime.utcnow())

    def __init__(self, dwg_num, revision, created):
        self.dwg_num = dwg_num
        self.revision = revision
        self.date = created

    def __repr__(self):
        return f'<dwg number: {self.dwg_num}>'

@app1.route('/')
def home():
    return render_template('home.html')


@app1.route('/validate/<string:dwg_num>', methods = ["POST", "GET"])
def validate(dwg_num):
    data = "http://127.0.0.1:5000/goodforconstruction/"+dwg_num
    img = qrcode.make(data)
    img.save('/Users/mbpro/PycharmProjects/flask/static/temp_QR.png')
    return redirect(url_for('register'))

@app1.route('/goodforconstruction/<string:dwg_num>')
def good_for_construction(dwg_num):
    #open the database and check if dwg_num is found in the database.
    return f'<h1>Drawing Number "{dwg_num}" is Good for Construction</h1>'

@app1.route('/goodforconstruction/scanning')
def scanning():
    drawing_list = qrcode_reader(PATH)
    return f'<h1>{drawing_list} are scanned to the folder </h1>'


@app1.route('/register', methods =["POST", "GET"])
def register():
    if request.method =="POST":
        dwg_num = request.form['dwg_num']+request.form['rev']
        return redirect(url_for('validate', dwg_num = dwg_num))

    else:

        return render_template('Register.html')

if __name__ == "__main__":
    app1.run(debug=True)
