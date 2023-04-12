from project import db

from project.com.vo.BucketListVo import BucketListVo



bucketlistVo=BucketListVo()


class BucketListDAO:
    def add(self, vo):
        db.session.add(vo)
        db.session.commit()
    
    def delete(self, vo):
        db.session.delete(vo)
        db.session.commit()
    
    def Update(self, vo):
        
        db.session.commit()
    
    def fetchAllBucketList(self,UserId):
        
        return 