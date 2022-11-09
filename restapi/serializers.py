from rest_framework import serializers

from restapi.models import job,department,User,application,spez

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
# made by - Aryan Gera 20UCS032

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=job
        fields='__all__'
# made by - Aryan Gera 20UCS032
# made by - Aryan Gera 20UCS032
# made by - Aryan Gera 20UCS032

class application_Serializer(serializers.ModelSerializer):
    class Meta:
        model = application
        fields='__all__'
class dept_Serializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields='__all__'
class spez_Serializer(serializers.ModelSerializer):
    class Meta:
        model = spez
        fields='__all__'