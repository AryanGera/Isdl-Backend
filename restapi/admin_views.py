from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer
from .models import job,User,application,spez,department
from .views import register,authuser,authMMe,authCce,authCse,authEce





@api_view(['POST'])
def create_job(request):
    code = request.query_params.get('code',None)
    user=None
    if code =="cse":
        print("auth tried")
        user = authCse(request)
    if code =="ece":
        user = authEce(request)
    if code =="cce":
        user = authCce(request)
    if code =="mec":
        user = authMMe(request)
    if user:
        dept = department.objects.filter(code=code).first()
        js = JobSerializer(data=request.data)
        print(dept.id)
        if js.is_valid():
            jb=js.save()
        else:
            return Response({"bad":"input"})
        jb.dept = dept
        if js.is_valid():
            jb=js.save()
        else:
            return Response({"bad":"department"})
        return Response(jb.dept.name)
    else:
        return Response({"bad":"auth"})

@api_view(['POST'])
def delete_job(request):
    code = request.query_params.get('code',None)
    if code =="cse":
        user = authCse(request)
    if code =="ece":
        user = authEce(request)
    if code =="cce":
        user = authCce(request)
    if code =="mec":
        user = authMMe(request)
    if user:
        jb = job.objects.get(id=request.data.get("job_id")).first()
        jb.delete()
        return Response({"job":"deleted"})
        
    else:
        return Response({"bad":"auth"})


@api_view(['POST'])
def nextRnd(request):
    code = request.query_params.get('code',None)
    if code =="cse":
        user = authCse(request)
    if code =="ece":
        user = authEce(request)
    if code =="cce":
        user = authCce(request)
    if code =="mec":
        user = authMMe(request)
    if user:
        jb=job.objects.filter(id=request.data.get("id")).first()
        jb.roundNum+=1
        jb.save()
        return Response({"Round updated to":jb.roundNum})
    else:
        return Response({"auth error":"bad auth"})

@api_view(['POST'])
def schedule(request):
    code = request.query_params.get('code',None)
    if code =="cse":
        user = authCse(request)
    if code =="ece":
        user = authEce(request)
    if code =="cce":
        user = authCce(request)
    if code =="mec":
        user = authMMe(request)
    if user:
        jb=job.objects.filter(id=request.data.get("id")).first()
        jb.schedule = request.data.get("datetime")
        jb.save()
    else:
        return Response({"auth error":"bad auth"})
