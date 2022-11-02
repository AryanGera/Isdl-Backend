from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer
from .models import job,User,application
@api_view(['POST'])
def create_job(request):
    js = JobSerializer(data=request.data)
    if js.is_valid():
        js.save()
        return Response(js.data)
    else:
        return Response({"bad":"response"})
    qs = list(job.objects.all())
    jsall = JobSerializer(qs,many=True)
    return Response(jsall.data)

@api_view(['POST'])
def register_Application(request):
    ass = application_Serializer(data=request.data)
    email = request.data.get("email")
    password = request.data.get("password")

    if ass.is_valid():
        ass.save()
    else:
        return Response({"bad":"response"})
    return Response({"user":"registered"})

# @api_view(['POST'])
# def get_application(request):
    