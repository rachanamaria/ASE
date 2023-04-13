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
    bucket_list = BucketListVo.query.all()
    return render_template('BucketList.html',bucket_list=bucket_list) 
    

@app.route('/loadBucketList', methods=['POST','GET'])
def addlist():
    UserId = request.form['UserId']
    return redirect('/BucketList',UserId=UserId)

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

        bucket_list = BucketListVo.query.all()
        return render_template('BucketList.html',bucket_list=bucket_list)  



@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    bucket_list_item = BucketListVo.query.get_or_404(id)
    bucketlistdao.delete(bucket_list_item)
    bucket_list = BucketListVo.query.all()
    return render_template('BucketList.html',bucket_list=bucket_list)  

@app.route('/completed/<int:id>',methods=['POST'])
def completed(id):
    print("Completed")
    bucket_list_item = BucketListVo.query.get_or_404(id)
    bucket_list_item.isCompleted = True
    today = date.today()
    # bucket_list.CompletionDate=today
    bucketlistdao.UpdateComplte(bucket_list_item)
    bucket_list = BucketListVo.query.all()
    
    return render_template('BucketList.html',bucket_list=bucket_list)   