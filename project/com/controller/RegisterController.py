from project import app
from flask import Flask,url_for, render_template, request, flash, redirect
from project.com.dao.UserDAO import UserDAO
from project.com.dao.RelationsDAO import RelationsDAO

from project.com.dao.GroupDAO import GroupDAO
import pandas as pd
from project.com.vo.UserVo import UserVo
from project.com.dao.UserDAO import UserDAO

import re
from project.com.vo.UserRelationsVo import UserRelationsVo
relationsDAO=RelationsDAO()
@app.route('/RegisterPage')
def loadRegister():
    return render_template('RegisterPage.html')

@app.route('/registerUser',methods=['POST'])
def registerValidation():
    vo=UserVo()
    userDao=UserDAO()
    groupDao=GroupDAO()

    fName=request.form['FirstName']
    emaild=request.form['Emaild']
    lName =request.form['LastName']
    userName =request.form['UserName']
    password =request.form['Password']
    phone=request.form['phone']
    dob =request.form['dob']
    # 0=user
    # 1=admin
    # 0=not approved
    # 1=approved
    vo.FirstName =fName
    vo.Emaild =emaild
    vo.LastName = lName
    vo.UserName =userName
    vo.Password = password
    vo.Phone=phone
    vo.Dob =dob
    # print(vo)
    # password 
    print(len(fName))
    print(len(emaild))
    print(len(lName))
    print(len(password ))
                
    # if len(fName)>32 or len(emaild)>32 or len(lName)>32 or len(userName)>32 or len(password)>32:
    #     flash('The password you have entered is exceeding the limit. Please enter a smaller one.')
    #     return render_template('RegisterPage.html',obj=vo, error=msg)
    if len(fName)>32:
        msg ='First name exceeds lenght limit'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if len(lName)>32:
        msg ='Last name exceeds lenght limit'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if len(fName.strip())<1:
        msg ='First name is not entered'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if len(lName.strip())<1:
        msg ='Last name is not entered'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if len(emaild)>32:
        msg ='Email id exceeds lenght limit'
        return render_template('RegisterPage.html',obj=vo, error=msg)


    vo.Role=0
    if len(password)<8:
        msg ='Password should have atleast 8 charcates'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if bool(re.search(r"\s", password)):
        print(password)
        msg ='Password should not have tab or space in between'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if not bool(re.search(r'\d', password)):
        msg ='Password should have atleast one digit'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if not bool(re.search(r'[A-Z]', password)):
        msg ='Password should have atleast one uper case'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if not bool(re.search(r'[a-z]', password)):
        msg ='Password should have atleast one lower case'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    if len(phone)!=10:
        msg ='Phone number should be of 10 digits.'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    
    vo.Status=0
    ans=userDao.getUserByUserName(vo.UserName)
    
    if len(ans)>0:
        msg ='Please enter a different email or username, already in use!!!'
        return render_template('RegisterPage.html',obj=vo, error=msg)
    else:
        userDao.addUser(vo)
        groupDao.addDefaultGroups(vo)
    return redirect('/')

@app.route('/LoadData')
def LoadData():
    df=pd.read_csv('D:/Sem 4/ASE/Rachna repo/ASE/project/com/User_relations.csv')
    df2=pd.read_csv('D:/Sem 4/ASE/Rachna repo/ASE/project/com/user.csv')
    userDAO=UserDAO()
    for i in range(len(df2)):
        # print(df.iloc[i]['Relation'])
        vo=UserVo()
        vo.FirstName =df2.iloc[i]['FirstName']
        vo.Emaild =df2.iloc[i]['Emaild']
        vo.LastName =df2.iloc[i]['LastName']
        vo.UserName =df2.iloc[i]['UserName']
        vo.Password =df2.iloc[i]['Password']
        vo.Phone=int(df2.iloc[i]['Phone'])
        vo.Dob =df2.iloc[i]['Dob']
        vo.Status=int(df2.iloc[i]['Status'])
        vo.Role=int(df2.iloc[i]['Role'])
        userDAO.addUser(vo)
    for i in range(len(df)):
        print(df.iloc[i]['Relation'])
        userRelationsVo1=UserRelationsVo()
        userRelationsVo1.UserId=int(df.iloc[i]['UserId'])
        userRelationsVo1.User2Id=int(df.iloc[i]['User2Id'])
        userRelationsVo1.Relation=df.iloc[i]['Relation']
        relationsDAO.addRelation(userRelationsVo1)
        # 
        # print(i)
    return redirect('/')

    # loadData()
# 