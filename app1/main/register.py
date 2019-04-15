from flask import render_template
import json
#导入蓝本 main
from . import main

@main.route('/reg')
def register():
    # return render_template('index.html')
    # return("regiseter")
    return (json.dumps({"user":"sparrow","email":"runningsparrow@gmail.com"}))
