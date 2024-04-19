from django.contrib import admin
from .models import School ,Class,Teacher,Student,Supervisor,Course,Employee,StudentINCourse,Homework,CourseDate,mark,order_join,Order_meeting,Activites,Notifications,Installment1
from .models import ExCourses,RatingReviewSchool,adminSchool,Ads,News,location

# Register your models here.
admin.site.register(School)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Course)
admin.site.register(Employee)
admin.site.register(StudentINCourse)
admin.site.register(CourseDate)
admin.site.register(Homework)
admin.site.register(Notifications)
admin.site.register(Activites)
admin.site.register(Order_meeting)
admin.site.register(order_join)
admin.site.register(mark)
admin.site.register(ExCourses)
admin.site.register(RatingReviewSchool)
admin.site.register(Installment1)
admin.site.register(adminSchool)
admin.site.register(Ads)
admin.site.register(News)
admin.site.register(location)