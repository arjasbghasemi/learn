from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('^signin/$', signin, name='signin'),
    re_path('^signup/$', signup, name='signup'),
    re_path('^signout/$', signout, name='signout'),


]
