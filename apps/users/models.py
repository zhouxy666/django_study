from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='昵称', default='')
    birthday = models.DateField(verbose_name='出生日期', null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=(('male', '男'), ('female', '女')), default='male')
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, verbose_name='联系方式', null=True, blank=True)
    image = models.ImageField(max_length=100, verbose_name='照片', upload_to='image/user/%Y-%m',
                              default='image/user/default.png')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='邮箱验证码')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '找回密码')), max_length=10, verbose_name='发送类型')
    send_time = models.DateField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(max_length=100, verbose_name='轮播图', upload_to='image/banner/%Y-%m')
    url = models.URLField(max_length=20, verbose_name='图片链接')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
