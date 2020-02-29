from app import app
from flask import render_template
from flask import request



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/add_box', methods=['GET', 'POST'])
def add_box():
    box_id = request.args.get('box_id')
    return box_id

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
