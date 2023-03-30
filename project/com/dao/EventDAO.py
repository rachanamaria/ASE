from project import db
from project.com.dao.CommentDAO import CommentDAO
from project.com.dao.RelationsDAO import RelationsDAO
from project.com.vo.EventVo import EventVo
from project.com.dao.PostDAO import PostDAO
from project.com.DTO.EventPostObject import EventPostObject

postDao=PostDAO()
eventVo=EventVo()
commentDao =CommentDAO()
relationsDAO=RelationsDAO()

class EventDAO:
    def add(self, vo):
        db.session.add(vo)
        db.session.commit()
    
    def fetchAllEvents(self,UserId):
        dic=relationsDAO.getAllRelations(UserId)
        # print('dic...',dic)
        selfPost=[]
        postIds=[]
        events=[]
        for i,j in dic.items():
            data=eventVo.query.filter_by(UserId = i).filter_by(Visibility = j).all()
            for k in data:
                obj=EventPostObject(k.EventName,None,None)
                events.append(obj)
                postIds.append(k.PostId)
        for p in range(len(postIds)):
            pst=postDao.getPostByPostId(postIds[p])
            commentByPost = commentDao.getCommentByPostId(postIds[p])
            events[p].post=pst
            # fetch all the comments for a post using post_id postIds[p] and replace it with comments line below
            events[p].comments=commentByPost
        selfPost=eventVo.query.filter_by(UserId = UserId).all()
        for k in selfPost:
            obj=EventPostObject(k.EventName,None,None)
            events.append(obj)
            postIds.append(k.PostId)
            pst=postDao.getPostByPostId(postIds[p])
            commentByPost = commentDao.getCommentByPostId(postIds[p])
            events[-1].post=pst
            # fetch all the comments for a post using post_id postIds[p] and replace it with comments line below
            events[-1].comments=commentByPost
        return events