from django.urls import path,re_path

from .views import register,login,authuser,authCce,authCse,authEce,authMMe,grant_Perms
from .admin_views import create_job,nextRnd,schedule,Fetch_Jobs,add_dept,add_spez,delete_job,Fetch_applications,Reject
from .application_views import register_Application,get_details,update_Application,delete_app
from .dev_views import all_Jobs
from .unauth_views import FetchAllDept,FetchAllJobs,FetchAllSpez
urlpatterns = [
    path('createJob',create_job),
    path('updateApp',update_Application),
    path('aj',all_Jobs),
    path('deleteJob',delete_job),
    path('registerApp',register_Application),
    path('fetchJobs',Fetch_Jobs),
    path('schedule',schedule),
    path('nextRound',nextRnd),
    path('rg',register),
    path('login',login),
    path('gp',grant_Perms),
    path('addDept',add_dept),
    path('addSpez',add_spez),
    path('fetchApp',Fetch_applications),
    path('rejectApp',Reject),
    path('deleteApp',delete_app),
    path('fetchAllJobs',FetchAllJobs),
    path('fetchAllDept',FetchAllDept),
    path('fetchAllSpez',FetchAllSpez),
    path('getDetails',get_details)

]