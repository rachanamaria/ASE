from project import app
from flask import Flask,url_for, render_template, request, flash, redirect
from project.com.dao.UserDAO import UserDAO
from project.com.dao.RelationsDAO import RelationsDAO

from project.com.vo.UserVo import UserVo
from project.com.dao.UserDAO import UserDAO

from project.com.vo.UserRelationsVo import UserRelationsVo


import re

relationsDAO=RelationsDAO()
userDAO=UserDAO()
@app.route('/addRelations',methods=['POST'])
def addRelations():
    userRelationsVo1=UserRelationsVo()
    userRelationsVo1.UserId=request.form['UserId']
    userRelationsVo1.User2Id=request.form['UserId2']
    userRelationsVo1.Relation=request.form['Relation']
    userRelationsVo2=UserRelationsVo()
    userRelationsVo2.User2Id=request.form['UserId']
    userRelationsVo2.UserId=request.form['UserId2']
    userRelationsVo2.Relation=request.form['Relation']
    relationsDAO.addRelation(userRelationsVo1)
    relationsDAO.addRelation(userRelationsVo2)
    users=[]
    UserId=request.form['UserId']
    if userRelationsVo2.Relation=='Friend':
        friends=relationsDAO.getFriends(UserId)
        users=userDAO.getActiveUsers()
        return render_template('AllFriends.html',userId=UserId,lenFriends=len(friends),friends=friends,users=users)
    elif userRelationsVo2.Relation=='Family':
        friends=relationsDAO.getFamily(UserId)
        users=userDAO.getActiveUsers()
        return render_template('AllFamily.html',userId=UserId,lenFriends=len(friends),friends=friends,users=users)

@app.route('/allfriends',methods=['POST'])
def getUsersAndFriends():
    users=[]
    UserId=request.form['UserId']
    
    friends=relationsDAO.getFriends(UserId)
    users=userDAO.getActiveUsers()
    return render_template('AllFriends.html',userId=UserId,lenFriends=len(friends),friends=friends,users=users)


@app.route('/searchfriend',methods=['POST'])
def searchfriend():
    users=[]
    UserId=request.form['userId']
    print("userid",UserId)
    searchFriendName = request.form['searchFriendName']
    
    friends=relationsDAO.getFriends(UserId)
    users=userDAO.getActiveUsers()
    
    singleSearch= ""
    for i in users:
        print(i.UserName)
        if i.UserName == searchFriendName:
            singleSearch = i
        

        
    return render_template('AllFriends.html',userId=UserId,lenFriends=len(friends),friends=friends,users=users,searchuser=singleSearch)
