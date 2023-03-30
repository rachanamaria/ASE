from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect
from project.com.dao.EventDAO import EventDAO
from project.com.dao.RelationsDAO import RelationsDAO
from project.com.dao.UserDAO import UserDAO


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