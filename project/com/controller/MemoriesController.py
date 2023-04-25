from flask import render_template, request
from project import app
from flask import render_template,request
from project.com.dao.PostDAO import PostDAO
from project.com.dao.RelationsDAO import RelationsDAO
from project.com.controller.ForgetPasswordController import notification
from project.com.dao.UserDAO import UserDAO

relationsDAO=RelationsDAO()
postDAO=PostDAO()
dao=UserDAO()

@app.route('/MemoriesPost', methods=['POST','GET'])
def MemoriesPost():
    UserId=request.form['UserId']
    memories=[]
    dic=relationsDAO.getAllRelations(UserId)    
    for userId,relation in dic.items():
        memories.extend(postDAO.getMemoriesPost(userId))
    User=dao.getByUserId(UserId)
    email=User.Emaild
    notification(email,len(memories))
    return render_template('Memories.html',memories=memories)
