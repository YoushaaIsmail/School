from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from dj_rest_auth.views import LoginView
# from knox.auth import AuthToken
from .serializer import *
from .emails import *
from django.contrib.auth.hashers import make_password
from rest_framework import status

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                password = serializer.validated_data.get('password')
                serializer.validated_data['password'] = make_password(password)
                
                # Create the user
                user = serializer.save()
                
                # Create the parent
                parent_data = {
                    'account': user.pk

                }
                parent_serializer = parentSerializer(data=parent_data)
                if parent_serializer.is_valid():
                    parent_serializer.save()
                else:
                    # Delete the user if parent creation fails
                    user.delete()
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'Failed to create parent',
                        'data': parent_serializer.errors
                    })
                
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Registration successful. Check email for verification.',
                    'data': serializer.data
                })
            
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Something went wrong',
                'data': serializer.errors
            })
        
        except Exception as e:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Internal server error',
                'data': str(e)
            })
class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VeryfiAccountSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                
                try:
                    user = Account.objects.get(email=email)
                except Account.DoesNotExist:
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'Invalid Email',
                    })
                
                if user.otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'Wrong OTP',
                    })
                
                user.is_verified = True
                user.save()
                
                return Response({
                    'status': 200,
                    'message': 'Account Verified',
                    'data': {},
                })
                
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors,
            })
        
        except Exception as e:
            print(e)          

# @api_view(['POST'])
# def login_api(request):
#     serializer=AuthTokenSerializer(data = request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     _, token =AuthToken.objects.create(user)

#     return Response({
#         'token': token
#     })

from rest_framework import status

class NewloginView(LoginView):
    def get_response(self):
        response = super().get_response()

        if response.status_code == status.HTTP_200_OK:
            user = self.user
            if user.is_verified:
                token = response.data['key']
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Login successful',
                    'data': {
                        'key': token
                    }
                })
            else:
                return Response({
                    'status': status.HTTP_401_UNAUTHORIZED,
                    'message': 'User is not verified',
                    'data': None
                })

        return response
@api_view(['POST'])    
def forgetpassword(request):

        try:
            data = request.data
            serializer = forgetpasswordSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                user = Account.objects.filter(email=email).first()
                if user:
                    send_otp_via_email(serializer.data['email'])
                    return Response({
                        'status': 200,
                        'message': 'successfully check email',
                        'data': serializer.data,
                    })
                return Response({
                    'status': 400,
                    'message': 'something went wrong',
                    'data': serializer.errors
                })
            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
from rest_framework import status
@api_view(['POST'])  
def resetpassword(request):
    try:
        data = request.data
        serializer = resetpassowrdSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data['email']
            user = Account.objects.filter(email=email).first()
            if user:
                password = serializer.validated_data.get('password')
                user.set_password(password)
                user.save()
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Password reset successful',
                    'data': serializer.data,
                })
            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'User not found',
                    'data': None,
                })
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Validation error',
                'data': serializer.errors,
            })
    except Exception as e:
        print(e)
        return Response({
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': 'Internal server error',
            'data': str(e),
        })