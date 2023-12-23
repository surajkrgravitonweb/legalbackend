from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate



#creating serializers.


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email", "username","first_name","password" , "role", "phone_number", ]

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
      
            phone_number=validated_data['phone_number'],
          
            # role=validated_data['role'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
         
            validation = {
                'email': user.email,
                "password": user.password,
                'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")

from rest_framework import serializers
from .models import *

class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = '__all__'

class UserFormDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFormDocument
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'



class AllPagesApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllPagesApi
        fields = '__all__'

class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOutput
        fields = '__all__'


class AllPAgesByAgentControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllPAgesByAgentControl
        fields = '__all__'