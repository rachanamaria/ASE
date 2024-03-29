from project import app
from flask import flash, session
from project.com.dao.UserDAO import UserDAO
from project.com.vo.UserVo import UserVo
from project.com.controller.ProjectAdminController import  adminLogin
from flask import Flask,url_for, render_template,session ,request
from project.com.dao.GroupDAO import GroupDAO
from project.com.dao.PostDAO import PostDAO
from project.com.dao.UserGroupDAO import UserGroupDAO
from project import index


PostDao=PostDAO()
GroupDao=GroupDAO()
UserDao=UserDAO()
UserGroupDao=UserGroupDAO()

@app.route('/afterApproval', methods=['POST'])
def afterApproval(user):
    print('...inside after approval.....')
    unApprovedUserList=[]
    unApprovedGroupUserList=[]
    UnApprovedPostList=[]
    unApprovedGroup=[]
    dailyPost=[]
    if user.Status==1:
        groups=GroupDao.getGroupsWhereAdminId(user.UserId)
        if user.Role==1:
            unApprovedUserList=adminLogin()
            UnApprovedPostList=PostDao.getUnapporvedPost()
            unApprovedGroup=GroupDao.UnApporvedGroup()
            unApprovedGroupUserList=UserGroupDao.getUnapporvedUser()
            # dailyPost.append(PostDao.getApporvedPost())
        # check if user is admin of any group
        elif len(groups)>0:
            for i in groups:
                ls=PostDao.getUnapporvedPostByGroupId(i.GroupId)
                ps=PostDao.getApporvedPostByGoupId(i.GroupId)
                if len(ps)>0:
                    dailyPost.append(ps)
                if len(ls)>0:
                    UnApprovedPostList.append(ls)
                users=UserGroupDao.getUnapporvedUserByGroupId(i.GroupId)
                if len(users):
                    unApprovedGroupUserList.append(users)
        return render_template('DashBoard.html',obj=user,ldp=len(dailyPost),lugu=len(unApprovedGroupUserList),lug=len(unApprovedGroup),lup=len(UnApprovedPostList),lus=len(unApprovedUserList),dailyPost=dailyPost,unApprovedUserList=unApprovedUserList,UnApprovedPostList=UnApprovedPostList,unApprovedGroup=unApprovedGroup,unApprovedGroupUserList=unApprovedGroupUserList)
        


@app.route('/login', methods=['POST'])
def loginValidation():
    print('login...................')
    unApprovedUserList=[]
    unApprovedGroupUserList=[]
    UnApprovedPostList=[]
    unApprovedGroup=[]
    dailyPost=[]
    adminPost=[]
    groupPost=[]
    activeGroup=[]
    activeGroupUser=[]
    activeUsers=[]
    vo=UserVo()
    dao=UserDAO()
    UserName=''
    Password=request.form['Password']
    EmailId=request.form['Emaild']

    if (len(UserName)<1 and len(EmailId)<1) or len(Password)<1:
        flash('you invalid entery!!, try again')
        return render_template('LoginPage.html')
    if len(UserName)>32 or len(EmailId)>32 or len(Password)>32:
        flash('you entered very long details, please enter smaller one')
        return render_template('LoginPage.html')
    vo.UserName=UserName
    vo.Password=Password
    vo.Emaild=EmailId
    session['isLoggedIn'] = False
    if len(UserName)>0:
        user=dao.getUserByUserName(UserName)
    elif len(EmailId)>0:
        user=dao.getUserByEmailId(EmailId)
    if len(user)>0:
        print(user)
        user=user[0]
        print(user)
        if vo.Password==user.Password and (vo.UserName==user.UserName or vo.Emaild==user.Emaild):
            if user.Status==1:
                adminGroups=GroupDao.getGroupsWhereAdminId(user.UserId)
                group=UserGroupDao.getApprovedGroupsByUserId(user.UserId)
                if user.Role==1:
                    activeUsers=UserDao.getActiveUsers()
                    print('activeUsers',activeUsers)
                    unApprovedUserList=adminLogin()
                    unApprovedGroup=GroupDao.UnApporvedGroup()
                    activeGroupUser=GroupDao.activeGroups()
                    UnApprovedPostList=PostDao.getUnapporvedPost()
                    unApprovedGroupUserList=UserGroupDao.getUnapporvedUser()
                    adminPost=PostDao.getApporvedPost()
                    print('admin post....',adminPost)
                elif len(adminGroups)>0:
                    for i in adminGroups:
                        ls=PostDao.getUnapporvedPostByGroupId(i.GroupId)
                        if len(ls)>0:
                            UnApprovedPostList.append(ls)
                        users=UserGroupDao.getUnapporvedUserByGroupId(i.GroupId)
                        if len(users):
                            unApprovedGroupUserList.append(users)
                if len(group)>0:
                    for j in group:
                        ps=PostDao.getApporvedPostByGoupId(j.GroupId)
                        if len(ps)>0:
                            groupPost.append(ps)
                print('user role:',user.Role)
                session['username'] = user.UserName
                session['isLoggedIn'] = True
                session['role'] = 0
                session['userId']=user.UserId
                if(user.Role):
                    session['role'] = 1
                    return render_template('DashBoard.html',obj=user,activeGroupUser=activeGroupUser,lenActiveGroupUser=len(activeGroupUser),lenActiveUsers=len(activeUsers),activeUsers=activeUsers,adminPost=adminPost,ldp=len(groupPost),lugu=len(unApprovedGroupUserList),lug=len(unApprovedGroup),lup=len(UnApprovedPostList),lus=len(unApprovedUserList),dailyPost=groupPost,unApprovedUserList=unApprovedUserList,UnApprovedPostList=UnApprovedPostList,unApprovedGroup=unApprovedGroup,unApprovedGroupUserList=unApprovedGroupUserList)
                else:
                     return render_template('Home.html',obj=user,activeGroupUser=activeGroupUser,lenActiveGroupUser=len(activeGroupUser),lenActiveUsers=len(activeUsers),activeUsers=activeUsers,adminPost=adminPost,ldp=len(groupPost),lugu=len(unApprovedGroupUserList),lug=len(unApprovedGroup),lup=len(UnApprovedPostList),lus=len(unApprovedUserList),dailyPost=groupPost,unApprovedUserList=unApprovedUserList,UnApprovedPostList=UnApprovedPostList,unApprovedGroup=unApprovedGroup,unApprovedGroupUserList=unApprovedGroupUserList)
            else:
                flash('admin has yet not approved you!!!')
                return render_template('LoginPage.html')        
        else:
            flash('Password is incorrect')
            return render_template('LoginPage.html')
    else:
        flash('EmailId incorrect')
        return render_template('LoginPage.html') 

       
@app.route('/DeActivateUser', methods=['POST'])
def deActivateUser():
    UserId=request.form['TargetUserId']
    UserDao.deActivateUser(UserId)
    return loadDashBoard()


@app.route('/DashBoard', methods=['POST'])
def loadDashBoard():
    print('in load dashboard.............')
    UserId=request.form['UserId']
    user=UserDao.getByUserId(UserId)
    print(UserId)
    print(user)
    # print(user[0])
    user=user
    # return afterApproval(user)
    unApprovedUserList=[]
    unApprovedGroupUserList=[]
    UnApprovedPostList=[]
    unApprovedGroup=[]
    dailyPost=[]
    adminPost=[]
    groupPost=[]
    activeGroupUser=[]
    activeGroup=[]
    activeUsers=[]
    vo=UserVo()
    dao=UserDAO()
    if user.Status==1:
        session['username'] = user.UserName
        session['isLoggedIn'] = True
        adminGroups=GroupDao.getGroupsWhereAdminId(user.UserId)
        group=UserGroupDao.getApprovedGroupsByUserId(user.UserId)
        if user.Role==1:
            activeUsers=UserDao.getActiveUsers()
            print('activeUsers',activeUsers)
            unApprovedUserList=adminLogin()
            activeGroupUser=GroupDao.activeGroups()
            unApprovedGroup=GroupDao.UnApporvedGroup()
            unApprovedGroupUser=[]
            UnApprovedPostList=PostDao.getUnapporvedPost()
            unApprovedGroupUserList=UserGroupDao.getUnapporvedUser()
            adminPost=PostDao.getApporvedPost()
            # print('admin post....',adminPost)
        # check if user is admin of any group
        elif len(adminGroups)>0:
            for i in adminGroups:
                ls=PostDao.getUnapporvedPostByGroupId(i.GroupId)
                if len(ls)>0:
                    UnApprovedPostList.append(ls)
                users=UserGroupDao.getUnapporvedUserByGroupId(i.GroupId)
                if len(users):
                    unApprovedGroupUserList.append(users)
        if len(group)>0:
            for j in group:
                ps=PostDao.getApporvedPostByGoupId(j.GroupId)
                if len(ps)>0:
                    groupPost.append(ps)
                # ps=PostDao.getApporvedPostByGoupId(i.GroupId)
        print('user role:',user.Role)
        session['role'] = user.Role
        session['userId']=user.UserId
        return render_template('DashBoard.html',obj=user,activeGroupUser=activeGroupUser,lenActiveGroupUser=len(activeGroupUser),lenActiveUsers=len(activeUsers),activeUsers=activeUsers,adminPost=adminPost,ldp=len(groupPost),lugu=len(unApprovedGroupUserList),lug=len(unApprovedGroup),lup=len(UnApprovedPostList),lus=len(unApprovedUserList),dailyPost=groupPost,unApprovedUserList=unApprovedUserList,UnApprovedPostList=UnApprovedPostList,unApprovedGroup=unApprovedGroup,unApprovedGroupUserList=unApprovedGroupUserList)
    else:
        return render_template('LoginPage.html')