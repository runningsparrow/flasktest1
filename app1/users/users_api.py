from flask import jsonify, request
from flask import render_template
from flask import request,Response

#导入蓝本 main
from app1.main import main
from app1.models import User
from app1.auth.auths import Auth
from app1 import utils

#注册
@main.route('/reg', methods=('GET','POST'))
def reg():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        """
        用户注册
        :return: json
        """
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(email=email, username=username, password=utils.set_password(password))
        result = User.add(User, user)
        if user.userid:
            returnUser = {
                'id': user.userid,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time
            }
            return jsonify(utils.trueReturn(returnUser, "用户注册成功"))
            # success = utils.trueReturn(returnUser, "用户注册成功")
            # return render_template('register.html',**success)
        else:
            return jsonify(utils.falseReturn('', '用户注册失败'))
            # failed = utils.falseReturn('', '用户注册失败')
            # return render_template('register.html',**failed)


# #注册
# @main.route('/regprocess', methods=('GET','POST'))
# def registerprocess():
#     """
#     用户注册
#     :return: json
#     """
#     email = request.form.get('email')
#     username = request.form.get('username')
#     password = request.form.get('password')
#     user = User(email=email, username=username, password=utils.set_password(password))
#     result = User.add(User, user)
#     if user.userid:
#         returnUser = {
#             'id': user.userid,
#             'username': user.username,
#             'email': user.email,
#             'login_time': user.login_time
#         }
#         return jsonify(utils.trueReturn(returnUser, "用户注册成功"))
#         # success = utils.trueReturn(returnUser, "用户注册成功")
#         # return render_template('register.html',**success)
#     else:
#         return jsonify(utils.falseReturn('', '用户注册失败'))
#         # failed = utils.falseReturn('', '用户注册失败')
#         # return render_template('register.html',**failed)


#登陆
@main.route('/login', methods=('GET','POST'))
def login():
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
            'id': user.userid,
            'username': user.username,
            'email': user.email,
            'login_time': user.login_time
        }
        result = utils.trueReturn(returnUser, "请求成功")
    return jsonify(result)