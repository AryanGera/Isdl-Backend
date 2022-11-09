from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer, application_Serializer, UserLoginSerializer, dept_Serializer, spez_Serializer
from .models import job, User, application, spez, department
from .views import register, authuser, authMMe, authCce, authCse, authEce, authDofa
from django.db.models.query import QuerySet


@api_view(['GET'])
def FetchAllJobs(request):
    jobs = job.objects.all()
    return Response(JobSerializer(jobs, many=True).data)
# made by - Aryan Gera 20UCS032
# made by - Aryan Gera 20UCS032
# made by - Aryan Gera 20UCS032

@api_view(['GET'])
def FetchAllDept(request):
    depts = department.objects.all()
    return Response(dept_Serializer(depts, many=True).data)

@api_view(['GET'])
def FetchAllSpez(request):
    specializations = spez.objects.all()
    return Response(spez_Serializer(specializations, many=True).data)
