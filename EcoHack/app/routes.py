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
def delete_box(id: int) -> None:
    """Удаляет коробку из базы данных """
    box = Box.query.get(id)
    db.session.delete(box)
    db.session.commit()


@app.route('/box_is_full', methods=['GET', 'POST'])
def box_is_full(id: int) -> None:
    box = Box.query.get(id)
    box.is_full = True
    db.session.commit()


@app.route('/clear_box', methods=['GET', 'POST'])
def clear_box(id: int) -> None:
    box = Box.query.get(id)
    box.is_full = False
    db.session.commit()
