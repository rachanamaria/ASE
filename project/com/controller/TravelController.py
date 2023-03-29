from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect
from project.com.dao.TravelDAO import TravelDAO

travelDAO=TravelDAO()
    
@app.route('/EventPosts', methods=['POST'])
def getEventPosts():   
    UserId=request.form['UserId']
    data=travelDAO.fetchAllTravels(UserId)
    print('data..',data)
    for i in data:
        print(i.UserName)
    return redirect('/')