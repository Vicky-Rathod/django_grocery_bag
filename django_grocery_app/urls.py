from django.urls import path,re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
urlpatterns = [
    path('', grocery_home,name = 'index'),
    path('add/',grocery_add,name ='add'),
    re_path(r'^(?P<pk>\d+)/update/$',grocery_update,name = 'update'),
    re_path(r'^(?P<pk>\d+)/details/$',grocery_details,name = 'detail'),
    path('logout/user/login/', auth.LogoutView.as_view(), {'template_name': 'logged_out.html'}, name = 'logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)