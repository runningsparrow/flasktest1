import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345678' 
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod    
    def init_app(app):        
        print(app)
        print("start....") 


class DevelopmentConfig(Config):    
    DEBUG = True    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or "mysql+pymysql://root:sparrow1@127.0.0.1:3306/flasktest1"
    print("===========")
    print(SQLALCHEMY_DATABASE_URI)
    print("============")

class TestingConfig(Config):    
    TESTING = True    
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or "mysql+pymysql://root:sparrow1@127.0.0.1:3306/flasktest1"

class ProductionConfig(Config):    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:sparrow1@127.0.0.1:3306/flasktest1"


config1 = {    
    'development': DevelopmentConfig,    
    'testing': TestingConfig,    
    'production': ProductionConfig,    
    'default': DevelopmentConfig
}

