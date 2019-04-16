from flask import render_template
from flask import request,Response
import json
#导入蓝本 main
from . import main
from app1.models import Blog
from app1 import db

@main.route('/revblog', methods=('GET','POST'))
def revblog():
    if request.method == 'POST':
        print("POST")
        # return render_template("revblog.html")
        blogid = request.args.get("blogid")
        if blogid == None:
            pass
            return null
        else:
            print(blogid)
            #query 
            data = Blog.query.filter_by(blodid=blogid).first()
            print(data)
            print(data.blogtopic)
            context={
                'blogid':data.blodid,
                'blogtopic':data.blogtopic,
                'blogcontent':data.blogcontent
            }
            return Response(json.dumps(context))

    if request.method == 'GET':
        print("GET")
        blogid = request.args.get("blogid")
        blogtopic = request.args.get("blogtopic")
        blogcontent = request.args.get("blogcontent")
        if blogid == None:
            pass
            return render_template("revblog.html")
        else:
            print(blogid)
            #query 
            data = Blog.query.filter_by(blodid=blogid).first()
            print(data)
            print(data.blogtopic)
            context={
                'blogid':data.blodid,
                'blogtopic':data.blogtopic,
                'blogcontent':data.blogcontent
            }
            return render_template("revblog.html",**context)
            # return Response(json.dumps(context))
        