from django.urls import path,re_path

from .views import register,login,authuser,authCce,authCse,authEce,authMMe,grant_Perms
from .admin_views import create_job,nextRnd,schedule,Fetch_Jobs,add_dept,add_spez,delete_job,Fetch_applications,Reject
from .application_views import register_Application,get_details,update_Application,delete_app
from .dev_views import all_Jobs

urlpatterns = [
    path('cj',create_job),
    path('ua',update_Application),
    path('aj',all_Jobs),
    path('dj',delete_job),
    path('ra',register_Application),
    path('fj',Fetch_Jobs),
    path('sc',schedule),
    path('nr',nextRnd),
    path('rg',register),
    path('lg',login),
    path('au',authCse),
    path('gp',grant_Perms),
    path('ad',add_dept),
    path('as',add_spez),
    path('fa',Fetch_applications),
    path('rj',Reject),
    path('da',delete_app),



    path('gd',get_details)

]