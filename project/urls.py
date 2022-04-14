from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    url(r'^login_authentication/$', views.login_authentication),
    url(r'^register/$', views.register),
    url(r'^get_member_list', views.get_member_list),
    url(r'^get_customer_list', views.get_customer_list)

]