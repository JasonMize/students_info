
from django.conf.urls import  url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^students/(?P<id>\d+)/$', views.post, name='student'),
]

