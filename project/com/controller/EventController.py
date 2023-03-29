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
        print(i.eventName)
        print(i.post.UserName)
    return redirect('/')