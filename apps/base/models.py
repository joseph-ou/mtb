from django.db import models

# Create your models here.

class BaseModel(models.Model):
    name=models.CharField( verbose_name='名称',max_length=255, null=True, blank=True)
