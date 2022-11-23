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

        return Response({"error":"cannot fill application for same job twice"},400)
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
            return Response({"error":"does not fulfil requirments"},400)
        return Response({"error":str(ass.errors)},400)
    if user:
        obj.user = user
    else:
        return Response({"error":"User Authorization Failure"},401)
    
    jb = job.objects.filter(id=request.data.get("job")).first()
    obj.job = jb
    hs = hireability_score(request)
    obj.hireScore = round(hs,2)
    
    try:
        obj.save()
    except ValidationError as e:
        obj.delete()
        return Response({"error":str(e)})
    return Response({"success":"user registered"})

def hireability_score(request):
    cit = float(request.data.get("citations"))
    pub= float(request.data.get("publications"))
    exp= float(request.data.get("experiance"))
    cpi= float(request.data.get("cgpa"))
    normCit = cit/200
    normCit*=1
    normPub = pub/50
    normPub *=3
    normExp = exp/30
    normExp*=5
    normCpi = cpi/10
    normCpi *=5
    avg = (normCpi+normPub+normCit+normExp)/14
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
        return Response({"error":"User Authorization Failure"},401)


@api_view(['POST'])
def update_Application(request):
    user=authuser(request)
    apps = application.objects.filter(user=user.id)
    if user and apps:
        dt = request.data
        apps.update(
            experiance=dt.get("experiance"),
            citations=dt.get("citations"),
            publications = dt.get("publications"),
            country =dt.get("country"), 
            city = dt.get("city"),
            state = dt.get("state"),
            district = dt.get("district"),
            postal =dt.get("postal"),
            pincode = dt.get("pincode"),
            mob_num =dt.get("mob_num"),
            hireScore=hireability_score(request)
        )
        return Response({"success":"application updated"})
    else:
        return Response({"error":"User Authorization Failure"},401)


@api_view(['POST'])
def delete_app(request):
    user = authuser(request)
    if(user):
        application.objects.filter(user=user.id).delete()
        return Response({"success":"application deleted"})
    else:
        return Response({"error":"User Authorization Failure"},401)
