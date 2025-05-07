'''userinfo创建数据的离线脚本'''

#加载离线脚本所需模块
import os
import sys
import django

#设置项目路径
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
sys.path.append(base_dir)

#加载Django项目
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mtb.settings")
django.setup()



from apps.base import models

models.UserInfo.objects.create(
    username='org',
    password='615520'
)
