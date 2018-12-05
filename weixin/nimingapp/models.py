from django.db import models

# Create your models here.

from django.contrib.auth.models import User 
#导入Django自带用户模块

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sex = models.CharField(max_length=10)
    year =models.CharField(max_length=10)
    mess = models.CharField(max_length=150)
    time = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = '匿名消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mess