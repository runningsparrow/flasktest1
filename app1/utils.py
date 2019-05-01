from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import SQLAlchemyError

#password
#加密用户注册时填写的密码和在用户登录时检查用户密码是否正确。
def set_password(password):
    return generate_password_hash(password)

def check_password(hash, password):
    return check_password_hash(hash, password)



#db 
def session_commit(db):
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason

#return
def trueReturn(data, msg):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(data, msg):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }