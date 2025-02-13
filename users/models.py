from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    """用户信息(扩展用户模型,扩展django内置用户发生）"""
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户")
    nickname = models.CharField('昵称', max_length=23, blank=True, default='')
    desc = models.CharField('个人简介', max_length=200, blank=True, default='')
    gexing = models.CharField('个性签名', max_length=100, blank=True, default='')
    phone = models.CharField('手机号', max_length=11, blank=True, default='')
    birthday = models.DateField('生日', null=True, blank=True)
    gender = models.CharField('性别', max_length=6, choices=(
        ('male', '男'), ('female', '女')), default='female')
    address = models.CharField("地址", max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=100,
                              verbose_name="用户头像")

    class Meta:
        verbose_name = "用户数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.owner.username


# null为空表示 数据库中该字段可以为空，default为空表示数据库中默认为空；blank为空表示表单验证时该字段可以为空


class EmailVerifyRecord(models.Model):
    """ 邮箱验证码校验记录 """
    code = models.CharField('验证码', max_length=20)
    email = models.EmailField("邮箱", max_length=50)
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码")), default='register',
                                 max_length=10)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
