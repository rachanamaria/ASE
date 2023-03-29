from project import db
from project.com.vo.UserRelationsVo import UserRelationsVo

class RelationsDAO:
    def addRelation(self, vo):
        db.session.add(vo)
        db.session.commit()
    
    def getAllRelations(self,UserId):
        dic={}
        ans=UserRelationsVo.query.filter_by(UserId = UserId).all()
        for i in ans:
            dic[i.User2Id]=i.Relation
        return dic