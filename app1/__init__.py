# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *

db = SQLAlchemy()

#create_app() 就是程序的工厂函数，
# 参数就是配置类的名字，即 config.py，
# 其中保存的配置可以使用 from_object() 方法导入。
def create_app(config_name):
     #创建Flask的实例app
    app = Flask(__name__)
    #Flask有属性config（第2个config），此属性是一个Config类，
    #有方法from_object，可以用dir(app.config)查到。在后面会介绍。
    #传入from_object的参数是引入Config类。类也是对象，可以当参数传递。
    app.config.from_object(config1[config_name])
    config1[config_name].init_app(app)
    db.init_app(app)

    #引入蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

