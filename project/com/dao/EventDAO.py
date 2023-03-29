from project import db
from project.com.dao.RelationsDAO import RelationsDAO
from project.com.vo.EventVo import EventVo
from project.com.dao.PostDAO import PostDAO
from project.com.DTO.EventPostObject import EventPostObject

postDAO=PostDAO()
eventVo=EventVo()

relationsDAO=RelationsDAO()
class EventDAO:
    def add(self, vo):
        db.session.add(vo)
        db.session.commit()
    
    def fetchAllEvents(self,UserId):
        dic=relationsDAO.getAllRelations(UserId)
        print('dic...',dic)
        postIds=[]
        events=[]
        for i,j in dic.items():
            data=eventVo.query.filter_by(UserId = i).filter_by(Visibility = j).all()
            for k in data:
                obj=EventPostObject(k.EventName,None,None)
                events.append(obj)
                postIds.append(k.PostId)
        for p in range(len(postIds)):
            pst=postDAO.getPostByPostId(postIds[p])
            comments=[]
            events[p].post=pst
            # fetch all the comments for a post using post_id postIds[p] and replace it with comments line below
            events[p].comments=comments
        return events