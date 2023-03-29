from project import db
from project import app

class EventVo(db.Model):
    __tablename__ = 'Event'
    EventId = db.Column('EventId', db.Integer, primary_key = True)
    UserId = db.Column('UserId',db.Integer,nullable=False)
    PostId = db.Column('PostId',db.Integer,nullable=False)
    EventName = db.Column('EventName',db.String(50),nullable=False)
    Visibility= db.Column('Visibility',db.String(50))

with app.app_context():
    db.create_all()
