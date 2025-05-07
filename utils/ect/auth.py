'''验证用 '''

import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .. import return_code


#格式化字典封装数据并且返回
class CurrentUser(object):

    def __init__(self,user_id,username,exp):
        self.user_id = user_id
        self.username = username
        self.exp = exp



class JwtTokenAuthentication(BaseAuthentication):
    '''JWT验证'''
    def authenticate(self, request):
        #读取用户提交过来的jwt token

        #在 Django REST framework 中，query_params 是 Request 对象的一个属性，它包含了 HTTP GET 请求的查询参数。查询参数是在 URL 中以键值对形式出现的，位于 ? 符号之后。
        # 例如，在 URL http://example.com/api/resource?token=12345&name=John 中，token 和 name 就是查询参数。
        # query_params 属性是一个 QueryDict 对象，它类似于 Python 的标准字典，但有一些额外的功能，比如多重键的支持（即一个键可以对应多个值）。
        # 你可以使用 query_params 来访问查询参数的值。例如：

        #第一种提取jwt token的方法
        # token = request.query_params.get('token')

        #第二种提取jwt token的方法 去请求头中提取
        token = request.META.get('HTTP_AUTHORIZATION',b'')
        print(token)

        #验证失败 抛出异常
        #raise exceptions.AuthenticationFailed('用户认证失败')
        if not token:
            raise AuthenticationFailed({'coed':return_code.AUTH_FAILED,'detail':'认证失败'})

        #验证jwt token
        #成功 return xx,xxx #request.user/request.auth
        try:
            payload= jwt.decode(token,settings.SECRET_KEY, algorithms=['HS256'])

            # print(payload)#{'user_id': 1, 'username': 'org', 'exp': 1736250550}
            return CurrentUser(**payload),token


        except Exception as e:
            raise AuthenticationFailed({'coed':return_code.AUTH_FAILED,'detail':'认证失败'})


    def authenticate_header(self, request):
        #返回响应头

        return 'Bearer realm="API"'