"""boom_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
import rest_framework
from tsrm.views import *
from django.conf import settings
from django.conf.urls.static import static

# from rest_framework import routers

app_name = 'tsrm'

# router = routers.DefaultRouter()
# router.register(r'todo_board', tsrm)

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$', tsrm.as_view(), name = 'todo'),
    url(r'^todo_list/$', tsrm.as_view(), name = 'todo_list'),
    url(r'^todo_list/create/$', tsrmc.as_view(), name = 'todo_create'),
    url(r'^todo_list/(?P<no>\d+)/$', tsrmd.as_view(), name = 'todo_detail'),
    url(r'^todo_list/(?P<no>\d+)/update/$', tsrmu.as_view(), name = 'todo_update'),
    url(r'^todo_list/(?P<no>\d+)/delete/$', tsrmdd.as_view(), name = 'todo_delete'),

    url(r'^apis/$', apis.as_view(), name = 'api_see'),
    url(r'^apis/apic/$', apic.as_view(), name = 'api_create')
    
    # url('list', tsrm.as_view()),
    # url(r'^', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

