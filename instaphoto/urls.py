from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('/', views.signup, name='signup'),
]
