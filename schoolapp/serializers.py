from rest_framework import serializers
from .models import *
import base64
from Account.models import Account

class orderjoinSreializes(serializers.ModelSerializer):
    class Meta:
        model=order_join
        fields = ['His_level','StudentBirthday','Studentgender','StudentName','parentjoin','Schooljoin','state','Img1','Img2','Img3','Img4']
class locationSreializes(serializers.ModelSerializer):
    class Meta:
        model=location
        fields = '__all__'
class adsSreializes(serializers.ModelSerializer):
    class Meta:
        model=Ads

        fields = '__all__'

class acounntsSreializes(serializers.ModelSerializer):
    class Meta:
        model=Account

        fields = ['username','photo','last_name','first_name']

class teacherSreializes(serializers.ModelSerializer):
    account=serializers.SerializerMethodField('get_account')
    def get_account(self,obj):
        if obj:
            ser=acounntsSreializes(obj.account,many=False)
            return ser.data
        return None
    class Meta:
        model = Teacher
        fields = '__all__'
class excoursesSreializes(serializers.ModelSerializer):
    Teacher_ID=serializers.SerializerMethodField("get_te")
    def get_te(self, obj):
        if obj:
            
            ser=teacherSreializes(obj.Teacher_ID,many=False)
            return ser.data
        return None 
    class Meta:
        model=ExCourses

        fields = '__all__'
class InstSreializes(serializers.ModelSerializer):
    class Meta:
        model = Installment1
        fields = '__all__'        
class albomSerializ(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=['photo1','photo2','photo3','photo4','photo5','photo6']
class RatingReviewSchoolSreializes(serializers.ModelSerializer):
    parent=serializers.SerializerMethodField('get_account')
    def get_account(self,obj):
        if obj:
            ser=acounntsSreializes(obj.parent.account,many=False)
            return ser.data
        return None
    class Meta:
        model = RatingReviewSchool
        fields = '__all__' 

class SchoolSreializes(serializers.ModelSerializer):
    # image1_data = serializers.SerializerMethodField("get_image_data")
    # image2_data = serializers.SerializerMethodField("get_image_data2")
    # image3_data = serializers.SerializerMethodField("get_image_data3")
    # image4_data = serializers.SerializerMethodField("get_image_data4")

    reviews=serializers.SerializerMethodField("get_reviews")
    tes=serializers.SerializerMethodField("get_te")
    Location=serializers.SerializerMethodField("get_location")
    instment=serializers.SerializerMethodField("get_In")
    albom1=serializers.SerializerMethodField("get_albom")
    seatsNumber=serializers.SerializerMethodField("get_seatsNumber")
    
    def get_location(self, obj):
        if obj:
            
            ser=locationSreializes(obj.Location,many=False)
            return ser.data
        return None 
    
    def get_seatsNumber(self,obj):
        if obj:
            seatsNumber=[]
            allnumber1=0
            Classlevel1=Class.objects.filter(level=1).all()
            Classlevel1=Classlevel1.filter(school=obj)
            allStudent1=0
            for i in Classlevel1:
                
                Studentlevel1=Student.objects.filter(hisclass=i).count()
                print(Studentlevel1)
                allStudent1=allStudent1+Studentlevel1
                allnumber1=allnumber1+i.number
            level1=allnumber1-allStudent1
            allnumber2=0
            Classlevel2=Class.objects.filter(level=2).all()
            Classlevel2=Classlevel2.filter(school=obj)
            allStudent2=0
            for i in Classlevel2:
                Studentlevel2=Student.objects.filter(hisclass=i).count()
                allStudent2=allStudent2+Studentlevel2
                allnumber2=allnumber2+i.number
            level2=allnumber2-allStudent2
            allnumber3=0
            Classlevel3=Class.objects.filter(level=3).all()
            Classlevel3=Classlevel3.filter(school=obj)
            allStudent3=0
            for i in Classlevel3:
                Studentlevel3=Student.objects.filter(hisclass=i).count()
                allStudent3=allStudent3+Studentlevel3
                allnumber3=allnumber3+i.number
            level3=allnumber3-allStudent3
            allnumber4=0
            Classlevel4=Class.objects.filter(level=4).all()
            Classlevel4=Classlevel4.filter(school=obj)
            allStudent4=0
            for i in Classlevel4:
                Studentlevel4=Student.objects.filter(hisclass=i).count()
                allStudent4=allStudent4+Studentlevel4
                allnumber4=allnumber4+i.number
            level4=allnumber4-allStudent4
            allnumber5=0
            Classlevel5=Class.objects.filter(level=5).all()
            Classlevel5=Classlevel5.filter(school=obj)
            allStudent5=0
            for i in Classlevel5:
                Studentlevel5=Student.objects.filter(hisclass=i).count()
                allStudent5=allStudent5+Studentlevel5
                allnumber5=allnumber5+i.number
            level5=allnumber5-allStudent5
            allnumber6=0
            Classlevel6=Class.objects.filter(level=6).all()
            Classlevel6=Classlevel6.filter(school=obj)
            allStudent6=0
            for i in Classlevel6:
                Studentlevel6=Student.objects.filter(hisclass=i).count()
                allStudent6=allStudent6+Studentlevel6
                allnumber6=allnumber6+i.number
            level6=allnumber6-allStudent6
            seatsNumber.append({
                'level1':level1,
                'level2':level2,
                'level3':level3,
                'level4':level4,
                'level5':level5,
                'level6':level6,
            })
            return seatsNumber
        return None    
    
    def get_reviews(self, obj):
        if obj:
            ht=RatingReviewSchool.objects.filter(school=obj)
            ser=RatingReviewSchoolSreializes(ht,many=True)
            return ser.data
        return None    


    
    def get_albom(self, obj):
        if obj:
            ht=School.objects.filter(id=obj.id)
            ser=albomSerializ(ht,many=True)
            return ser.data
        return None
    

    def get_In(self, obj):
        if obj:
            ht=Installment1.objects.filter(school=obj)
            ser=InstSreializes(ht,many=True)
            return ser.data
        return None    
    
    def get_te(self, obj):
        if obj:
            ht=Teacher.objects.filter(school=obj)
            ser=teacherSreializes(ht,many=True)
            return ser.data
        return None 
    def get_Albome(self, obj):
        image_all=[]
        if obj.photo1:
            with open(obj.photo1.path, 'rb') as loaded_file:
                 image_data = loaded_file.read()
                 encoded_image1 = base64.b64encode(image_data).decode('utf-8')

        if obj.photo2:
            with open(obj.photo2.path, 'rb') as loaded_file:
                 image_data = loaded_file.read()
                 encoded_image2 = base64.b64encode(image_data).decode('utf-8')
                       
        if obj.photo3:
            with open(obj.photo3.path, 'rb') as loaded_file:
                 image_data = loaded_file.read()
                 encoded_image3 = base64.b64encode(image_data).decode('utf-8')
                  
        if obj.photo4:
            with open(obj.photo4.path, 'rb') as loaded_file:
                 image_data = loaded_file.read()
                 encoded_image4 = base64.b64encode(image_data).decode('utf-8') 
              
        if obj.photo5:
            with open(obj.photo5.path, 'rb') as loaded_file:
                 image_data = loaded_file.read()
                 encoded_image5 = base64.b64encode(image_data).decode('utf-8')  
              
        if obj.photo6:
            with open(obj.photo6.path, 'rb') as loaded_file:
                 image_data = loaded_file.read()
                 encoded_imag6 = base64.b64encode(image_data).decode('utf-8')                                                                    
        image_all.append({
        'img1':obj.photo6,
        'img2':encoded_image2,
        'img3':encoded_image3,
        'img4':encoded_image4,
        'img5':encoded_image5,    
        'img6':encoded_imag6})    

        return image_all
    def get_image_data(self, obj):
        if obj.photo1:
            with open(obj.photo1.path, 'rb') as loaded_file:
                image_data = loaded_file.read()
                encoded_image = base64.b64encode(image_data).decode('utf-8')
                return encoded_image
        return None  
    def get_image_data2(self, obj):
        if obj.photo2:
            with open(obj.photo2.path, 'rb') as loaded_file:
                image_data = loaded_file.read()
                encoded_image = base64.b64encode(image_data).decode('utf-8')
                return encoded_image
        return None     
    def get_image_data3(self, obj):
        if obj.photo3:
            with open(obj.photo3.path, 'rb') as loaded_file:
                image_data = loaded_file.read()
                encoded_image = base64.b64encode(image_data).decode('utf-8')
                return encoded_image
        return None     
    def get_image_data4(self, obj):
        if obj.photo4:
            with open(obj.photo4.path, 'rb') as loaded_file:
                image_data = loaded_file.read()
                encoded_image = base64.b64encode(image_data).decode('utf-8')
                return encoded_image
        return None
    class Meta:
        model=School
        fields='__all__'

