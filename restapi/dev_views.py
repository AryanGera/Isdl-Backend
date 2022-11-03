from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer,UserSerializer,dept_Serializer,spez_Serializer
from .models import job,User,application,spez,department
from .views import register,authuser

@api_view(['GET'])
def all_Jobs(request):
    jbs = job.objects.all()
    return Response(JobSerializer(jbs,many=True).data)

@api_view(['GET'])
def all_apps(request):
    jbs = application.objects.all()
    return Response(application_Serializer(jbs,many=True).data)
    

@api_view(['GET'])
def all_Users(request):
    jbs = User.objects.all()
    return Response(UserSerializer(jbs,many=True).data)
    
@api_view(['GET'])
def all_dept(request):
    jbs = department.objects.all()
    return Response(dept_Serializer(jbs,many=True).data)
    
@api_view(['GET'])
def all_spez(request):
    jbs = spez.objects.all()
    return Response(spez_Serializer(jbs,many=True).data)
    


