from django.urls import path,re_path

from .views import register,login,authuser,authCce,authCse,authEce,authMMe,grant_Perms
from .admin_views import create_job,nextRnd,schedule


urlpatterns = [
    path('cj',create_job),
    path('sc',schedule),
    path('nr',nextRnd),
    path('rg',register),
    path('lg',login),
    path('au',authCse),
    path('gp',grant_Perms)
]