from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect
from project.com.dao.EventDAO import EventDAO

eventDAO=EventDAO()
    
@app.route('/EventPosts', methods=['POST'])
def getEventPosts():   
    UserId=request.form['UserId']
    data=eventDAO.fetchAllEvents(UserId)
    print('data..',data)   
    for i in data:
        print('-----data------------------')
        print(i.eventName)
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
