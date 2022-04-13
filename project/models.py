from django.db import models
from django.db import models
from django.db.models.base import Model
# Create your models here.

# Create your models here.


class UserAbstractModel(models.Model):
    """
    会员、客服和管理员角色的抽象类
    """
    ROLE_CHOICES = {
        (0, '会员'),
        (1, '客服'),
        (2, '管理员')
    }

    username = models.CharField('用户名', default='', max_length=50, null=False)
    password = models.CharField('密码', default='', max_length=50, null=False)
    created = models.DateTimeField('注册时间', auto_now_add=True, null=False)

    class Meta:
        abstract = True

# 会员的模型类


class Member(UserAbstractModel):
    """
    学生角色的模型类
    """

    role = models.IntegerField(
        verbose_name='用户角色', default='0', choices=UserAbstractModel.ROLE_CHOICES, null=False)

    def __str__(self):
        return self.username


# 公益企业
class Customer(UserAbstractModel):
    """
    公益企业角色的模型类
    """
    role = models.IntegerField(
        verbose_name='用户角色', default='1', choices=UserAbstractModel.ROLE_CHOICES, null=False)

    def __str__(self):
        return self.username


# 管理员
class Manager(UserAbstractModel):
    """
    管理员的模型类
    """
    role = models.IntegerField(
        verbose_name='用户角色', default='2', choices=UserAbstractModel.ROLE_CHOICES, null=False)

    def __str__(self):
        return self.username
