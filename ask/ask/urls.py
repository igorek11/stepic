"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based viewsll
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns, url
from  qa  import views

urlpatterns = patterns('',                                              
   url(r'^$', views.question_all, name='question_all'),                                                              
   url(r'^login/', views.test, name='login'),                                    
   url(r'^signup/', views.test, name='signup'),                                   
   url(r'^question/(?P<question_id>\d+)/$', views.question,name='question'),                
   url(r'^ask/', views.test, name='ask'),                                         
   url(r'^popular/', views.popular, name='popular'),                                 
   url(r'^new/', views.test, name='new'),                                         
) 
