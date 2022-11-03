from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer
from .models import job,User,application,spez,department
from .views import register,authuser,authMMe,authCce,authCse,authEce


@api_view(['POST'])


@api_view(['POST'])
def create_job(request):
    code = "cse"
    print("code",code)
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
        # dept = department.objects.filter(code=code)
        js = JobSerializer(data=request.data)
        
        if js.is_valid():
            js.save()
        # jb.dept = dept
        return Response({"done":"done"})
    else:
        return Response({"bad":"auth"})

@api_view(['POST'])
def delete_job(request):
    code = request.query.params.get('code',None)
    if code =="cse":
        user = authCse(request)
    if code =="ece":
        user = authEce(request)
    if code =="cce":
        user = authCce(request)
    if code =="mec":
        user = authMMe(request)
    if user:
        jb = job.objects.get(id=request.data.get("job_id"))
        jb.delete()

        return Response({"job":"deleted"})
        
    else:
        return Response({"bad":"auth"})


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