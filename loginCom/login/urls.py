from django.conf.urls import url
from django.contrib import admin
from . import views

#this will help identify to which app the url is associated
app_name = 'login'

urlpatterns = [
    url(r'^$', views.homeView, name='HomeView'),
    url(r'^login/$', views.dealLogin, name='DealLogin'),
    url(r'^logout/$', views.dealLogout, name='DealLogout'),
    url(r'^reg/$', views.dealReg, name='DealReg'),
]
