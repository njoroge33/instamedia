from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.signup, name='signup'),
    re_path(r'^login/', LoginView.as_view(), name='login_url'),
]
