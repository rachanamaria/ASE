from project.com.vo.PostVo import PostVo

class EventPostObject:
    def __init__(self,eventName,postVo,comments):
        self.eventName=eventName
        self.post=postVo
        self.comments=comments