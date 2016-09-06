"""
redis_test앱내에서 필요한 url 설정을 합니다
"""
from django.conf.urls import url
from . import views

urlpatterns = {
     url(r'^$', views.main_view, name='main_view'),
     url(r'^(?P<page_alias>.+?)/$', views.visit_count),
}
