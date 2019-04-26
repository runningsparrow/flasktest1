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
    #config1在 config.py 定义,config1[config_name]实际指向一个config类
    #可以查看def from_object(self, obj)函数代码,获取类中的每个属性
    #然后Config的所有属性，如果是大写的，将被存入以self为名字的字典中，即本例为app.config为名字的字典中。
    app.config.from_object(config1[config_name])
    #执行与不执行 init_app无区别
    #config1[config_name].init_app(app)
    #SQLALCHEMY_DATABASE_URI通过config.from_object方法获取,db.init_app 通过 app配置SQLALCHEMY_DATABASE_URI
    db.init_app(app)

    #引入蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

