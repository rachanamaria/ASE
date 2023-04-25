from project import app
from project.com.dao.BucketListDAO import BucketListDAO
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
from project.com.vo.BucketListVo import BucketListVo
from project.com.vo.UserVo import UserVo

PostDao=PostDAO()
UserGroupDao=UserGroupDAO()
UserDao=UserDAO()
GroupDao=GroupDAO()
eventVo=EventVo()
eventDAO=EventDAO()
travelVo=TravelVo()
travelDAO=TravelDAO()
bucketlistdao=BucketListDAO()
vo=UserVo()

@app.route('/profilepost', methods=['POST'])
def profilepost():
    userId = session['userId']
    user=UserDao.getByUserId(userId)
    print("firstname",user.FirstName)
    print("last name",user.LastName)
    firendPosts=PostDao.getPostByUserId(userId)
    return render_template('Profile.html',profileusername=user.UserName,firendPosts=firendPosts,person= user.UserId)


@app.route('/profileupdate', methods=['POST'])
def profileupdate():
    userId = session['userId']
    user=UserDao.getByUserId(userId)
    print("firstname",user.Dob)
    print("last name",user.Phone)
    firendPosts=PostDao.getPostByUserId(userId)
    return render_template('Profile.html',profileusername=user.UserName,FirstName = user.FirstName,LastName=user.LastName, Emaild=user.Emaild,UserName=user.UserName,Dob=user.Dob,Phone=user.Phone,person= user.UserId)


@app.route('/updateprofile', methods=['POST'])
def updateprofile(): 
    userId = session['userId']
    user=UserDao.getByUserId(userId)
    sessionusername= session['username']
    fName=request.form['FirstName']
    # emaild=request.form['Emaild']
    lName =request.form['LastName']
    userName =request.form['UserName']
    phone=request.form['phone']
    dob =request.form['dob']
    print("values",phone,dob,lName)
    # 0=user
    # 1=admin
    # 0=not approved
    # 1=approved
    user.FirstName =fName
    # vo.Emaild =emaild
    user.LastName = lName
    user.UserName =userName
    # vo.UserId = userId
    user.Phone=phone
    user.Dob =dob
    # print(vo)
    # password 
    # print(len(fName))
    # print(len(emaild))
    # print(len(lName))
  
                
    # if len(fName)>32 or len(emaild)>32 or len(lName)>32 or len(userName)>32 or len(password)>32:
    #     flash('The password you have entered is exceeding the limit. Please enter a smaller one.')
    #     return render_template('RegisterPage.html',obj=vo, error=msg)
    if len(fName)>32:
        msg ='First name exceeds lenght limit'
        return render_template('RegisterPage.html',obj=user, error=msg)
    if len(lName)>32:
        msg ='Last name exceeds lenght limit'
        return render_template('RegisterPage.html',obj=user, error=msg)
    if len(fName.strip())<1:
        msg ='First name is not entered'
        return render_template('RegisterPage.html',obj=user, error=msg)
    if len(lName.strip())<1:
        msg ='Last name is not entered'
        return render_template('RegisterPage.html',obj=user, error=msg)
    # if len(emaild)>32:
    #     msg ='Email id exceeds lenght limit'
    #     return render_template('RegisterPage.html',obj=vo, error=msg)


    vo.Role=0
    # if len(password)<8:
    #     msg ='Password should have atleast 8 charcates'
    #     return render_template('RegisterPage.html',obj=vo, error=msg)
    # if bool(re.search(r"\s", password)):
    #     print(password)
    #     msg ='Password should not have tab or space in between'
    #     return render_template('RegisterPage.html',obj=vo, error=msg)
    # if not bool(re.search(r'\d', password)):
    #     msg ='Password should have atleast one digit'
    #     return render_template('RegisterPage.html',obj=vo, error=msg)
    # if not bool(re.search(r'[A-Z]', password)):
    #     msg ='Password should have atleast one uper case'
    #     return render_template('RegisterPage.html',obj=vo, error=msg)
    # if not bool(re.search(r'[a-z]', password)):
    #     msg ='Password should have atleast one lower case'
    #     return render_template('RegisterPage.html',obj=vo, error=msg)
    if len(phone)!=10:
        msg ='Phone number should be of 10 digits.'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    
    user.Status=0
    ans=[]
    if(sessionusername!=userName):
        ans=UserDao.getUserByUserName(user.UserName)
    if len(ans)>0:
        msg ='Please enter a different email or username, already in use!!!'
        user=UserDao.getByUserId(userId)
        return render_template('Profile.html',profileusername=user.UserName,FirstName = user.FirstName,LastName=user.LastName, Emaild=user.Emaild,UserName=user.UserName,Dob=user.Dob,Phone=user.Phone,person= user.UserId,error=msg)
    else:
        print("test")
        UserDao.addUser(user)
    
    firendPosts=PostDao.getPostByUserId(userId)
    user=UserDao.getByUserId(userId)
    return render_template('Profile.html',profileusername=user.UserName,FirstName = user.FirstName,LastName=user.LastName, Emaild=user.Emaild,UserName=user.UserName,Dob=user.Dob,Phone=user.Phone,person= user.UserId)