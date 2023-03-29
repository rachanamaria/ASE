from project import db
from project.com.vo.groupVo import GroupVo
from project.com.vo.UserGroupVo import UserGroupVo

from project.com.dao.UserGroupDAO import UserGroupDAO
from project.com.dao.UserDAO import UserDAO
from project.com.vo.UserVo import UserVo


UserGroupDao=UserGroupDAO()
userGroupVo=UserGroupVo()
userDao=UserDAO()
userVo=UserVo()
# groupVo=GroupVo()
class GroupDAO:
    def addGroup(self, GroupVo):
        db.session.add(GroupVo)
        db.session.commit()

    def addDefaultGroups(self, UserVo):
        familyGroup=GroupVo()
        familyGroup.AdminId=UserVo.UserId
        familyGroup.Status=1
        familyGroup.AdminName=UserVo.UserName
        familyGroup.GroupName='Family'
        
        friendsGroup=GroupVo()
        friendsGroup.AdminId=UserVo.UserId
        friendsGroup.Status=1
        friendsGroup.AdminName=UserVo.UserName
        friendsGroup.GroupName='Friends'

        db.session.add(familyGroup)
        db.session.add(friendsGroup)
        db.session.commit()
        
    def getAllGroup(self):
        print('inside getr all group')
        groups=GroupVo.query.all()
        print('group dao',groups)
        for g in groups:
            print(g.GroupName)
        return groups
    def getGroupsByGroupname(self,GroupName):
        groups=GroupVo.query.filter_by(GroupName = GroupName).all()
        return groups

    def getGroupsWhereAdminId(self,UserId):
        groups=GroupVo.query.filter_by(AdminId = UserId).all()
        return groups
    def getGroupsByGroupId(self,GroupId):
        group=GroupVo.query.filter_by(GroupId = GroupId).all()
        return group
    
    def UnApporvedGroup(self):
        # AdminId=UserId
        # userId,GroupId
        dic={}
        user=UserVo()
        groups=GroupVo.query.filter_by(Status=0).all()
        # for i in groups:
            # getByUserId
        return groups

    def apporvedGroup(self,GroupId):
        group=self.getGroupsByGroupId(GroupId)
        group[0].Status=1
        db.session.commit()
        return 1
    
    def DeActivateGroup(self, GroupId):
        group=self.getGroupsByGroupId(GroupId)
        group=group[0]
        group.Status=0
        db.session.commit()

    def activeGroups(self):
        print('activeGroups........ ')
        groups=GroupVo.query.filter_by(Status = 1).all()
        activeGroupUser=[]
        for j in groups:
            user=userGroupVo.query.filter_by(GroupId = j.GroupId).filter_by(Status = 1).all()
            activeGroupUser.append([j,user])
        print(activeGroupUser)
        return activeGroupUser