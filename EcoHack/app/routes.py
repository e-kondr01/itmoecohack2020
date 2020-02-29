from app import app
from flask import render_template
from flask import request
from flask import make_response
from app.models import db, Building, Place, Boxe



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/add_box', methods=['GET', 'POST'])
def add_box():
    place_id = request.args.get('place_id')
    new_box = Boxe(place_id)
    db.session.add(new_box)
    db.session.commit()
    return "Yay"

@app.route('/delete_box', methods=['GET', 'POST'])
def delete_box():
    box_id = request.args.get('box_id')
    box = db.session.query(Boxe).filter(Boxe.box_id == box_id).first()
    if not box is None:
        db.session.delete(box)
        db.session.commit()
        return make_response(jsonify({'Fine': 'Deleted'}), 200)
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/box_is_full', methods=['GET', 'POST'])
def box_is_full():
    box_id = request.args.get('box_id')
    box = db.session.query(Boxe).filter(Boxe.box_id == box_id).first()
    box.is_full = True
    db.session.commit()
    return box_id


@app.route('/clear_boxes', methods=['GET', 'POST'])
def clear_boxes():
    building_id = request.args.get('building_id')
    places = db.session.query(Place).filter(Place.building_id == building_id).all()
    for place in places:
        boxes = db.session.query(Boxe).filter(Boxe.place_id == place.place_id).all()
        for box in boxes:
            clear_a_box(box)
    return make_response(jsonify({'Done': 'Done'}), 404)


def clear_a_box(box):
    box.is_full = False
    db.session.commit()

@app.route('/get_boxes')
def get_boxes():
    boxes = db.session.query(Boxe).all()
    array = []
    for boxe in boxes:
        box = {}
        box['id'] = boxe.box_id
        box['is_full'] = boxe.is_full
        array.append(box)
    return str(array)
