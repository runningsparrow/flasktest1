import os
from flask_script import Manager, Shell
from app1 import create_app,db
from flask_migrate import Migrate, MigrateCommand, upgrade
from flask_cors import CORS
#引入models
from app1.models import User, Blog

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#解决跨域问题
CORS(app, supports_credentials=True)


# 构建指令，设置当前app受指令控制（即将指令绑定给指定app对象）
manager = Manager(app)
# 构建数据库迁移操作，将数据库迁移指令绑定给指定的app和数据库
Migrate = Migrate(app, db)

def make_shell_conftext():
    return dict(app=app, db=db)

manager.add_command("shell",Shell(make_context=make_shell_conftext))
# 添加数据库迁移指令，该操作保证数据库的迁移可以使用指令操作
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()


