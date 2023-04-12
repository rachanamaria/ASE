from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect, session
from project.com.dao.TravelDAO import TravelDAO

travelDAO=TravelDAO()
    
@app.route('/Travels')
def getTravelPosts():   
    UserId=0
    # if 'isLoggedIn'in session and session['isLoggedIn']:
    UserId = request.form['UserId']
    # print(UserId)
    data=travelDAO.fetchAllTravels(UserId)
    print('data..',data)   
    for i in data:
        print('-----data------------------')
        print(i.TravelName)
        print(i.post.PostId)
        print(i.post.CreatorId)
        print(i.post.MediaType)
        print(i.post.type)
        print(i.post.createdTime)
        print(i.post.UserName)
        print(i.post.PostDescription)
        print(i.comments)
        print(i.post.PostURL)

    return render_template('Events.html',ln=len(data),data=data,UserId=UserId)