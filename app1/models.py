from app1 import db

class User(db.Model): 
    userid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=True)

    # 表格更名
    __tablename__ = 'user'

    # 初始化每个实例。
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Blog(db.Model):
    blodid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    blogtopic = db.Column(db.String(100),nullable=False)
    blogcontent = db.Column(db.Text,nullable=False)

    # 表格更名
    __tablename__ = 'blog'

    def __init__(self,blogtopic,blogcontent):
        self.blogtopic = blogtopic
        self.blogcontent = blogcontent
