from flask import render_template
from flask import request,Response
import json
#导入蓝本 main
from . import main
from app1.models import Blog
from app1 import db

@main.route('/addblog', methods=('GET','POST'))
def addblog():
    if request.method == 'POST':
        print("POST")
        btopic = request.form.get("blogtopic")
        bcontent = request.form.get("blogcontent")
        blog = Blog(btopic, bcontent)
        db.session.add(blog)
        db.session.commit()
        print(btopic)
        jsondata = {}
        jsondata["blogtopic"] = btopic
        jsondata["blogcontent"] = bcontent
        # return Response(json.dumps({"data":"0"}))
        return render_template("addblog.html")

    if request.method == 'GET':
        print("GET")
        # return Response(json.dumps({"data":"0"}))
        return render_template("addblog.html")