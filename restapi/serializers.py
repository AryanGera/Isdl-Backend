from rest_framework import serializers
from restapi.models import User
from restapi.models import application
from restapi.models import job

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','name']
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

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=job
        fields=['dept_name','post']

class application_Serializer(serializers.ModelSerializer):
    class Meta:
        model = application
        fields='__all__'