from datetime import datetime
from models.models import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # 'lost' or 'found'
    category = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(255), nullable=False)
    date_reported = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_item = db.Column(db.Date, nullable=False)
    photo_url = db.Column(db.String(255))
    status = db.Column(db.String(20), default='open')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('items', lazy=True))