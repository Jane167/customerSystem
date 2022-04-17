from logging import Logger
from turtle import update
from unittest import result
from django.dispatch import receiver
from django.shortcuts import render

from django.http import HttpResponse
import json
from django.db import DatabaseError, transaction
from django.db.models import Count
from django.db.models import Q

from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
# Create your views here.
# def hello(request):
#     return HttpResponse('Hello World!')

# 注册
def register(request):
    try:
        jsonRes = json.loads(request.body)
        username = jsonRes["username"]
        password = jsonRes["password"]
        role = jsonRes["identity"]

        user = {
            "username": username,
            "password": password,
            "role": role
        }
        # print('requestBody', jsonLoad)
        print('user用户:', user)
        if int(role) == 0:
            if Member.objects.filter(username=username):
                return JsonResponse({"result": False, "code": 101, "message": '注册失败，该用户名已经注册'})
            else:
                Member.objects.create(**user)
        elif int(role) == 1:
            if Customer.objects.filter(username=username):
                return JsonResponse({"result": False, "code": 101, "message": '注册失败，该用户名已经注册'})
            else:
                Customer.objects.create(**user)
        elif int(role) == 2:
            if Manager.objects.filter(username=username):
                return JsonResponse({"result": False, "code": 101, "message": '注册失败，该用户名已经注册'})
            else:
                Manager.objects.create(**user)

    except Exception as err:
        result = False
        message = str(err)
    else:
        result = True
        message = "注册成功！"
    return JsonResponse({"result": result, "message": message})

# 登录验证
def login_authentication(request):
    if request.method == 'POST':
        JsonRes = json.loads(request.body)
        username = JsonRes["username"]
        password = JsonRes["password"]
        role = JsonRes["identity"]
        user = {
            "username": username,
            "password": password,
            "role": role,
        }
        try:
            if int(role) == 0:
                result0 = Member.objects.filter(**user)
                if result0.exists():
                    result_data = result0.values()
                    print('resultdata', result_data)
                    id = result_data[0]['id'],
                    return JsonResponse({
                        "result": True, "code": 200, "message": '登录成功，点击确定跳转至主页！', 'id': id
                    })
                else:
                    return JsonResponse({"result": False, "code": 101, "message": '用户名或密码错误', })
            elif int(role) == 1:
                result1=Customer.objects.filter(**user)
                if result1.exists():
                    return JsonResponse({
                        "result": True, "code": 200, "message": '登录成功，点击确定跳转至主页！',
                    })
                else:
                    return JsonResponse({"result": False, "code": 101, "message": '用户名或密码错误'})
            elif int(role) == 2:
                result2=Manager.objects.filter(**user)
                if result2.exists():
                    return JsonResponse({
                        "result": True, "code": 200, "message": '登录成功，点击确定跳转至主页！',
                    })
                else:
                    return JsonResponse({"result": False, "code": 101, "message": '用户名或密码错误'})
        except Exception as error:
            print('登录失败原因：',error)
            return JsonResponse({"result": False, "code": 101, "message": '登录失败！'})
    else:
        return JsonResponse({"result": False, "code": 101, "message": '请求方法错误！'})

# 获取会员用户列表
def get_member_list(request):
    """
    获取会员列表数据
    """
    if request.method == 'GET':
        members=Member.objects.all()
        result_data=[]
        for item in members:
            result_data.append(
                {
                    "id": item.id,
                    "username": item.username,
                    "password": item.password,
                    "nickname": item.nickname,
                    "introduction": item.introduction,
                    "create_time": item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "update_time": item.update_time.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
        return JsonResponse(
            {
                "result": True, "code": 200,
                "data": result_data
            }
        )

# 获取客户用户列表
def get_customer_list(request):
    """
    获取会员列表数据
    """
    if request.method == 'GET':
        customers=Customer.objects.all()
        result_data=[]
        for item in customers:
            result_data.append(
                {
                    "id": item.id,
                    "username": item.username,
                    "password": item.password,
                    "nickname": item.nickname,
                    "introduction": item.introduction,
                    "create_time": item.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "update_time": item.update_time.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
        return JsonResponse(
            {
                "result": True, "code": 200,
                "data": result_data
            }
        )

# 编辑客服信息
def edit_customer_info(request):
    """
    编辑
    """
    if request.method == 'POST':
        jsonRes = json.loads(request.body)

        customer_id = jsonRes['id']
        kwargs = {
            "nickname": jsonRes['nickname'],
            "username": jsonRes['username'],
            "password": jsonRes['password'],
            "introduction": jsonRes['introduction']
        }

        try:
            Customer.objects.filter(id=customer_id).update(**kwargs)
            return JsonResponse({"result": True, "code": 200, "message": "修改成功!"})
        except Exception:
            return JsonResponse({"result": False, "code": 101, "message": "保存修改信息失败！"})
    else:
        return JsonResponse({"result": False, "code": 501, "message": "请求方法错误！"})


# 注销客服账号接口
def delete_customer_info(request):
    """
    删除任务数据
    """
    if request.method == 'GET':
        customer_id = request.GET.get("customer_id")
        try:
            with transaction.atomic():
                customer = Customer.objects.get(id=int(customer_id))
                customer.delete()
        except Exception:
            return JsonResponse({"result": False, "code": 101, "message": "删除任务失败！"})
        return JsonResponse(
            {
                "result": True, "code": 200,
                "message": "删除成功！"
            }
        )
    else:
        return JsonResponse({'result': False, 'code': 401, 'message': '请求方法错误！'})

#根据id查询会员用户信息
def search_member_info(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        print('id------:', id)
        if id is None:
            return JsonResponse(
                {"result": False, "code": 400, "message": "该用户不存在", "data": {}}
            )
        else:
            try:
                member = list(Member.objects.filter(id=id).values())
                print('member', member)
                member[0]['create_time'] = member[0]['create_time'].strftime("%Y-%m-%d %H:%M:%S")
                member[0]['update_time'] = member[0]['update_time'].strftime("%Y-%m-%d %H:%M:%S")

            except DatabaseError as e:
                Logger.exception(e)
                return JsonResponse(
                    {"result": True, "code": 500, "message": "查询失败(请检查日志)", "date": {}}
                )
            return JsonResponse(
                {
                    "result": True,
                    "code": 200,
                    "message": "查询成功",
                    "data": member,
                }
            )

# 用户编辑个人资料
def edit_member_info(request):
    """
    编辑
    """
    if request.method == 'POST':
        jsonRes = json.loads(request.body)

        member_id = jsonRes['id']
        kwargs = {
            "nickname": jsonRes['nickname'],
            "username": jsonRes['username'],
            "password": jsonRes['password'],
            "introduction": jsonRes['introduction']
        }

        try:
            Member.objects.filter(id=member_id).update(**kwargs)
            return JsonResponse({"result": True, "code": 200, "message": "修改成功!"})
        except Exception:
            return JsonResponse({"result": False, "code": 101, "message": "保存修改信息失败！"})
    else:
        return JsonResponse({"result": False, "code": 501, "message": "请求方法错误！"})

#用户向客服发送消息
def member_send_to_customer(request):
    if request.method == 'GET':
        sender = int(request.GET.get('sender'))
        receiver = int(request.GET.get('receiver'))
        message = request.GET.get('message')

        kwargs = {
            'sender': Member.objects.get(id = sender),
            'receiver': Customer.objects.get(id = receiver),
            'message': message
        }
        try:
            ChatRecords.objects.create(**kwargs)
            return JsonResponse({"result": True, "code": 200, "message": "发送成功!"})
        except Exception as error:
            print('发送错误原因', error)
            return JsonResponse({"result": False, "code": 101, "message": "发送失败！"})
    else:
        return JsonResponse({"result": False, "code": 501, "message": "请求方法错误！"})


