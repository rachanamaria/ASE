from project import app
from project.com.vo.PostVo import PostVo
from project.com.dao.PostDAO import PostDAO
from project.com.dao.UserGroupDAO import UserGroupDAO
from project.com.dao.UserDAO import UserDAO
from project.com.dao.GroupDAO import GroupDAO
from flask import Flask,url_for, render_template, request, flash, redirect
from project.com.controller.LoginController import afterApproval,loadDashBoard
from flask import render_template, request
from datetime import datetime as dt
from project.com.vo.EventVo import EventVo
from project.com.dao.EventDAO import EventDAO
import re


PostDao=PostDAO()
UserGroupDao=UserGroupDAO()
UserDao=UserDAO()
GroupDao=GroupDAO()
eventVo=EventVo()
eventDAO=EventDAO()

@app.route('/LoadAddPost', methods=['POST'])
def LoadAddPost():
    UserId=request.form['UserId']
    approvedGroups=UserGroupDao.getApprovedGroupsByUserId(UserId)
    print(UserId)
    print(approvedGroups)
    if len(approvedGroups)==0:
        approvedGroups=[]
    return render_template('LoadAddPost.html',ln=len(approvedGroups),approvedGroups=approvedGroups,UserId=UserId)

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
    print(user)
    user=user[0]

    PostDescription=request.form['PostDescription']
    uploaded_img = request.files['file']
    nm=uploaded_img.filename.split('.')
    time=dt.now()
    vo=PostVo()
    vo.createdTime=time
    vo.CreatorId=UserId
    vo.MediaType=nm[-1]
    vo.type=request.form['Type']
    vo.PostDescription=PostDescription
    vo.UserName=user.UserName
    post=PostDao.addPost(vo,time)
    img=open('D:/Sem 4/ASE/Rachna repo/ASE/project/static/Posts/'+str(post.PostId)+'.'+nm[-1],'wb')
    img.write(uploaded_img.read())
    img.close()
    vo.PostURL='D:/Sem 4/ASE/Rachna repo/ASE/project/static/Posts/'+str(post.PostId)+'.'+nm[-1]
    post=PostDao.addPost(vo,time)

    if vo.type=='Travel':
        objVo=EventVo()
    elif vo.type=='BucketList':
        objVo=EventVo()
    elif vo.type=='Event':
        objVo=EventVo()
        objVo.EventName=request.form['EventName']
    objVo.PostId=post.PostId
    objVo.Visibility= request.form['Visibility']
    objVo.UserId =UserId
    eventDAO.add(objVo)
    return loadDashBoard()

@app.route('/UserPosts', methods=['POST'])
def userPosts():
    friendId=request.form['UserId']
    firendPosts=PostDao.getPostByUserId(friendId)
    return redirect ('/')


