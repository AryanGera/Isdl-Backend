from django.urls import path,re_path

from .views import register,login,authuser,authCce,authCse,authEce,authMMe,grant_Perms

urlpatterns = [
    path('rg',register),
    path('lg',login),
    path('au',authuser),
    path('gp',grant_Perms)
]