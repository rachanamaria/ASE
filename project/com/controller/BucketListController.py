from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect, session
from project.com.dao.BucketListDAO import BucketListDAO
from project.com.vo.BucketListVo import  BucketListVo
from datetime import date

bucketlistvo=BucketListVo()
bucketlistdao=BucketListDAO()

@app.route('/bucketlist', methods=['POST','GET'])
def Bucketlist():
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    bucket_list = BucketListVo.query.filter_by(UserId = userId).all()
    completedcount = BucketListVo.query.filter_by(UserId = userId).filter_by(isCompleted=True).count()
    inprogresscount = BucketListVo.query.filter_by(UserId = userId).filter_by(isCompleted=False).count()
    
    return render_template('BucketList.html',bucket_list=bucket_list,UserId=userId,Completedcount=completedcount,Inprogresscount=inprogresscount)
    



@app.route('/addBucketList')
def addBucketList():
    userId=0
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    return render_template('AddBucketList.html', UserId=userId)

@app.route('/AddList', methods=['POST'])
def addList():
        UserId=request.form['UserId']
        objVo=BucketListVo()
        objVo.ListTitle=request.form['BucketList']
        objVo.Date=request.form['posteddate'] 
        objVo.BucketId= 0 ####
        objVo.UserId =UserId
        objVo.isCompleted=False
        objVo.Purpose=request.form['Visibility']
        bucketlistdao.add(objVo)
        print(UserId)
        bucket_list = BucketListVo.query.filter_by(UserId = UserId).all()
        completedcount = BucketListVo.query.filter_by(UserId = userId).filter_by(isCompleted=True).count()
        inprogresscount = BucketListVo.query.filter_by(UserId = userId).filter_by(isCompleted=False).count()
    
        return render_template('BucketList.html',bucket_list=bucket_list,UserId=userId,Completedcount=completedcount,Inprogresscount=inprogresscount)
    


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):

    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    bucket_list_item = BucketListVo.query.get_or_404(id)
    bucketlistdao.delete(bucket_list_item)
    bucket_list = BucketListVo.query.filter_by(UserId = userId).all()
    completedcount = BucketListVo.query.filter_by(UserId = userId).filter_by(isCompleted=True).count()
    inprogresscount = BucketListVo.query.filter_by(UserId = userId).filter_by(isCompleted=False).count()
    
    return render_template('BucketList.html',bucket_list=bucket_list,UserId=userId,Completedcount=completedcount,Inprogresscount=inprogresscount)
    
@app.route('/completed/<int:id>',methods=['POST'])
def completed(id):
    print("Completed")
    if 'isLoggedIn'in session and session['isLoggedIn']:
        userId = session['userId']
    bucket_list_item = BucketListVo.query.get_or_404(id)
    bucket_list_item.isCompleted = True
    today = date.today()
    # bucket_list.CompletionDate=today
    bucketlistdao.UpdateComplte(bucket_list_item)
    bucket_list = BucketListVo.query.all()
    completedcount = BucketListVo.query.filter_by(isCompleted=True).count()
    inprogresscount = BucketListVo.query.filter_by(isCompleted=False).count()
    
    return render_template('BucketList.html',bucket_list=bucket_list,Completedcount=completedcount,Inprogresscount=inprogresscount)
       