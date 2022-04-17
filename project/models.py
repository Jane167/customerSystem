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
    create_time = models.DateTimeField('注册时间', auto_now_add=True, null=False)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    nickname = models.CharField('昵称', default='', max_length=50, null=True, blank=True)
    introduction = models.CharField('个人介绍', default='', max_length=50, null=True, blank=True)

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

class ChatRecords(models.Model):
    '''在线客服聊天记录模型类'''
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='发送者', null=False)
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name='接收者', null=False)
    message = models.TextField(verbose_name='聊天信息')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')

    class Meta:
        db_table = "tb_chat_records"
        verbose_name = '客服聊天记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id