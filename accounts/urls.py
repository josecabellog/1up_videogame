
from django.urls import path, include 
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('/auth/', include("django.contrib.auth.urls")),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', home, name= 'home'),
    path('login/', auth_view.LoginView.as_view(template_name= 'registration/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout1'),
]