from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import JobSerializer,application_Serializer,UserLoginSerializer
from .models import job,User,application
@api_view(['GET'])
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
def register_Application(request):
    as = application_Serializer(data=re)
