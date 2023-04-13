from project import db
from project import app

class BucketListVo(db.Model):
    __tablename__ = 'BucketList'
    BucketId = db.Column('BucketId', db.Integer, primary_key = True)
    UserId = db.Column('UserId',db.Integer,nullable=False)
    ListTitle = db.Column('ListTitle',db.String(50),nullable=False)
    Date = db.Column('Date',db.String(50),nullable=False)
    isCompleted = db.Column('isCompleted',db.Boolean,default=False)
    Purpose= db.Column('Purpose',db.String(50))
    CompletionDate=db.Column('CompletionDate',db.String(50))

with app.app_context():
    db.create_all()
