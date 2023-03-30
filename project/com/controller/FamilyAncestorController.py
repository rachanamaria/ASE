from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect
from project.com.dao.EventDAO import EventDAO

@app.route('/FamilyAncestoryTree', methods=['POSt'])
def familyAncestory():   
    UserId=request.form['UserId']
    return render_template('tree.html',UserId=UserId)


@app.route('/FamilyAncestory', methods=['POSt'])
def familyHistory():   
    UserId=request.form['UserId']
    return render_template('FamilyHistoryLoad.html',UserId=UserId)


@app.route('/AllFamily', methods=['POST'])
def allFamily():   
    UserId=request.form['UserId']
    return render_template('AllFamily.html',UserId=UserId)
    