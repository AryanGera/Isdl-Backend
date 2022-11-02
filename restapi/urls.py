from django.urls import path,re_path
from .user_views import create_job
urlpatterns = [
    path('create_job',create_job)
]