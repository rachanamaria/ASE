from project import db
from project.com.dao.RelationsDAO import RelationsDAO
from project.com.vo.TravelVo import TravelVo
from project.com.dao.PostDAO import PostDAO

postDAO=PostDAO()
travelVo=TravelVo()

relationsDAO=RelationsDAO()
class TravelDAO:
    def add(self, vo):
        db.session.add(vo)
        db.session.commit()
    
    def fetchAllTravels(self,UserId):
        dic=relationsDAO.getAllRelations(UserId)
        postIds=[]
        posts=[]
        for i,j in dic.items():
            data=travelVo.query.filter_by(UserId = i).filter_by(Visibility = j).all()
            for k in data:
                postIds.append(k.PostId)
        for p in postIds:
            pst=postDAO.getPostByPostId(p)
            posts.append(pst)
        return posts