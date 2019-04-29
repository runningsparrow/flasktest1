from app1 import db
from app1.utils import session_commit

class User(db.Model): 
    userid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=True)
    login_time = db.Column(db.Integer)

    # 表格更名
    __tablename__ = 'user'

    # 初始化每个实例。
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def get(self, id):
        return self.query.filter_by(id=id).first()

    def add(self, user):
        db.session.add(user)
        return session_commit(db)

    def update(self):
        return session_commit(db)

    def delete(self, id):
        self.query.filter_by(id=id).delete()
        return session_commit(db)

class Blog(db.Model):
    blodid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    blogtopic = db.Column(db.String(100),nullable=False)
    blogcontent = db.Column(db.Text,nullable=False)

    # 表格更名
    __tablename__ = 'blog'

    def __init__(self,blogtopic,blogcontent):
        self.blogtopic = blogtopic
        self.blogcontent = blogcontent
