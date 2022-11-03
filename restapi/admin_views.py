from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer,dept_Serializer,spez_Serializer
from .models import job,User,application,spez,department
from .views import register,authuser,authMMe,authCce,authCse,authEce,authDofa





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
        app=application.objects.filter(id=request.data.get("id")).first()
        app.roundNum+=1
        app.save()
        return Response({"Round updated to":app.roundNum})
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
        app=application.objects.filter(id=request.data.get("id")).first()
        app.schedule = request.data.get("datetime")
        app.save()
    else:
        return Response({"auth error":"bad auth"})

@api_view(['GET'])
def Fetch_Jobs(request):
    jobs = []
    user = authCse(request)
    if user:
        jobs+=list(job.objects.filter(dept=department.objects.filter(code="cse").first()))
    user=None
    user = authEce(request)
    if user:
        jobs+=list(job.objects.filter(dept=department.objects.filter(code="ece").first()))
    user=None
    user = authCce(request)   
    if user:
        jobs+=list(job.objects.filter(dept=department.objects.filter(code="cce").first()))
    user=None
    user = authMMe(request)
    if user:
        jobs+=list(job.objects.filter(dept=department.objects.filter(code="mec").first()))
    user=None
    if len(jobs):
        return Response(JobSerializer(jobs,many=True).data)
    else:
        return Response({"auth error":"bad_auth"})

@api_view(['GET'])
def Fetch_applications(request):
    user = None
    jb = job.objects.filter(id=request.data.get("job_id")).first()
    code = jb.dept.code
    if code =="cse":
        user = authCse(request)
    if code =="ece":
        user = authEce(request)
    if code =="cce":
        user = authCce(request)
    if code =="mec":
        user = authMMe(request)
    if user:
        cand = application.objects.filter(job=jb)
        return Response(application_Serializer(cand,many=True).data)
    else:
        return Response({"auth error":"bad auth"})

@api_view(['GET'])
def Reject(request):
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
        app=application.objects.filter(id=request.data.get("id")).first()
        app.delete()
        return Response({"Succesful Action":"Application Deleted"})
    else:
        return Response({"auth error":"bad auth"})

@api_view(['POST'])
def add_dept(request):
    user = authDofa(request)
    ds = dept_Serializer(data=request.data)
    if user and ds.is_valid():
        ds.save()
        return Response(ds.data)
    else:
        return Response({"bad":"input"})

@api_view(['POST'])
def add_spez(request):
    user = authDofa(request)
    ss = spez_Serializer(data=request.data)
    if user and ss.is_valid():
        ss.save()
        return Response(ss.data)
    else:
        return Response({"bad":"input"})

