from django.db import models
from Account.models import Parent,Account
from django.contrib.auth.models import User,AbstractUser
from django_resized import ResizedImageField
import os
from django.contrib.auth.hashers import make_password,check_password
def upload_to(inst,filename):
      base_path="profile"
      safe_filename=str(filename)
      final_path=os.path.join(base_path,safe_filename)
      return final_path

class School(models.Model):
   
   listt8=(
       ('multiple languages', 'multiple languages'),
       ('multinational', 'multinational'),
       ('geneal education', 'geneal education'),
      ('islamic education', 'islamic education'),
      ('christian educations','christian educations'),
      )
  
   photo1=ResizedImageField(upload_to=upload_to,null=True,blank=True)
   photo2=ResizedImageField(upload_to=upload_to,null=True,blank=True)
   photo3=ResizedImageField(upload_to=upload_to,null=True,blank=True)
   photo4=ResizedImageField(upload_to=upload_to,null=True,blank=True)
   photo5=ResizedImageField(upload_to=upload_to,null=True,blank=True)
   photo6=ResizedImageField(upload_to=upload_to,null=True,blank=True)
   name =models.CharField(max_length=100, unique=True)
   Location=models.OneToOneField("location", on_delete=models.CASCADE,related_name='His_location')
   Rating=models.FloatField()

   Des=models.CharField(max_length=1000)

   EType =models.CharField(max_length=200,choices=listt8)

class location(models.Model):
     x=models.FloatField()
     y=models.FloatField()
class Installment1(models.Model):
    level1=models.FloatField()
    level2=models.FloatField()
    level3=models.FloatField()
    level4=models.FloatField()
    level5=models.FloatField()
    level6=models.FloatField()
    school=models.OneToOneField("School", on_delete=models.CASCADE,related_name='His_Installment')


class SchoolAwareModel(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE)

class Class(SchoolAwareModel):
    level=models.FloatField()
    number=models.FloatField()

class Teacher(SchoolAwareModel):
        account=models.OneToOneField(Account,on_delete=models.CASCADE,
            related_name='teacher', null=True, blank=True)
        Competence=models.CharField(max_length=50)

class Supervisor(SchoolAwareModel):
            account=models.OneToOneField(Account,on_delete=models.CASCADE,
            related_name='supervisor', null=True, blank=True)

class Employee(SchoolAwareModel):
            account=models.OneToOneField(Account,on_delete=models.CASCADE,
            related_name='employee', null=True, blank=True)   

class Student(models.Model):
    list1=(
       ('girl', 'girl'),
       ('boy', 'boy'),

      )
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Birthday=models.DateTimeField()
    photo=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    hisparent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    hisclass=models.ForeignKey(Class,on_delete=models.CASCADE)
    supervisor=models.ForeignKey(Supervisor,on_delete=models.CASCADE)
    gender=models.CharField(max_length=200,choices=list1)

class Course(models.Model):
    name=models.CharField(max_length=30)
    Time_Quiz=models.DateTimeField()
    Time_final=models.DateTimeField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    hisclass=models.ForeignKey(Class,on_delete=models.CASCADE)

class CourseDate(models.Model):
    listt1=(
       ('friday', 'Friday'),
       ('saturday', 'Saturday'),
       ('sunday', 'Sunday'),
      ('monday', 'Monday'),
      ('tuesday','Tuesday'),
      ('wednesday','Wednesday'),
      ('thursday','Thursday')
)
    Day=models.CharField(max_length=15,choices=listt1)
    time=models.TimeField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

class Homework(models.Model):
    Des=models.CharField(max_length=150)
    Course_ID=models.ForeignKey(Course,on_delete=models.CASCADE)
    Teacher_ID=models.ForeignKey(Teacher,on_delete=models.CASCADE)

class StudentINCourse(models.Model):
    state=models.BooleanField(default=True)
    Date=models.DateTimeField()
    Student_ID=models.ForeignKey(Student,on_delete=models.CASCADE)
    Course_ID=models.ForeignKey(Course,on_delete=models.CASCADE)

class mark(models.Model):
    mark_Quiz=models.FloatField()
    mark_final=models.FloatField()
    mark_Works=models.FloatField()
    student_Mark=models.ForeignKey(Student,on_delete=models.CASCADE) 
    course_Mark=models.ForeignKey(Course,on_delete=models.CASCADE)    

class Order_meeting(models.Model):
    listt2=(
       ('acceptable', 'Acceptable'),
       ('rejected', 'Rejected'),
       ('waiting', 'Waiting')

)
    state=models.CharField(max_length=15,choices=listt2)
    Date=models.DateTimeField()

class order_join(models.Model):
    listt3=(
       ('acceptable', 'Acceptable'),
       ('rejected', 'Rejected'),
       ('waiting', 'Waiting')

)              
    listt4=(
       ('first', 'First'),
       ('second', 'Second'),
       ('third', 'Third'),
       ('third', 'Third'),
        ('fourth', 'Fourth'),
        ('fifth', 'Fifth'),
        ('sixth', 'Sixth')


) 
    list1=(
       ('girl', 'girl'),
       ('boy', 'boy'),

      )
    state=models.CharField(max_length=15,choices=listt3)
    StudentName=models.CharField(max_length=50)
    Studentgender=models.CharField(max_length=200,choices=list1)
    StudentBirthday=models.DateTimeField()
    His_level=models.CharField(max_length=15,choices=listt4)
    Is_pay=models.BooleanField(default=False)
    Img1=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    Img2=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    Img3=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    Img4=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    parentjoin=models.ForeignKey(Parent,on_delete=models.CASCADE)    
    Schooljoin=models.ForeignKey(School,on_delete=models.CASCADE)
    
class Activites(models.Model):
    listt5=(
       ('healthy', 'Healthy'),
       ('sport', 'Sport'),
       ('intellectual', 'Intellectual'),
       ('general', 'General')


) 
    Type=models.CharField(max_length=15,choices=listt5)
    level=models.CharField(max_length=15)
    Des=models.CharField(max_length=100)
    Student_active=models.ForeignKey(Student,on_delete=models.CASCADE)
    
class Notifications(SchoolAwareModel):
    Des=models.CharField(max_length=100)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    
class RatingReviewSchool(models.Model):
        
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    scoure=models.FloatField()
    Des=models.CharField(max_length=1000)


                
class ExCourses(SchoolAwareModel):
     name=models.CharField(max_length=100)
     type=models.CharField(max_length=100)
     Stime=models.TimeField()
     Etime=models.TimeField()
     Sdate=models.DateField()
     Edate=models.DateField()
     SAge=models.PositiveIntegerField()
     EAge=models.PositiveBigIntegerField()
     price=models.FloatField()
     Des=models.CharField(max_length=1000)
     Teacher_ID=models.ForeignKey(Teacher,on_delete=models.CASCADE)

class chating(models.Model):
        
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    
    Des=models.CharField(max_length=1000)
    
class adminSchool(SchoolAwareModel):
        account=models.OneToOneField(Account,on_delete=models.CASCADE,
            related_name='admin', null=True, blank=True)

class News(SchoolAwareModel):
     Des=models.CharField(max_length=1000)

class Ads(models.Model):
    img=ResizedImageField(upload_to=upload_to,null=True,blank=True)
    Des=models.CharField(max_length=1000)
    link=models.CharField(max_length=100)
    locationName=models.CharField(max_length=300)
    price=models.FloatField()
    discount=models.FloatField()
     

              