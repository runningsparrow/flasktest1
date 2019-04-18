1 首先在目标的 windows环境安装与源windows机器相同的 python版本(本例使用3.7.2),配置好环境变量
  然后安装 virtualenv
  参考安装语句  pip install virtualenv 


2 将flask项目解压到  目录 xx
  进入项目虚拟环境所在目录上一层执行 
  Virtualenv 虚拟环境目录 


3 安装mysql 
建立一个数据库，本例同项目名称(flasktest1)

4 修改  项目根目录/config.py 
Mysql 的用户名密码

mysql+pymysql://username:password@127.0.0.1:3306/flasktest1

  
5 执行虚拟环境/Scripts/activate.bat 进入虚拟目录

删除 项目根目录/migrations

然后打开cmd, 在项目根目录执行 
Python manage.py db init
Python manage.py db migrate
Python manage.py db upgrade

6 运行项目
Python manage.py runserver 

默认地址  http://localhost:5000