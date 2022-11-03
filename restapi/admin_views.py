from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer
from .models import job,User,application,spez
from .views import register,authuser,authMMe,authCce,authCse,authEce

def create_job(request):
    dept = request.data.get("dept")
    if dept.code =="cse":
        user = authCse(request)
    if dept.code =="ece":
        user = authEce(request)
    if dept.code =="cce":
        user = authCce(request)
    if dept.code =="mec":
        user = authMMe(request)
    if user:
        
@api_view(['POST'])
def nextRnd(request):
    jb=job.objects.filter(id=request.data.get("id"))
    jb.round+=1
    jb.save()

@api_view(['POST'])
def schedule(request):
    jb=job.objects.filter(id=request.data.get("id"))
    jb.schedule = request.data.get("datetime")
    jb.save()