from flask import Blueprint
#实例化 Blueprint 类，两个参数分别为蓝本的名字和蓝本所在包或模块，第二个通常填 __name__ 即可
main = Blueprint('main', __name__)

#将views 和 error 引入进蓝图
from . import index, errors, register, addblog, bloglist


