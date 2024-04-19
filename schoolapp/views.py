from django.shortcuts import render,redirect
from .models import *
from .utilities import get_School
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.db.models import Q
from .form import *
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
def our_School(request):
    school1=get_School(request)
    # students=Student.objects.filter(school=school1)
    class1=Class.objects.filter(school=school1)

    return render(request ,'our_School.html',{'school':school1,'class':class1})

class AdminSchoolLoginView(auth_views.LoginView):
    template_name = 'login.html'  # Replace with your login template path
    success_url = reverse_lazy('our_School')  # Replace with the desired success URL
    
    def get_success_url(self):
        user = self.request.user
        print(user.identity)
        if user.identity=='admin':
            admin=adminSchool.objects.filter(account=user).first()
            print(admin.school)
            print(get_School(self.request))
           
            

            if admin.school == get_School(self.request):
                # User is an adminSchool associated with the correct school
                print('t')
                return reverse_lazy('our_School')  # Replace with the desired URL
        return super().get_success_url()



# @api_view(['GET'])
# def School_list(request):
#     schools = School.objects.all()
#     school_data = []
    
#     for school in schools:
#        # offer_data = {
#         #    'offer_id': car.offer.id,
#          #   'offer_subject': car.offer.Subject,
#           #  'offer_Description':car.offer.Description,
#          #   'offer_start_price':car.offer.start_price,
#          #   'offer_start_date':car.offer.start_date,
#          #   'offer_FA_user':car.offer.FA_user.username,
#         #}
        
#         school_data.append({
#             'car_id': school.id,
#             'name': school.name,
#             'description': school.Des,
#             'type': car.type,
#             'color': car.color,
#             'company': car.company,
#             'kind': car.kind,
#             'years': car.years,
#             #'offer': offer_data,
#             'offer_id': car.offer.id,
#             'offer_subject': car.offer.Subject,
#             'offer_Description':car.offer.Description,
#             'offer_start_price':car.offer.start_price,
#             'offer_start_date':car.offer.start_date,
#             'offer_FA_user':car.offer.FA_user.username,

#         })
    
#     return Response(car_data)

# @api_view(['GET'])
# def School_list(request):

#     Schools = School.objects.all()
    
#     #data={'Results':list(Cars.values('pk','A_door','Hours_power','type','color','company','kind','years','Foffer_ID'))}
#     school_data = []
    
#     for Schoollist in Schools:
#         Serializer=SchoolSreializes(Schoollist)
#         teacherhis =  Teacher.objects.filter(school=Schoollist)
#         Sreializes1=teacherSreializes(teacherhis,many=True)
#         Serializer.data.append({'teachers': Sreializes1.data })
#         print(Sreializes1.data)
#         school_data.append({
#             'school': Serializer.data,  # Serialized school data
#             'teachers': Sreializes1.data  # Serialized teachers data for this school
#         })
    
#     return Response(Serializer.data)
 

@api_view(['GET'])
def School_list(request):

    Schools = School.objects.all()
    Serializer=SchoolSreializes(Schools,many=True)
    #data={'Results':list(Cars.values('pk','A_door','Hours_power','type','color','company','kind','years','Foffer_ID'))}
    
    
    return Response(Serializer.data)

@api_view(['GET'])
def getfilterSchool(request):
    level= request.GET.get('level')
    type = request.GET.get('type')
    max_price = request.GET.get('max_price')
    min_price= request.GET.get('min_price')
    level=int(level)
    query = Q()
    
    if max_price and min_price and level:
        Insta1=Installment1.objects.all()
        


        all_School=[]

        if level==1:
            for i in Insta1:
                price=i.level1
                if price >= int(min_price) and price <= int(max_price):

                    
                    school1=i.school
                    if type:
                        if school1.EType==type:

                         all_School.append(school1)
                    else:
                        all_School.append(school1)

                   

        if level==2:
            for i in Insta1:
                price=i.level2
                if price >= int(min_price) and price <= int(max_price):
                    school1=i.school
                    if type:
                        if school1.EType==type:

                         all_School.append(school1)
                    else:
                        all_School.append(school1)

        if level==3:
            for i in Insta1:
                price=i.level3
                if price >= int(min_price) and price <= int(max_price):
                    school1=i.school
                    if type:
                        if school1.EType==type:

                         all_School.append(school1)
                    else:
                        all_School.append(school1)
        if level==4:
            for i in Insta1:
                price=i.level4
                if price >= int(min_price) and price <= int(max_price):
                    school1=i.school
                    if type:
                        if school1.EType==type:

                         all_School.append(school1)
                    else:
                        all_School.append(school1)
        if level==5:
            for i in Insta1:
                price=i.level5
                if price >= int(min_price) and price <= int(max_price):
                    school1=i.school
                    if type:
                        if school1.EType==type:

                         all_School.append(school1)
                    else:
                        all_School.append(school1)
        if level==6:
            for i in Insta1:
                price=i.level6
                if price >= int(min_price) and price <= int(max_price):
                    school1=i.school
                    if type:
                        if school1.EType==type:

                         all_School.append(school1)
                    else:
                        all_School.append(school1)
    print(all_School) 
    serializer = SchoolSreializes(all_School, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getallExCourses(request,pk):
    sch=School.objects.get(id=pk)
    exourse=ExCourses.objects.filter(school=sch)
    serializer = excoursesSreializes(exourse, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getallads(request):
    ads=Ads.objects.all()
    serializer = adsSreializes(ads, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def getfilterSchool(request):
#     level = request.GET.get('level')
#     school_type = request.GET.get('type')
#     max_price = request.GET.get('max_price')
#     min_price = request.GET.get('min_price')

#     queryset = School.objects.all()

#     if level:
#         # Perform filtering based on the specified level
#         level_field = f'level{level}'
#         level_filter = {f'installment__{level_field}__exact': float(level)}
#         queryset = queryset.filter(**level_filter)

#     if school_type:
#         # Perform filtering based on the school type
#         queryset = queryset.filter(EType=school_type)

#     if max_price:
#         # Perform filtering based on the maximum price
#         max_price_filter = {f'installment__{level_field}__lte': float(max_price)}
#         queryset = queryset.filter(**max_price_filter)

#     if min_price:
#         # Perform filtering based on the minimum price
#         min_price_filter = {f'installment__{level_field}__gte': float(min_price)}
#         queryset = queryset.filter(**min_price_filter)

#     serializer = SchoolSreializes(queryset, many=True)
#     return Response(serializer.data)
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# def school_admin_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None and user.account.identity == 'school_admin':
#             login(request, user)
#             return redirect('school_admin_dashboard')  # Redirect to the dashboard page for SchoolAdmin
#         else:
#             messages.error(request, 'Invalid login credentials')
    
#     return render(request, 'login.html'
@api_view(['POST'])
def createjoinorder(request):
        try:
            data = request.data
            data['state']='waiting'
            serializer = orderjoinSreializes(data = data)
            if serializer.is_valid():
                print('t')
                serializer.save()
                return Response(serializer.data)
            return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data':serializer.errors

            })

                  
        except Exception as e:
            print(e)
