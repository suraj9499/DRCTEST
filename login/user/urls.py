
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
  path('register/', views.RegisterFormView.as_view(), name='register'),
  path('home/', views.Home.as_view(), name='home'),
  path('File_list/', views.File_list.as_view(), name='File_list'),


] 