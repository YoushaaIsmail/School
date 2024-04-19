"""
URL configuration for School project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from schoolapp.views import our_School
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import UserDetailsView
from Account.views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('our_School',our_School,name='our_School'),
    path('auth/', include('dj_rest_auth.urls')),
    path('registration/',include('dj_rest_auth.registration.urls')),
    path('profile/', include('allauth.urls')),
    path('register/',RegisterAPI.as_view()),
    path('verify/',VerifyOTP.as_view()),
    path('Newlogin/',NewloginView.as_view(),name='login'),
    path('SchoolApp/',include('schoolapp.url')),
    path('forgetpassword/',forgetpassword,name='forgetpassword'),
        path('resetpassord/',resetpassword,name='resetpassword'),
    
    ]
