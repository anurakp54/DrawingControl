import sqlite3

from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime
from qrcode_reader import qrcode_reader
from base import Session, engine, Base
from class_drawing import drawing
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Runserver using the below command
# python3 app.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drawings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
PATH: str = "/Users/mbpro/PycharmProjects/flask/data/"
STORAGE = "/Users/mbpro/PycharmProjects/flask/Static/"
URL = 'http://127.0.0.1:5000'

db = SQLAlchemy(app)
db.init_app(app)


# in Terminal $ python3
# from app import db
# db.create_all() # it will generate drawings.db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return redirect((url_for('register')))


@app.route('/validate/<string:dwg_num>', methods=["POST","GET"])
def validate(dwg_num):

    data = URL+'/goodforconstruction/' + dwg_num
    img = qrcode.make(data)
    img.save(STORAGE + 'qcode.png')
    img = Image.open(STORAGE + 'qcode.png')
    editable = ImageDraw.Draw(img)
    editable.text((50, img.size[1] - 20), dwg_num, size= 10, fill='black')
    img.save( STORAGE + 'temp_QR.png')
    return redirect(url_for('register'))


@app.route('/goodforconstruction/<string:dwg_num>')
def good_for_construction(dwg_num):
    session: object = Session()
    match_dwg = session.query(drawing).filter(drawing.dwg_num == dwg_num[:-2]).order_by(drawing.created.desc()).first()
    if dwg_num[-2:] == match_dwg.revision:
        session.close()
        return f'<h2>Drawing Number "{dwg_num}" is Good for Construction</h2>'
    else:
        session.close()
        return f'<h2>This drawing is Not Good for Construction</h2>'
@app.route('/goodforconstruction/scanning')
def scanning():
    try:
        drawing_list = qrcode_reader(PATH)
        return f'<h2>{drawing_list} are scanned and stored to database. The original in Network folder was also deleted. </h2>'
    except:
        return f'<h2> The folder is empty</h2>'

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        dwg_num = request.form['dwg_num'] + request.form['rev']
        return redirect(url_for('validate', dwg_num=dwg_num))

    else:
        return render_template('Register.html')

if __name__ == "__main__":
    app.run(debug=True)
