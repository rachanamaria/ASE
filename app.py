from project import app
from project import db



if __name__=='__main__':
    app.run(debug=True,threaded=True, port=8000)
    reload=True

