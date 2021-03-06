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
        #获取表单数据
        print(request.form.get("blogid"))
        if request.form.get("blogid") == None:  
            #处理非表单提交
            print(request.args.get("blogid"))
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
        else:        
            #处理表单提交,更新数据
            blogid = request.form.get("blogid")
            if blogid == None:
                pass
                return null
            else:
                print(blogid)
                #update
                
                #query 
                data = Blog.query.filter_by(blodid=blogid).first()
                data.blogtopic = request.form.get("blogtopic")
                data.blogcontent = request.form.get("blogcontent")
                db.session.commit()
                context={
                    'blogid':data.blodid,
                    'blogtopic':data.blogtopic,
                    'blogcontent':data.blogcontent
                }
                return render_template("revblog.html",**context)

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
            
        