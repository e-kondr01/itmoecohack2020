from app import db

class Building(db.Model):
    __tablename__ = "buildings"
    building_id = db.Column(db.Integer, primary_key=True)
    box_num = db.Column(db.Integer)
    people_num = db.Column(db.Integer)
    def __init__(self, box_num=1, people_num=1000):
        self.box_num = box_num
        self.people_num = people_num


class Place(db.Model):
    __tablename__ = "places"
    place_id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey("buildings.building_id"))
    floor = db.Column(db.Integer)
    otdel = db.Column(db.Text)
    def __init__(self, building_id=None, floor=None, otdel=None):
        self.building_id = building_id
        self.floor = floor
        self.otdel = otdel


class Boxe(db.Model):
    __tablename__ = "boxes"
    box_id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey("places.place_id"))
    is_full = db.Column(db.Boolean, default=False)
    def __init__(self, place_id=None, is_full=False):
        self.place_id = place_id
        self.is_full = is_full

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    box_id = db.Column(db.Integer, db.ForeignKey('boxes.box_id'))
    name = db.Column(db.Text)
    surname = db.Column(db.Text)
    email = db.Column(db.Text)
    phone = db.Column(db.Text)
