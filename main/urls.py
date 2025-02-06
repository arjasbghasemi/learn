from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path('^$', index, name='index'),
    re_path('^lesson/(?P<pk>\d+)$', lesson, name='lesson'),
    re_path('^lesson_menu/(?P<pk_menu>\d+)$', lesson_menu, name='lesson_menu'),
    re_path('^lesson_cat/(?P<pk_menu>\d+)/(?P<pk_cat>\d+)/$', lesson_cat, name='lesson_cat'),
    re_path('^lesson_sub_cat/(?P<pk_menu>\d+)/(?P<pk_cat>\d+)/(?P<pk_sub_cat>\d+)/$', lesson_sub_cat,
            name='lesson_sub_cat'),
    re_path('^lesson_sub_sub_cat/(?P<pk_menu>\d+)/(?P<pk_cat>\d+)/(?P<pk_sub_cat>\d+)/(?P<pk_sub_sub_cat>\d+)$',
            lesson_sub_sub_cat, name='lesson_sub_sub_cat'),
re_path('^lesson_sub_sub_sub_cat/(?P<pk_menu>\d+)/(?P<pk_cat>\d+)/(?P<pk_sub_cat>\d+)/(?P<pk_sub_sub_cat>\d+)/(?P<pk_sub_sub_sub_cat>\d+)$',
            lesson_sub_sub_sub_cat, name='lesson_sub_sub_sub_cat'),
    re_path('^search/$', search, name='search'),
    re_path('^download_file/(?P<pk>\d+)/$', download_file, name='download_file'),

]
