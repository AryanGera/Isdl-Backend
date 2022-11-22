from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer,dept_Serializer,spez_Serializer,post_Serializer
from .models import job,User,application,spez,department,post
from .views import register,authuser,authMMe,authCce,authCse,authEce,authDofa,authAdmin
from django.db.models.query import QuerySet
from .generateMeet import sendMail




@api_view(['POST'])
def create_job(request):
    dept_id = request.data.get("dept")
    depart  = department.objects.get(id=dept_id)
    code = depart.code
    user=None
    if code == 'cse':
        print("auth tried")
        user = authCse(request)
    if code == 'ece':
        user = authEce(request)
    if code == 'cce':
        user = authCce(request)
    if code == 'mec':
        user = authMMe(request)
    if user:
        dept = department.objects.filter(id=dept_id).first()
        js = JobSerializer(data=request.data)
        print(dept.id)
        if js.is_valid():
            jb=js.save()
        else:
            return Response(js.errors,400)
        
        return Response(jb.dept.name)
    else:
        return Response({"auth":"error"},401)

@api_view(['POST'])
def delete_job(request):
    jb = job.objects.get(id=request.data.get("id"))
    print(jb.dept)
    dept_id = jb.dept.id
    depart  = department.objects.get(id=dept_id)
    code = depart.code
    user=None
    if code == 'cse':
        print("auth tried")
        user = authCse(request)
    if code == 'ece':
        user = authEce(request)
    if code == 'cce':
        user = authCce(request)
    if code == 'mec':
        user = authMMe(request)
    if user:
        jb.delete()
        return Response({"job":"deleted"})
        
    else:
        return Response({"auth":"error"})
# made by - Aryan Gera 20UCS032


@api_view(['POST'])
def nextRnd(request):
    app=application.objects.filter(id=request.data.get("id")).first()
    jb = job.objects.get(id=app.job.id)
    dept_id = jb.dept.id
    depart  = department.objects.get(id=dept_id)
    code = depart.code
    user=None
    if code == 'cse':
        print("auth tried")
        user = authCse(request)
    if code == 'ece':
        user = authEce(request)
    if code == 'cce':
        user = authCce(request)
    if code == 'mec':
        user = authMMe(request)
    if user:
        app.roundNum+=1
        app.save()
        return Response({"Round updated to":app.roundNum})
    else:
        return Response({"auth error":"bad auth"})

@api_view(['POST'])
def schedule(request):
    app=application.objects.filter(id=request.data.get("id")).first()
    jb = job.objects.get(id=app.job.id)
    dept_id = jb.dept.id
    depart  = department.objects.get(id=dept_id)
    code = depart.code
    user=None
    if code == 'cse':
        print("auth tried")
        user = authCse(request)
    if code == 'ece':
        user = authEce(request)
    if code == 'cce':
        user = authCce(request)
    if code == 'mec':
        user = authMMe(request)
    if user:

        app.schedule = request.data.get("datetime")
        app.save()
        return Response({"Schedule Updated":request.data.get("datetime")})
    else:
        return Response({"auth error":"bad auth"})


@api_view(['GET'])
def getSchedule(request):
    app=application.objects.filter(id=request.data.get("id")).first()
    jb = job.objects.get(id=app.job.id)
    dept_id = jb.dept.id
    depart  = department.objects.get(id=dept_id)
    code = depart.code
    user=None
    if code == 'cse':
        print("auth tried")
        user = authCse(request)
    if code == 'ece':
        user = authEce(request)
    if code == 'cce':
        user = authCce(request)
    if code == 'mec':
        user = authMMe(request)
    if user:
        return Response({"schedule":app.schedule})
    else:
        return Response({"auth error":"bad auth"})

@api_view(['GET'])
def Fetch_Jobs(request):
    jobs = QuerySet(job)
    user = authCse(request)
    if user:
        jobs|=job.objects.filter(dept=department.objects.filter(code="cse").first())
    user=None
    user = authEce(request)
    if user:
        jobs|=job.objects.filter(dept=department.objects.filter(code="ece").first())
    user=None
    user = authCce(request)   
    if user:
        jobs|=job.objects.filter(dept=department.objects.filter(code="cce").first())
    user=None
    user = authMMe(request)
    if user:
        jobs|=job.objects.filter(dept=department.objects.filter(code="mec").first())
    user=None
    if len(jobs):
        return Response(JobSerializer(jobs,many=True).data)
    else:
        return Response({"auth error":"bad_auth"})
# made by - Aryan Gera 20UCS032

@api_view(['GET'])
def Fetch_applications(request):
    user = None
    id=request.query_params.get("id")
    jb = job.objects.filter(id=id).first()
    dept_id=jb.dept.id
    depart  = department.objects.get(id=dept_id)
    code = depart.code
    user=None
    if code == 'cse':
        print("auth tried")
        user = authCse(request)
    if code == 'ece':
        user = authEce(request)
    if code == 'cce':
        user = authCce(request)
    if code == 'mec':
        user = authMMe(request)
    if user:
        cand = application.objects.filter(job=jb)
        return Response(application_Serializer(cand,many=True).data)
    else:
        return Response({"auth error":"bad auth"})

@api_view(['GET'])
def Reject(request):
    app=application.objects.filter(id=request.data.get("id")).first()
    jb = job.objects.get(id=app.job.id)
    dept_id = jb.dept.id
    depart  = department.objects.get(id=dept_id)
    code = depart.code
    user=None
    if code == 'cse':
        print("auth tried")
        user = authCse(request)
    if code == 'ece':
        user = authEce(request)
    if code == 'cce':
        user = authCce(request)
    if code == 'mec':
        user = authMMe(request)
    if user:
        app.delete()
        return Response({"Succesful Action":"Application Deleted"})
    else:
        return Response({"auth error":"bad auth"},401)

@api_view(['POST'])
def add_dept(request):
    user = authDofa(request)
    ds = dept_Serializer(data=request.data)
    if user and ds.is_valid():
        ds.save()
        return Response(ds.data)
    else:
        if user:
            return Response(ds.errors,400)
        else:
            return Response({"dofa":"auth error no dofa found"},401)


@api_view(['POST'])
def add_spez(request):
    user = authDofa(request)
    ss = spez_Serializer(data=request.data)
    if user and ss.is_valid():
        ss.save()
        return Response(ss.data)
    else:
        if user:
            return Response(ss.errors,400)
        else:
            return Response({"dofa":"auth error no dofa found"},401)

@api_view(['POST'])
def send_mail(request):
    app=application.objects.filter(id=request.data.get("id")).first()
    jb = job.objects.get(id=app.job.id)
    dept_id = jb.dept.id
    depart  = department.objects.get(id=dept_id)
    code = depart.code
    user=None
    if code == 'cse':
        print("auth tried")
        user = authCse(request)
    if code == 'ece':
        user = authEce(request)
    if code == 'cce':
        user = authCce(request)
    if code == 'mec':
        user = authMMe(request)
    if user:
        dt = str(app.schedule.date()).strip().split("-")
        d=dt[0]
        m=dt[1]
        y=dt[2]
        date=d+"/"+m+"/"+y
        body="Dear "+app.name+",\nWe are glad to inform you that your application matches our requirements and we would like to know you better. Following are the details for the online meet session.\nDate - "+date+"\nTime - "+str(app.schedule.time())+"\nLink - Placeholder"
        send = app.user.email
        subject="Regarding your Job Application in LNMIIT"
        sendMail(body,send,subject=subject)
        return Response({"email":"send"})
    else:
        return Response({"auth":"error"},401)

@api_view(['POST'])
def addPost(request):
    user = authDofa(request)
    if user:
        ps = post_Serializer(data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.errors,400)
    else:
        return Response({"dofa":"auth error no dofa found"},401)
    
@api_view(['GET'])
def getPosts(request):
    user = authAdmin(request)
    if user:
        posts = post.objects.all()
        return Response(post_Serializer(posts, many=True).data)
    else:
        return Response({"autherror":"No Admin Found"})


