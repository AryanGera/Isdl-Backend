from django.urls import path,re_path
from .user_views import create_job
from .views import register,login,authuser,authCce,authCse,authEce,authMMe,grant_Perms

urlpatterns = [
    path('create_job',create_job),
    path('rg',register),
    path('lg',login),
    path('au',authuser),
    path('gp',grant_Perms)
]