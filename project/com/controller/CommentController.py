from project import app
from project import db
from project.com.controller import EventController
from project.com.dao.UserDAO import UserDAO
from project.com.vo.CommentVo import CommentVo
from project.com.dao.CommentDAO import CommentDAO
from project.com.dao.PostDAO import PostDAO
from flask import redirect, request
from flask import render_template
from datetime import datetime as dt

PostDao=PostDAO()
CommentDao=CommentDAO()
userDao=UserDAO()

@app.route('/addComment', methods=['POST'])
def addComment():
    vo=CommentVo()
    commentDescription=request.form['comment']
    PostId=request.form['PostId']
    UserId=request.form['UserId']
    id=request.form['id']
    routetype=request.form['routetype']
    time=dt.now()
    vo.CommentTime=time
    vo.commentDescription=commentDescription
    vo.PostId=PostId
    vo.CommentorId=UserId
    user=userDao.getByUserId(UserId)
    vo.UserName=user.UserName
    CommentDao.addComment(vo)
    if routetype == "FriendRoute":
         firendPosts=PostDao.getPostByUserId(id)
         return render_template('IndividualFriend.html',person=UserId,friendName=firendPosts[0]['post'].UserName,firendPosts=firendPosts,friendid=id)
    elif routetype == "FamilyRoute":
         familyPosts=PostDao.getPostByUserId(id)
         return render_template('IndividualFamily.html',person=UserId,familyName=familyPosts[0]['post'].UserName,familyPosts=familyPosts,familyId=id)
    elif routetype == "EventRoute":
         return redirect('/events')
    elif routetype == "TravelRoute":
         return redirect('/Travels')

    return 'comented'
