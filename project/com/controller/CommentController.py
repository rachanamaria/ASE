from project import app
from project import db
from project.com.dao.UserDAO import UserDAO
from project.com.vo.CommentVo import CommentVo
from project.com.dao.CommentDAO import CommentDAO
from flask import request
from datetime import datetime as dt



vo=CommentVo()
CommentDao=CommentDAO()
userDao=UserDAO()
@app.route('/addComment', methods=['POST'])
def addComment():
    commentDescription=request.form['comment']
    PostId=request.form['PostId']
    UserId=request.form['UserId']
    time=dt.now()
    vo.CommentTime=time
    vo.commentDescription=commentDescription
    vo.PostId=PostId
    vo.CommentorId=UserId
    user=userDao.getByUserId(UserId)
    vo.UserName=user.UserName
    CommentDao.addComment(vo)
    return 'comented'
