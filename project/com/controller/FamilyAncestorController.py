from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect
from project.com.dao.EventDAO import EventDAO
from project.com.dao.RelationsDAO import RelationsDAO
from project.com.dao.UserDAO import UserDAO
from project.com.dao.PostDAO import PostDAO


postDAO=PostDAO()
relationsDAO=RelationsDAO()
userDAO=UserDAO()
@app.route('/FamilyAncestoryTree', methods=['POSt'])
def familyAncestory():   
    UserId=request.form['UserId']
    return render_template('tree.html',UserId=UserId)


@app.route('/FamilyAncestory', methods=['POSt'])
def familyHistory():   
    UserId=request.form['UserId']
    return render_template('FamilyHistoryLoad.html',UserId=UserId)


# @app.route('/AllFamily', methods=['POST'])
# def allFamily():   
#     UserId=request.form['UserId']
#     return render_template('AllFamily.html',UserId=UserId)
    
@app.route('/AllFamily',methods=['POST'])
def getUsersAndFamily():
    users=[]
    UserId=request.form['UserId']
    friends=relationsDAO.getFamily(UserId)
    users=userDAO.getActiveUsers()
    return render_template('AllFamily.html',userId=UserId,lenFriends=len(friends),friends=friends,users=users)



@app.route('/searchFamily',methods=['POST'])
def searchFamily():
    users=[]
    UserId=request.form['userId']
    print("userid",UserId)
    searchFriendName = request.form['searchFriendName']
    
    friends=relationsDAO.getFamily(UserId)
    users=userDAO.getActiveUsers()
    
    singleSearch= ""
    for i in users:
        print(i.UserName)
        if i.UserName == searchFriendName:
            singleSearch = i        
    return render_template('AllFamily.html',userId=UserId,lenFriends=len(friends),friends=friends,users=users,searchuser=singleSearch)


@app.route('/UserFamilyPosts', methods=['POST'])
def userFamilyPosts():
    person=request.form['UserId']
    familyId=request.form['User2Id']
    familyPosts=postDAO.getPostByUserId(familyId)
    if len(familyPosts)==0:
        fnName=''
    else:
        fnName=familyPosts[0]['post'].UserName
    return render_template('IndividualFamily.html',person=person,familyName=fnName,familyPosts=familyPosts,familyId=familyId)