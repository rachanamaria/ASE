from project import app
from project import db
from project.com.dao.UserDAO import UserDAO
from project.com.vo.CommentVo import CommentVo
from project.com.dao.CommentDAO import CommentDAO
from project.com.dao.PostDAO import PostDAO
from flask import request
from flask import render_template
from datetime import datetime as dt



vo=CommentVo()
PostDao=PostDAO()
CommentDao=CommentDAO()
userDao=UserDAO()
@app.route('/addComment', methods=['POST'])
def addComment():
    commentDescription=request.form['comment']
    PostId=request.form['PostId']
    UserId=request.form['UserId']
    FriendId=request.form['Friendid']
    firendPosts,comments=PostDao.getPostByUserId(FriendId)
    routetype=request.form['routetype']
    print(PostId,UserId,FriendId,firendPosts,comments)
    time=dt.now()
    vo.CommentTime=time
    vo.commentDescription=commentDescription
    vo.PostId=PostId
    vo.CommentorId=UserId
    user=userDao.getByUserId(UserId)
    vo.UserName=user.UserName
    CommentDao.addComment(vo)

    if routetype == "FriendRoute":
         return render_template('IndividualFriend.html',person=UserId,friendName=firendPosts[0].UserName,firendPosts=firendPosts,comments=comments,friendid=FriendId)
    return 'comented'
