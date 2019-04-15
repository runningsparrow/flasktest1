from flask import render_template
import json
#导入蓝本 main
from . import main
from app1.models import Blog
from app1 import db

@main.route('/bloglist')
def bloglist():
    datas =  db.session.query(Blog).all()
    jsontext = []
    for data in datas:
        jsondata = {}
        #这句可以不要
        #blog = Blog('','')
        blog = data
        jsondata["blogid"] = blog.blodid
        jsondata["blogtopic"] = blog.blogtopic
        jsondata["blogcontent"] = blog.blogcontent
        jsontext.append(jsondata)
    # print(json.dumps(jsontext,ensure_ascii=False))
    return (json.dumps(jsontext,ensure_ascii=False))
