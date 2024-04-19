from rest_framework import serializers
from .models import Account,Parent
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.views import UserDetailsView
from django.contrib.auth import authenticate,get_user_model

UserModel=get_user_model()
class parentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['account']
class NewUserDetailsView(UserDetailsView):
    class Meta:
        model= Account
        fields = ['username','email','last_name','first_name','pk']




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username','email' ,'password' , 'is_verified']


class VeryfiAccountSerializer(serializers.Serializer):
    email =serializers.EmailField()
    otp= serializers.CharField()

class NewLoginSerializer(LoginSerializer):
    pass

class forgetpasswordSerializer(serializers.Serializer):
    email =serializers.EmailField()

class resetpassowrdSerializer(serializers.Serializer):
    email =serializers.EmailField()
    password= serializers.CharField()
