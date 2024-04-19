
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('our_School',our_School,name='our_School'),
    path('Schools',School_list,name='School_list'),
    path('Schools/filter',getfilterSchool,name='School_filter'),
    path('login/', AdminSchoolLoginView.as_view(), name='admin_login'),
    path('Schools/<int:pk>/Semester',getallExCourses,name='getallExCourses'),
    path('createjoinorder',createjoinorder,name='createjoinorder'),
    path('ads',getallads,name='ads'),
        
    ]
