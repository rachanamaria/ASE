from project import db
from project.com.vo.UserRelationsVo import UserRelationsVo
from project.com.vo.UserVo import UserVo
from project.com.dao.UserDAO import UserDAO


userDAO=UserDAO()
class RelationsDAO:
    def addRelation(self, vo1,vo2):
        user=UserRelationsVo.query.filter_by(UserId = vo1.UserId).filter_by(User2Id=vo1.User2Id).all()
        user2=UserRelationsVo.query.filter_by(UserId = vo1.User2Id).filter_by(User2Id=vo1.UserId).all()
        if len(user)==0 and len(user2)==0:
            db.session.add(vo1)
            db.session.add(vo2)
            db.session.commit()
    
    def getAllRelations(self,UserId):
        dic={}
        ans=UserRelationsVo.query.filter_by(UserId = UserId).all()
        for i in ans:
            dic[i.User2Id]=i.Relation
        return dic


    def getFriends(self,UserId):
        friends=[]
        users=UserRelationsVo.query.filter_by(UserId = UserId).filter_by(Relation='Friend').all()
        for i in users: 
            print(i.User2Id)
            friends.append(userDAO.getByUserId(i.User2Id))
            print(friends[-1].UserName)
        return friends
    
    def getFamily(self,UserId):
        friends=[]
        users=UserRelationsVo.query.filter_by(UserId = UserId).filter_by(Relation='Family').all()
        for i in users: 
            print(i.User2Id)
            friends.append(userDAO.getByUserId(i.User2Id))
            print(friends[-1].UserName)
        return friends