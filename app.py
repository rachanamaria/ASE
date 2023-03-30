from project import app
from project import db
from project.com.dao.UserDAO import UserDAO
from project.com.vo.UserVo import UserVo
from project.com.vo.UserRelationsVo import UserRelationsVo
import pandas as pd



if __name__=='__main__':
    app.run(debug=True,threaded=True, port=8000)
    reload=True

