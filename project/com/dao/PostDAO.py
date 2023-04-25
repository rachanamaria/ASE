import datetime
from project import db
from project.com.vo.PostVo import PostVo
from project.com.dao.CommentDAO import CommentDAO
from datetime import date

today = date.today()


CommentDao=CommentDAO()
class PostDAO:
    def addPost(self, PostVo,time):
        db.session.add(PostVo)
        db.session.commit()
        post=self.getpostByCreatTime(time)
        return post[0]
    
    def deletePost(self, PostId):
        post=self.getPostByPostId(PostId)[0]
        db.session.delete(post)
        db.session.commit()
        return 

    def getpostByCreatTime(self,time):
        print(time)
        post=PostVo.query.filter_by(createdTime = time).all()
        print(post)
        return post
    
    def getPostByPostId(self, PostId):
        post=PostVo.query.filter_by(PostId = PostId).one()
        return post

    def getUnapporvedPostByGroupId(self, GroupId):
        unApprovedPosts=PostVo.query.filter_by(GroupId = GroupId).all()
        return unApprovedPosts

    def getApporvedPostByGoupId(self, GroupId):
        print('inside.....getApporvedPostByGoupId')
        approvedPosts=PostVo.query.filter_by(GroupId = GroupId).all()
        postComments=[]
        for j in approvedPosts:
            comments=CommentDao.getCommentByPostId(j.PostId)
            postComments.append([j,comments])
        print('postComments:',postComments)
        return postComments
    
    def getPostByUserId(self, UserId):
        comments=[]
        posts=PostVo.query.filter_by(CreatorId = UserId).all()
        for post in posts:
            coomentByPost = CommentDao.getCommentByPostId(post.PostId)
            comments.append({'post':post,'comment':coomentByPost})
            # comments.append(coomentByPost)
        # fetch coments for each post with postId inside posts
        # store it inside a comments=[] and resturn it with post
        # posts at index 0 of posts array with have comments at index 0 of comment array
        # print(comments)
        return comments

    def getUnapporvedPost(self):
        # unApprovedPosts=PostVo.query.filter_by(Status = 0).all()
        # return unApprovedPosts
        return []

    def getApporvedPost(self):
        print('inside getApprovedPost..............')
        # approvedPosts=PostVo.query.filter_by(Status = 1).all()
        # get comment here append with post and then load it
        postComments=[]
        # for j in approvedPosts:
        #     comments=CommentDao.getCommentByPostId(j.PostId)
        #     postComments.append([j,comments])
        # print('postComments:',postComments)
        return postComments

    def apporvePost(self,PostId):
        print(PostId)
        post=self.getPostByPostId(PostId)
        post[0].Status=1
        db.session.commit()
        return 1
    
    def deletePost(self, PostId):
        

        return 
    
    def getMemoriesPost(self,UserId):
        comments=[]
        requiredPost=[]
        posts=PostVo.query.filter_by(CreatorId = UserId).all()
        for post in posts:
            dt=post.createdTime.date()
            print(dt)
            if dt.year==today.year-1 and dt.month == today.month and dt.day == today.day:
                requiredPost.append(post)
        return requiredPost
