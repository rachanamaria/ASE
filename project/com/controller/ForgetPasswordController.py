import smtplib
import random
import string
from flask import flash
from flask import render_template, request
from project import db,app
from email.mime.text import MIMEText
from project.com.vo.UserVo import UserVo
from project.com.dao.UserDAO import UserDAO


vo=UserVo()
dao=UserDAO()

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(sender,password)
    smtpserver.sendmail(sender, recipients, msg.as_string())
    smtpserver.quit()
    
@app.route('/loadForgetPassword')
def loadForgetPassword():
    return render_template('ForgetPassword.html')


@app.route('/forgetpassword',methods=['POST'])
def foregotPassword():
    email=request.form['Emaild']
    vo.Emaild=email
    user=dao.getUserByEmailId(email)

    if len(user)>0:
        user=user[0]
        subject = "Password Reset"
        letters = string.ascii_lowercase
        newPassword = ''.join(random.choice(letters) for i in range(10))
        body = f'Your new password is: {newPassword}\nplease try login with this'
        sender = "testingase01@gmail.com"
        recipients = [email]
        password = "ckzmtgslgcqyifjm"
        send_email(subject, body, sender, recipients, password)
        user.Password=newPassword
        dao.addUser(user)
    else:
        flash('\nEmailId incorrect')
    return render_template('ForgetPassword.html')
    