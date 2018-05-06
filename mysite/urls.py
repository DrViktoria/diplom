from django.conf.urls import url, include
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^admin/', admin.site.urls, name='admin'),
]