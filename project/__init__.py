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
# ---------------------mysql url---------------------------------------------
url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(username, password, servername, port, dbname)
# ---------------------------In memory url-----------------------------------------
# url='sqlite:///database.db'
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
    print(isUserLoggedIn)
    return render_template('LoginPage.html', isUser=isUserLoggedIn, isAdmin = isAdmin)

@app.route('/familyancestry')
def familyancestry():
    return render_template('FamilyAncestry.html')

@app.route('/addPostMain')
def addPostMain():
    return render_template('AddPostMain.html')

@app.route('/addPostEvent')
def addPostEvent():
    userId=0
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    return render_template('AddPostEvent.html', UserId=userId)

# @app.route('')
# def allfriends():
#     return render_template('AllFriends.html')

@app.route('/friendsaddpost')
def friendsaddpost():
    return render_template('FriendsAddPost.html')

@app.route('/home')
def home():
    user = {'UserId':0,'Role': ''}
    if 'isLoggedIn'in session and session['isLoggedIn']:
        user['UserId'] = session['userId']
        return render_template('Home.html', obj=user)
    return index()

@app.route('/travel')
def travel():
    return render_template('Travel.html')


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
    session.pop('isLoggedIn')
    session.pop('role')
    session.pop('userId')
    return index()




import project.com  
