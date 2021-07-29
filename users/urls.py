
from django.urls import path
from users import views as user_view
from django.urls import reverse_lazy

app_name = 'custom_auth'
urlpatterns = [
    path('register/', user_view.RegisterView.as_view(), name ='register'),
    path('login/', user_view.LoginView.as_view(), name ='login'),
    
]