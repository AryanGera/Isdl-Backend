from django.urls import path,re_path
from .user_views import create_job
from .views import register,login,authuser

urlpatterns = [
    path('create_job',create_job),
    path('rg',register),
    path('lg',login),
    path('au',authuser),

]