from flask import render_template
from flask import request,Response
import json
#导入蓝本 main
from . import main
from app1.models import Blog
from app1 import db

@main.route('/delblog', methods=('GET','POST'))
def delblog():
    if request.method == "POST":
        print("delblog post")
        
        jsondata = json.loads(request.data)
        print(jsondata["blogid"])
        blogid = jsondata["blogid"]
        
        blog = Blog.query.filter_by(blodid=blogid).first()
        db.session.delete(blog)
        db.session.commit()
        return Response("200")

    if request.method == "GET":
        print("delblog get")
        return render_template("index.html") 
