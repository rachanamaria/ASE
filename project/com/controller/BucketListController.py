from flask import flash
from flask import render_template, request
from project import db,app
from flask import render_template,request,redirect, session
from project.com.dao.BucketListDAO import BucketListDAO
from project.com.vo.BucketListVo import  BucketListVo
from datetime import datetime

bucketlistvo=BucketListVo()
bucketlistdao=BucketListDAO()


class BucketList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    bucket_list = bucketlistvo.query.all()
    return render_template('index.html', bucket_list=bucket_list)

@app.route('/addlist', methods=['POST'])
def addlist():
    item = request.form['item']
    new_item = BucketListVo(item=item)
    bucketlistdao.add(new_item)
    return redirect('/BucketList')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    item = request.form['item']
    bucket_list_item = BucketListVo.query.get_or_404(id)
    bucket_list_item.item = item
    db.session.commit()
    return redirect('/BucketList')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    bucket_list_item = BucketListVo.query.get_or_404(id)
    
    return redirect('/BucketList')

@app.route('/completed/<int:id>')
def completed(id):
    bucket_list_item = BucketListVo.query.get_or_404(id)
    bucket_list_item.completed = True
    db.session.commit()
    return redirect('BucketList')