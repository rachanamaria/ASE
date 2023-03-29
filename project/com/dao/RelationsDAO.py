from project import db
from project.com.vo.UserRelationsVo import UserRelationsVo
from project.com.vo.UserVo import UserVo
from project.com.dao.UserDAO import UserDAO


userDAO=UserDAO()
class RelationsDAO:
    def addRelation(self, vo):
        user=UserRelationsVo.query.filter_by(UserId = vo.UserId).filter_by(Relation='Friend').filter_by(User2Id=vo.User2Id).all()
        print('user:',user)
        if len(user)==0:
            db.session.add(vo)
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