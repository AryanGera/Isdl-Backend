from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer
from .models import job,User,application,spez
from .views import register,authuser,registerM

@api_view(['POST'])
def register_Application(request):
    ass = application_Serializer(data=request.data)
    registerM(request)
    email = request.data.get("email")
    user = User.objects.filter(email=email).first()
    jb = job.objects.get(id=request.data.get("job"))
    
    req_spez = jb.spez_Req
    inSpez = spez.objects.get(id=request.data.get("spez"))
    print(inSpez)
    valid = True
    if jb.phd_Req and int(request.data.get("qualifications"))!=7:
        print("yep1")
        valid =False
    if float(jb.cgpa_Req)>float(request.data.get("cgpa")):
        print("yep2")
        valid=False
    if req_spez !=inSpez:
        print("1")
        valid=False
    if ass.is_valid() and valid:
        obj = ass.save()
    else:
        user.delete()
        return Response({"bad":"response"})
    if user:
        obj.user = user

    else:
        return Response({"user":"not found"})
    # obj.spez_Req=spez
    jb = job.objects.filter(id=request.data.get("job")).first()
    obj.job = jb
    hs = hireability_score(request)
    obj.hireScore = hs
    obj.save()
    return Response({"user":"registered"})

def hireability_score(request):
    cit = float(request.data.get("citations"))
    pub= float(request.data.get("publications"))
    exp= float(request.data.get("experiance"))
    cpi= float(request.data.get("cgpa"))
    normCit = cit/50
    normPub = pub/20
    normExp = exp/15
    normCpi = cpi/10
    avg = (normCpi+normPub+normCit+normExp)/4
    score = avg*10
    return score

@api_view(['GET'])
def get_details(request):
    user = authuser(request)

    if user:
        app = application.objects.filter(user=user.data.get("id")).first()
        return Response(application_Serializer(app).data)
    else:
        return Response({"bad":"auth"})

@api_view(['POST'])
def update_Application(request):
    user=authuser(request)
    if user:
        ass = application_Serializer(data=request.data)
        # obj = application.objects.filter(id=ass.id)
        # obj.postal=ass.data.get('postal')
        # obj.city=ass.data.get('city')
        # obj.pincode=ass.data.get('pincode')
        # obj.mob_num=ass.data.get('mob_num')
        # obj.state=ass.data.get('state')
        if ass.is_valid():
            obj = ass.save()
        else:
            return Response({"bad":"response"})
    else:
        return Response({"bad":"auth"})
    # user.application = obj
    # obj.spez_Req=spez
    # jb = job.objects.filter(id=request.data.get("job_id"))
    # obj.job = jb
    # hs = hireability_score(request)
    # obj.hireScore = hs
    # return Response({"user":"registered"})
# @api_view(['POST'])
# def get_application(request):
    
# @api_view(['POST'])
# def update_Application(request):
@api_view(['POST'])
def delete_app(request):
    user = authuser(request)
    if(user):
        application.objects.filter(user=user).delete()
        Response({"deleted":"yep"})
    else:
        Response({"bad":"auth"})


    
    
    