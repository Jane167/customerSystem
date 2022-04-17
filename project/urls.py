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
    url(r'^get_customer_list', views.get_customer_list),
    url(r'^edit_customer_info', views.edit_customer_info),
    url(r'^delete_customer_info', views.delete_customer_info),
    url(r'^search_member_info', views.search_member_info),
    url(r'^edit_member_info', views.edit_member_info),
    url(r'^member_send_to_customer', views.member_send_to_customer),

    


    

]
