from project import db
from project import app

class PostVo(db.Model):
    __tablename__ = 'postMaster'
    PostId=db.Column('PostId', db.Integer, primary_key = True)
    CreatorId = db.Column(db.Integer,nullable=False)
    MediaType=db.Column('MediaType',db.String(100))
    type=db.Column('type',db.String(100))
    createdTime=db.Column(db.DateTime(timezone=True))
    UserName = db.Column('UserName',db.String(50))  
    PostDescription=db.Column('PostDescription',db.String(500))

with app.app_context():
    db.create_all()
