from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect, session
from project.com.dao.TravelDAO import TravelDAO

travelDAO=TravelDAO()
    
@app.route('/Travels',methods=['POST','GET'])
def getTravelPosts():   
    userId=0
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    data=travelDAO.fetchAllTravels(userId)
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

    return render_template('Travel.html',ln=len(data),data=data,UserId=userId)