import jwt
import datetime

#查看orm对应的对象内容
from django.forms.models import model_to_dict


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import QueryParameterVersioning

from ..serializers.account import AuthSerializer
from .. import models
from django.conf import settings
from utils import return_code


class AuthViews(APIView):
    authentication_classes = []
    permission_classes = []

    #认证

    #版本控制
    # versioning_class = QueryParameterVersioning

    def get(self, request,*args, **kwargs):

        # print(request.version)
        # return Response('GET请求')
        return Response({"code":'100','data':'get请求成功'})


    def post(self, request,*args, **kwargs):
        # 获取用户请求发送用户名和密码
        # username=request.data.get('username')
        # password=request.data.get('password')

        # 数据校验
        ser=AuthSerializer(data=request.data)
        if not ser.is_valid():
            return Response({'code':return_code.AUTH_FAILED,'detail':ser.errors})


        # 数据库校验
        username=ser.validated_data.get('username')
        password=ser.validated_data.get('password')
        user_object=models.UserInfo.objects.filter(username=username,password=password).first()

        #查看user_object对象内容
        # user_data = model_to_dict(user_object)
        # print(user_data)

        if not user_object:
            return Response({'code':return_code.VALIDATE_FAILED,'detail':'用户名或密码错误'})

        # 生成jwt token返回

        headers={
            'typ':'jwt',
            'alg':'HS256'
        }

        #构造payload
        payload={
            'user_id':user_object.id,#自定义用户id
            'username':user_object.username,#自定义用户名
            'exp':datetime.datetime.now()+datetime.timedelta(days=7)#超时时间
        }

        token=jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256', headers=headers)





        # print(request.user)
        # print(request.auth)
        return Response({'code':return_code.SUCCESS,'data':{'token':token,'name':username}})


        # print(request.data)
        # username = request.data.get('username')
        # password = request.data.get('password')
        # user = models.User.objects.filter(username=username, password=password).first()
        # if user:
        #     return {'code': 200, 'msg': '登录成功', 'data': user.id}
        # else:
        #     return {'code': 400, 'msg': '用户名或密码错误', 'data': None}


class TestViews(APIView):


    def get(self, request, *args, **kwargs):

        #通过自定义的jwt token验证后可以直接查询request.user和request.auth
        # print(request.user.user_id)
        # print(request.user.username)
        # print(request.user.exp)
        # print(request.auth)


        return Response({'code': 0, 'detail': 'test'})
