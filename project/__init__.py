from flask import Flask,render_template, session
from flask_sqlalchemy import SQLAlchemy
import os


UPLOAD_FOLDER = os.path.join('../project/static')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'sessionData'
app.config['TESTING'] = True
app.config['PORT']=8000
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = False
servername = '51.81.160.154'
port=3306
dbname = 'rxr8071_FFTD'
username = 'rxr8071_admin'
password = 'c#vFH9LQnQ'
url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(username, password, servername, port, dbname)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
db = SQLAlchemy(app)


@app.route('/')
def index():
    isUserLoggedIn = False
    isAdmin = False
    if 'isLoggedIn' not in session:
        session['isLoggedIn'] = False
    else:
        if 'role' in session and session['role'] == 1:
            isAdmin = True
        elif 'role' in session and session['role'] == 0:
            isAdmin = False
        else:
            isAdmin = False
        isUserLoggedIn = session['isLoggedIn']
    return render_template('LoginPage.html', isUser=isUserLoggedIn, isAdmin = isAdmin)

@app.route('/familyancestry')
def familyancestry():
    return render_template('FamilyAncestry.html')

@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/travel')
def travel():
    return render_template('Travel.html')

@app.route('/events')
def events():
    return render_template('Events.html')

@app.route('/friendhistory')
def friendhistory():
    return render_template('FriendHistory.html')

@app.route('/bucketlist')
def Bucketlist():
    return render_template('BucketList.html')

@app.route('/loadContact')
def contact():
    if 'role' in session and session['role'] == 1:
        isAdmin = True
    elif 'role' in session and session['role'] == 0:
        isAdmin = False
    else:
        isAdmin = False
    isUserLoggedIn = session['isLoggedIn']
    return render_template('Contact.html', isUser=isUserLoggedIn, isAdmin = isAdmin)

@app.route('/loadAbout')
def about():
    if 'role' in session and session['role'] == 1:
        isAdmin = True
    elif 'role' in session and session['role'] == 0:
        isAdmin = False
    else:
        isAdmin = False
    isUserLoggedIn = session['isLoggedIn']
    return render_template('About.html', isUser=isUserLoggedIn, isAdmin = isAdmin)

@app.route('/logout')
def logOut():
    session.pop('username')
    session['isLoggedIn'] = False
    session.pop('role')
    return index()

import project.com  
