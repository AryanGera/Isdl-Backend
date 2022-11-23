from rest_framework.response import Response

from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer
from .models import job,User,application,spez
from .views import register,authuser,registerM
from rest_framework import serializers
from django.core.exceptions import ValidationError

from django.db import models


@api_view(['POST'])
def register_Application(request):
    ass = application_Serializer(data=request.data)
    email = request.data.get("email")
    user = User.objects.filter(email=email).first()
    if user==None:
        registerM(request)
        user = User.objects.filter(email=email).first()
    ass_data = ass.initial_data
    ass_data['user'] = user.id
    ass.initial_data=ass_data
    jb = job.objects.get(id=request.data.get("job"))
    ap = application.objects.filter(job=jb.id,user=user.id).first()
    if ap:

        return Response({"bad input":"cannot fill application for same job twice"},400)
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
    if ass.is_valid() and valid :
        obj = ass.save()
    else:
        if valid==False:
            return Response({"condition":"does not fulfil requirments"},400)
        return Response(ass.errors,400)
    if user:
        obj.user = user
    else:
        return Response({"user":"not found"})
    # obj.spez_Req=spez
    jb = job.objects.filter(id=request.data.get("job")).first()
    obj.job = jb
    hs = hireability_score(request)
    obj.hireScore = round(hs,2)
    # os = application_Serializer(obj)
    try:
        obj.save()
    except ValidationError as e:
        obj.delete()
        return Response(e)
    return Response({"user":"registered"})

def hireability_score(request):
    cit = float(request.data.get("citations"))
    pub= float(request.data.get("publications"))
    exp= float(request.data.get("experiance"))
    cpi= float(request.data.get("cgpa"))
    normCit = cit/200
    normCit*=4
    normPub = pub/50
    normPub *=2
    normExp = exp/30
    normCpi = cpi/10
    avg = (normCpi+normPub+normCit+normExp)/8
    score = avg*10
    return score

@api_view(['GET'])
def get_details(request):
    user = authuser(request)
    if user:
        app = application.objects.filter(user=user.id)
        jb=job.objects.all()
        return Response(application_Serializer(app,many=True).data)
    else:
        return Response({"bad":"auth"})

#if anything breaks check this first
@api_view(['POST'])
def update_Application(request):
    user=authuser(request)
    apps = application.objects.filter(user=user.data.get("id"))
    if user and apps:
        for ap in apps:
            dt = request.data
            ap.update(
                experiance=dt.get("experiance")if (dt.get("experiance")) else ap.experiance,
                citations=dt.get("citations")if (dt.get("citations")) else ap.citations,
                publications = dt.get("publications")if (dt.get("publications")) else ap.publications,
                country =dt.get("country")if (dt.get("country")) else ap.country, 
                city = dt.get("city")if (dt.get("city")) else ap.city,
                state = dt.get("state")if (dt.get("state")) else ap.state,
                district = dt.get("district")if (dt.get("district")) else ap.district,
                postal =dt.get("postal")if (dt.get("postal")) else ap.postal,
                pincode = dt.get("pincode")if (dt.get("pincode")) else ap.pincode,
                mob_num =dt.get("mob_num")if (dt.get("mob_num")) else ap.mob_num,
            )
            return Response({"done":"done"})
    else:
        return Response({"bad":"auth"})


@api_view(['POST'])
def delete_app(request):
    user = authuser(request)
    if(user):
        application.objects.filter(user=user.data.get("id")).delete()
        return Response({"deleted":"yep"})
    else:
        return Response({"bad":"auth"})


    
    
    