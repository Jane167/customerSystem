from django.shortcuts import render

from django.http import HttpResponse
import json
from django.db import transaction
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
            if Member.objects.filter(username = username):
                return JsonResponse({"result": False, "code":101,"message": '注册失败，该用户名已经注册'})
            else:
                Member.objects.create(**user)
        elif int(role) == 1:
            if Customer.objects.filter(username = username):
                return JsonResponse({"result": False, "code":101,"message": '注册失败，该用户名已经注册'})
            else:
                Customer.objects.create(**user)
        elif int(role) == 2:
            if Manager.objects.filter(username = username):
                return JsonResponse({"result": False, "code":101,"message": '注册失败，该用户名已经注册'})
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
    JsonRes = json.loads(request.body)
    username = JsonRes["username"]
    password = JsonRes["password"]
    role = JsonRes["identity"]
    user = {
        "username": username,
        "password": password,
        "role": role,
    }
    print('登录:', JsonRes)
    print('登录用户', user)
    try:
        if int(role) == 0:
            result0 = Member.objects.filter(**user)
            if result0.exists():
                return JsonResponse({
                    "result": True, "code": 200, "message": '登录成功，点击确定跳转至主页！', 
                })
            else:
                return JsonResponse({"result": False, "code": 101, "message": '用户名或密码错误',})
        elif int(role) == 1:
            result1 = Customer.objects.filter(**user)
            if result1.exists():
                return JsonResponse({
                    "result": True, "code": 200, "message": '登录成功，点击确定跳转至主页！',
                })
            else:
                return JsonResponse({"result": False, "code": 101, "message": '用户名或密码错误'})
        elif int(role) == 2:
            result2 = Manager.objects.filter(**user)
            if result2.exists():
                return JsonResponse({
                    "result": True, "code": 200, "message": '登录成功，点击确定跳转至主页！', 
                })
            else:
                return JsonResponse({"result": False, "code": 101, "message": '用户名或密码错误'})
    except Exception as error:
        print(error)
    else:
        return JsonResponse({"result": False, "code": 101, "message": '登录失败！'})

#获取会员用户列表
def get_member_list(request):
    """
    获取会员列表数据
    """
    if request.method == 'GET':
        members = Member.objects.all()
        result_data = []
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

#获取客户用户列表
def get_customer_list(request):
    """
    获取会员列表数据
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        result_data = []
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