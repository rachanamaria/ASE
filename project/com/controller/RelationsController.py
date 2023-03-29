from project import app
from flask import Flask,url_for, render_template, request, flash, redirect
from project.com.dao.UserDAO import UserDAO
from project.com.dao.RelationsDAO import RelationsDAO

from project.com.vo.UserVo import UserVo
from project.com.vo.UserRelationsVo import UserRelationsVo


import re

relationsDAO=RelationsDAO()

@app.route('/addRelations',methods=['POST'])
def addRelations():
    userRelationsVo1=UserRelationsVo()
    userRelationsVo1.UserId=request.form['UserId']
    userRelationsVo1.User2Id=request.form['UserId2']
    userRelationsVo1.Relation=request.form['Relation']
    userRelationsVo2=UserRelationsVo()
    userRelationsVo2.User2Id=request.form['UserId']
    userRelationsVo2.UserId=request.form['UserId2']
    userRelationsVo2.Relation=request.form['Relation']
    relationsDAO.addRelation(userRelationsVo1)
    relationsDAO.addRelation(userRelationsVo2)
    return redirect('/')
