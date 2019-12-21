from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.signup, name='signup'),
    re_path(r'^home/', views.index, name='home'),
    re_path(r'^login/', LoginView.as_view(), name='login_url'),
    re_path(r'^logout/', LogoutView.as_view(next_page='signup'), name='logout_url'),
]
