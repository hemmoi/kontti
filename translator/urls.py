from django.conf.urls import url
from . import views

app_name = 'translator'

urlpatterns = [

    url(r'^$', views.index, name='translator'),

    url(r'^process/$', views.process, name='process'),
]