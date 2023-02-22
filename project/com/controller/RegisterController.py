from project import app
from flask import Flask,url_for, render_template, request, flash
from project.com.dao.UserDAO import UserDAO
from project.com.vo.UserVo import UserVo
import re

@app.route('/RegisterPage')
def loadRegister():
    return render_template('RegisterPage.html')

@app.route('/registerUser',methods=['POST'])
def registerValidation():
    vo=UserVo()
    dao=UserDAO()
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
                
    if len(fName)>32 or len(emaild)>32 or len(lName)>32 or len(userName)>32 or len(password)>32:
        flash('The password you have entered is exceeding the limit. Please enter a smaller one.')
        return render_template('ReloadSignInPage.html',obj=vo)
    vo.Role=0
    if len(password)<8:
        flash('Password should have atleast 8 charcates')
        return render_template('ReloadSignInPage.html',obj=vo)
    if bool(re.search(r"\s", password)):
        print(password)
        flash('Password should not have tab or space in between')
        return render_template('ReloadSignInPage.html',obj=vo)
    if not bool(re.search(r'\d', password)):
        flash('Password should have atleast one digit')
        return render_template('ReloadSignInPage.html',obj=vo)
    if not bool(re.search(r'[A-Z]', password)):
        flash('Password should have atleast one uper case')
        return render_template('ReloadSignInPage.html',obj=vo)
    if not bool(re.search(r'[a-z]', password)):
        flash('Password should have atleast one lower case')
        return render_template('ReloadSignInPage.html',obj=vo)
    
    vo.Status=0
    ans=dao.getUserByUserName(vo.UserName)
    
    if len(ans)>0:
        flash('Please enter a different email or username, already in use!!!')
        return render_template('ReloadSignInPage.html',obj=vo)
    else:   
        dao.addUser(vo)
    return render_template('LoginPage.html')
    