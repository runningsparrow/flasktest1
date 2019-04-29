from flask import jsonify, request
from flask import render_template
from flask import request,Response

#导入蓝本 main
from app1.main import main
from app1.models import User
from app1.auth.auths import Auth
from app1 import utils


@main.route('/reg', methods=('GET','POST'))
def reg():
    return render_template('register.html')

#注册
@main.route('/regprocess', methods=('GET','POST'))
def registerprocess():
    """
    用户注册
    :return: json
    """
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    user = User(email=email, username=username, password=User.set_password(Users, password))
    result = User.add(Users, user)
    if user.id:
        returnUser = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'login_time': user.login_time
        }
        return jsonify(utils.trueReturn(returnUser, "用户注册成功"))
    else:
        return jsonify(utils.falseReturn('', '用户注册失败'))


#登陆
@main.route('/loginprocess', methods=('GET','POST'))
def loginprocess():
    """
    用户登录
    :return: json
    """
    username = request.form.get('username')
    password = request.form.get('password')
    if (not username or not password):
        return jsonify(utils.falseReturn('', '用户名和密码不能为空'))
    else:
        return Auth.authenticate(Auth, username, password)


#获取用户信息
@main.route('/userget',methods=('GET','POST'))
def userget():
    """
    获取用户信息
    :return: json
    """
    result = Auth.identify(Auth, request)
    if (result['status'] and result['data']):
        user = User.get(User, result['data'])
        returnUser = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'login_time': user.login_time
        }
        result = utils.trueReturn(returnUser, "请求成功")
    return jsonify(result)