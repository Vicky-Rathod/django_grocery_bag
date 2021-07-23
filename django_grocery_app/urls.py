from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('', grocery_home,name = 'index'),
    path('add/',grocery_add,name ='add'),
    re_path(r'^(?P<pk>\d+)/update/$',grocery_update,name = 'update'),

]