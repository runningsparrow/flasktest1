import jwt, datetime, time
from flask import jsonify
from app1.models import User
from app1 import utils
from app1 import Config

class Auth():

# （1）encode_auth_token方法用来生成认证Token

# 要生成Token需要用到pyjwt的encode方法，这个方法可以传入三个参数，如示例：

# jwt.encode(payload, config.SECRET_KEY, algorithm=’HS256′)

# 上面代码的jwt.encode方法中传入了三个参数：第一个是payload，这是认证依据的主要信息，第二个是密钥，这里是读取配置文件中的SECRET_KEY配置变量，第三个是生成Token的算法。

# 这里稍微讲一下payload，这是认证的依据，也是后续解析token后定位用户的依据，需要包含特定用户的特定信息，如本例注册了data声明，data声明中包括了用户ID和用户登录时间两个参数，在“用户鉴权”方法中，解析token完成后要利用这个用户ID来查找并返回用户信息给用户。这里的data声明是我们自己加的，pyjwt内置注册了以下几个声明：

#     “exp”: 过期时间
#     “nbf”: 表示当前时间在nbf里的时间之前，则Token不被接受
#     “iss”: token签发者
#     “aud”: 接收者
#     “iat”: 发行时间

# 要注意的是”exp”过期时间是按当地时间确定，所以设置时要使用utc时间。

    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                Config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

#     （2）decode_auth_token方法用于Token验证

# 这里的Token验证主要包括过期时间验证和声明验证。使用pyjwt的decode方法解析Token，得到payload。如：

# jwt.decode(auth_token, config.SECRET_KEY, options={‘verify_exp’: False})

# 上面的options设置不验证过期时间，如果不设置这个选项，token将在原payload中设置的过期时间后过期。

# 经过上面解析后，得到的payload可以跟原来生成payload进行比较来验证token的有效性。

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            # payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
            # 取消过期时间验证
            payload = jwt.decode(auth_token, Config.SECRET_KEY, options={'verify_exp': False})
            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

#     （3）authenticate方法用于用户登录验证

# 这个方法进行用户登录验证，如果通过验证，先把登录时间写入用户记录，再调用上面第一个方法生成token，返回给用户（用户登录成功后，据此token来获取用户信息或其他操作）。

    def authenticate(self, username, password):
        """
        用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因
        :param password:
        :return: json
        """
        userInfo = User.query.filter_by(username=username).first()
        if (userInfo is None):
            return jsonify(utils.falseReturn('', '找不到用户'))
        else:
            if (utils.check_password(userInfo.password, password)):
                login_time = int(time.time())
                userInfo.login_time = login_time
                User.update(User)
                token = self.encode_auth_token(userInfo.userid, login_time)
                return jsonify(utils.trueReturn(token.decode(), '登录成功'))
            else:
                return jsonify(utils.falseReturn('', '密码不正确'))

#     （4）identify方法用于用户鉴权

# 当用户有了token后，用户可以拿token去执行一些需要token才能执行的操作。这个用户鉴权方法就是进一步检查用户的token，如果完全符合条件则返回用户需要的信息或执行用户的操作。

# 用户鉴权的操作首先判断一个用户是否正确传递token，这里使用header的方式来传递，并要求header传值字段名为“Authorization”，字段值以“JWT”开头，并与token用“ ”（空格）隔开。

# 用户按正确的方式传递token后，再调用decode_auth_token方法来解析token，如果解析正确，获取解析出来的用户信息（user_id）并到数据库中查找详细信息返回给用户。

    def identify(self, request):
        """
        用户鉴权
        :return: list
        """
        auth_header = request.headers.get('Authorization')
        if (auth_header):
            auth_tokenArr = auth_header.split(" ")
            if (not auth_tokenArr or auth_tokenArr[0] != 'JWT' or len(auth_tokenArr) != 2):
                result = utils.falseReturn('', '请传递正确的验证头信息')
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user = User.get(Users, payload['data']['id'])
                    if (user is None):
                        result = utils.falseReturn('', '找不到该用户信息')
                    else:
                        if (user.login_time == payload['data']['login_time']):
                            result = utils.trueReturn(user.id, '请求成功')
                        else:
                            result = utils.falseReturn('', 'Token已更改，请重新登录获取')
                else:
                    result = utils.falseReturn('', payload)
        else:
            result = utils.falseReturn('', '没有提供认证token')
        return result

