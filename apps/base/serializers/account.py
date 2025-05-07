from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .. import models


# class AuthSerializer(serializers.ModelSerializer):
class AuthSerializer(serializers.Serializer):
    username= serializers.CharField(label='用户名',required=True)
    password= serializers.CharField(label='密码',required=True,min_length=6)

    # class Meta:
    #     model = models.Account
    #     fields = '__all__'
    #
    # def validate(self, data):
    #     if data['password'] != data['password2']:
    #         raise ValidationError('Passwords do not match')
    #     return data


# class TestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Test
#         fields = '__all__'