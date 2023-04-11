from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect, session
from project.com.dao.EventDAO import EventDAO
from datetime import datetime

eventDAO=EventDAO()
    
@app.route('/events',methods=['POST'])
def getEventPosts():   
    userId=0
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    data=eventDAO.fetchAllEvents(userId)
    justhappend=request.form['justhappend']
    # print('data..',data)   
    # for i in data:
    #     print('-----data------------------')
    #     print(i.eventName)
    #     print(i.post.PostId)
    #     print(i.post.CreatorId)
    #     print(i.post.MediaType)
    #     print(i.post.type)
    #     print(i.post.createdTime)
    #     print(i.post.UserName)
    #     print(i.post.PostDescription)
    #     print(i.comments)
    #     print(i.post.PostURL)

    data2=[]
    print(type(data))
    for i in data:
        currentDate = datetime.now()
        print("test")
        diff = currentDate-i.post.createdTime
        print(diff.days)

        if(diff.days <2 ):
            data2.append(i)
        
    print(data2)

    if(justhappend=='justhappend'):
        return render_template('Events.html',ln=len(data2),data=data2,UserId=userId,page ='justhappend')
    
    return render_template('Events.html',ln=len(data),data=data,UserId=userId,page ='events')


# @app.route('/recentpost')
# def getRecentPosts():   
#     userId=0
#     if 'isLoggedIn'in session and session['isLoggedIn']:
#         userId = session['userId']
#     data=eventDAO.fetchAllEvents(userId)
#     data2=[]
#     print(type(data))
#     for i in data:
#         currentDate = datetime.now()
#         print("test")
#         diff = currentDate-i.post.createdTime
#         print(diff.days)

#         if(diff.days <2 ):
#             data2.append(i)
        
#     print(data2)
#     return render_template('RecentPost.html',ln=len(data2),data=data2,UserId=userId)



    