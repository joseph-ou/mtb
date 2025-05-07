from django.urls import path
from rest_framework import routers

from .views import account

router=routers.SimpleRouter()

#其他注册方法
# router.register(r'users', account.UserViewSet, basename='users')

urlpatterns = [
    path('auth/', account.AuthViews.as_view()),
    path('test/', account.TestViews.as_view()),
]

urlpatterns+=router.urls