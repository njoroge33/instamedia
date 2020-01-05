from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.signup, name='signup'),
    re_path(r'^home/', views.index, name='home'),
    re_path(r'^login/', LoginView.as_view(), name='login_url'),
    re_path(r'^logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
    re_path(r'^newpost/', views.new_post, name='new_post'),
    re_path(r'^profile/', views.profile, name='profile'),
    re_path(r'^updateprofile/', views.update_profile, name='update_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
