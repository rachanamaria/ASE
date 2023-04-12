from project import db
from project.com.dao.RelationsDAO import RelationsDAO
from project.com.vo.TravelVo import TravelVo
from project.com.dao.PostDAO import PostDAO
from project.com.DTO.TravelPostObject import TravelPostObject
from project.com.vo.TravelVo import TravelVo
from project.com.dao.CommentDAO import CommentDAO



postDao=PostDAO()
travelVo=TravelVo()
commentDao =CommentDAO()
relationsDAO=RelationsDAO()

relationsDAO=RelationsDAO()
class TravelDAO:
    def add(self, vo):
        db.session.add(vo)
        db.session.commit()
    
    def fetchAllTravels(self,UserId):
        dic=relationsDAO.getAllRelations(UserId)
        selfPost=[]
        postIds=[]
        tarvels=[]
        for i,j in dic.items():
            data=travelVo.query.filter_by(UserId = i).filter_by(Visibility = j).all()
            for k in data:
                obj=TravelPostObject(k.TravelName,None,None)
                tarvels.append(obj)
                postIds.append(k.PostId)
        for p in range(len(postIds)):
            pst=postDao.getPostByPostId(postIds[p])
            commentByPost = commentDao.getCommentByPostId(postIds[p])
            tarvels[p].post=pst
            # fetch all the comments for a post using post_id postIds[p] and replace it with comments line below
            tarvels[p].comments=commentByPost
        selfPost=travelVo.query.filter_by(UserId = UserId).all()
        for k in selfPost:
            obj=TravelPostObject(k.TravelName,None,None)
            tarvels.append(obj)
            postIds.append(k.PostId)
            pst=postDao.getPostByPostId(k.PostId)
            commentByPost = commentDao.getCommentByPostId(k.PostId)
            tarvels[-1].post=pst
            # fetch all the comments for a post using post_id postIds[p] and replace it with comments line below
            tarvels[-1].comments=commentByPost
        return tarvels
    
    #