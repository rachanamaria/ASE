from project import db
from project import app

class UserRelationsVo(db.Model):
    __tablename__ = 'User_relations'
    UserId = db.Column('UserId', db.Integer, primary_key = True)
    User2Id = db.Column('User2Id',db.Integer,nullable=False,primary_key = True)
    Relation = db.Column('Relation',db.Integer,nullable=False,primary_key = True)

with app.app_context():
    db.create_all()
