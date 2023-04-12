from project import app
from project.com.dao.TravelDAO import TravelDAO
from project.com.vo.PostVo import PostVo
from project.com.dao.PostDAO import PostDAO
from project.com.dao.UserGroupDAO import UserGroupDAO
from project.com.dao.UserDAO import UserDAO
from project.com.dao.GroupDAO import GroupDAO
from flask import Flask,url_for, render_template, request, flash, redirect, session
from project.com.controller.LoginController import afterApproval,loadDashBoard
from flask import render_template, request
from datetime import datetime as dt
from project.com.vo.EventVo import EventVo
from project.com.dao.EventDAO import EventDAO
import re
from project.com.vo.TravelVo import TravelVo


PostDao=PostDAO()
UserGroupDao=UserGroupDAO()
UserDao=UserDAO()
GroupDao=GroupDAO()
eventVo=EventVo()
eventDAO=EventDAO()
travelVo=TravelVo()
travelDAO=TravelDAO()

@app.route('/addPostEvent')
def addPostEvent():
    userId=0
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    return render_template('AddPostEvent.html', UserId=userId)

@app.route('/addPostTravel')
def addPostTravel():
    userId=0
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    return render_template('AddPostTravel.html', UserId=userId)

@app.route('/CreatePost', methods=['POST'])
def CreatePost():
    UserId=request.form['UserId']
    GroupId=request.form['GroupId']
    return render_template('AddPost.html',UserId=UserId,GroupId=GroupId)

@app.route('/DeletePost', methods=['POST'])
def deletePost():
    PostId=request.form['PostId']
    PostDao.deletePost(PostId)
    return loadDashBoard()


@app.route('/AddPost', methods=['POST'])
def addPost():
    UserId=request.form['UserId']
    user=UserDao.getByUserId(UserId)
    user=user
    PostDescription=request.form['PostDescription']
    uploaded_img = request.files['file']
    nm=uploaded_img.filename.split('.')
    time=dt.now()
    time = time.replace(microsecond=0)
    vo=PostVo()
    vo.createdTime=time
    vo.CreatorId=UserId
    vo.MediaType=nm[-1]
    vo.type=request.form['Type']
    vo.PostDescription=PostDescription
    vo.UserName=user.UserName
    post=PostDao.addPost(vo,time)
    img=open('project/static/Posts/'+str(post.PostId)+'.'+nm[-1],'wb')
    img.write(uploaded_img.read())
    img.close()
    vo.PostURL='../static/Posts/'+str(post.PostId)+'.'+nm[-1]
    post=PostDao.addPost(vo,time)

    if vo.type=='Travel':
        objVo=TravelVo()
        objVo.TravelName=request.form['EventName']
        objVo.PostId=post.PostId
        objVo.Visibility= request.form['Visibility']
        objVo.UserId =UserId
        travelDAO.add(objVo)
    elif vo.type=='BucketList':
        objVo=EventVo()
    elif vo.type=='Event':
        objVo=EventVo()
        objVo.EventName=request.form['EventName']
        objVo.PostId=post.PostId
        objVo.Visibility= request.form['Visibility']
        objVo.UserId =UserId
        eventDAO.add(objVo)
    return render_template('Home.html', obj=user)

@app.route('/UserFriendsPosts', methods=['POST'])
def userPosts():
    person=request.form['UserId']
    friendId=request.form['User2Id']
    firendPosts=PostDao.getPostByUserId(friendId)
    if len(firendPosts)==0:
        fnName=''
    else:
        print(firendPosts)
        print(firendPosts[0])
        fnName=firendPosts[0]['post'].UserName
    return render_template('IndividualFriend.html',person=person,friendName=fnName,firendPosts=firendPosts,friendid=friendId)


@app.route('/AddPostMain', methods=['POST', 'GET'])
def addPostMains():
    userId=0
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    user=UserDao.getByUserId(userId)
    user=user
    return render_template("AddPostMain.html",userId=userId)

# @app.route('/AddPostEvent', methods=['POST'])
# def addPostEvents():
#     UserId=request.form['UserId']
#     user=UserDao.getByUserId(UserId)
#     user=user
#     return render_template("AddPostEvent.html",userId=UserId)