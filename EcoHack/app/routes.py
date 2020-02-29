from app import app
from flask import render_template
from flask import request
from app.models import db, Building, Place, Boxe



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/add_box', methods=['GET', 'POST'])
def add_box():
    new_box = Boxe(place_id)
    db.session.add(new_box)
    db.session.commit()
    return "Yay"

@app.route('/delete_box', methods=['GET', 'POST'])
def delete_box():
    box_id = request.args.get('box_id')
    return box_id


@app.route('/box_is_full', methods=['GET', 'POST'])
def box_is_full():
    box_id = request.args.get('box_id')
    return box_id


@app.route('/clear_box', methods=['GET', 'POST'])
def clear_box():
    box_id = request.args.get('box_id')
    return box_id
