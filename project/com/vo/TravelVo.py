from project import db
from project import app

class TravelVo(db.Model):
    __tablename__ = 'Travel'
    TravelId = db.Column('TravelId', db.Integer, primary_key = True)
    UserId = db.Column('UserId',db.Integer,nullable=False)
    PostId = db.Column('PostId',db.Integer,nullable=False)
    Visibility= db.Column('Visibility',db.String(50))

with app.app_context():
    db.create_all()
