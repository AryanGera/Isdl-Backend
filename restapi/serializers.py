
from dataclasses import fields
from rest_framework import serializers
from restapi.models import User
from restapi.models import applicant
from restapi.models import job_App


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password!=None:
            instance.set_password(password)
        instance.save()
        return instance
class ApplicantSerializer(serializers.Serializer):
    class Meta:
        model=applicant
        fields='__all__'
class ApplicantSerializer(serializers.Serializer):
    class Meta:
        model=applicant
        fields='__all__'
class JobSerializer(serializers.Serializer):
    class Meta:
        model=job_App
        fields='__all__'
