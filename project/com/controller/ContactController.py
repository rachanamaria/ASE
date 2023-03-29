import smtplib
import random
import string
from flask import flash, session
from flask import render_template, request
from project import db, app
from email.mime.text import MIMEText
from project.com.vo.UserVo import UserVo
from project.com.dao.UserDAO import UserDAO


vo = UserVo()
dao = UserDAO()


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(sender, password)
    smtpserver.sendmail(sender, recipients, msg.as_string())
    smtpserver.quit()


@app.route('/loadContact')
def loadContact():
    isUserLoggedIn = session['isLoggedIn']
    if 'role' in session and session['role'] == 1:
        isAdmin = True
    elif 'role' in session and session['role'] == 0:
        isAdmin = False
    else:
        isAdmin = False
    return render_template('Contact.html', isUser=isUserLoggedIn, isAdmin=isAdmin)


@app.route('/submitContact', methods=['POST'])
def submitContact():
    fName = request.form['FirstName']
    emaild = request.form['Emaild']
    lName = request.form['LastName']
    phone = request.form['phone']
    comment = request.form['comment']
    vo.Emaild = emaild
    # user = dao.getUserByEmailId(emaild)
    password = "ckzmtgslgcqyifjm"
    isUserLoggedIn = session['isLoggedIn']
    # if len(user)>0:
    subject = "FFTD: Help Requested"
    body = f'Hello {fName},\nThank you for reaching out to FFTD support team. We have registered your query with us. Our specialist will reach out to you as early as possible.\nThank you,\nFFTD. '
    sender = "testingase01@gmail.com"
    recipients = [emaild]
    send_email(subject, body, sender, recipients, password)
    # else:
    #     subject = "FFTD: Help Requested"
    #     body = f'Hello {fName},\nThank you for reaching out to FFTD support team. Please register to FFTD before we can offer our support.\nThank you,\nFFTD. '
    #     sender = "testingase01@gmail.com"
    #     recipients = [emaild]
    #     send_email(subject, body, sender, recipients, password)
    flash('\nRequest registered successfully!!!')
    return render_template('Contact.html', isUser=isUserLoggedIn)
