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
    userRelationsVo=UserRelationsVo()
    userRelationsVo.UserId=request.form['UserId']
    userRelationsVo.User2Id=request.form['UserId2']
    userRelationsVo.Relation=request.form['Relation']
    relationsDAO.addRelation(userRelationsVo)
    return redirect('/')
