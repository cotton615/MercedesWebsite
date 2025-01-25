from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    img = db.Column(db.String(200), nullable=False)
    carcass = db.Column(db.String(20)) 
    transmission = db.Column(db.String(50))
    engine = db.Column(db.String(100))
    descript = db.Column(db.String(500))
    feature1 = db.Column(db.String(100))
    feature2 = db.Column(db.String(100))
    feature3 = db.Column(db.String(100))
    feature4 = db.Column(db.String(100))
    images = db.relationship('CarImage', back_populates='car')
    
    def __init__(self, model):
        self.model = model

class CarImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    car = db.relationship('Car', back_populates='images')
