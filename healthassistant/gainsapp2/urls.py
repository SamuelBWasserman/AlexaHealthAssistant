"""Directing URLs and calling functions in the views method"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.scrapper, name='scrapper'),
]
