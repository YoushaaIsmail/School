from .models import School

def get_hostname(request):
    return request.get_host().split(':')[0].lower()

def get_School(request):
    hostname= get_hostname(request)
    name1=hostname.split('.')[0] 
    return School.objects.filter(name=name1).first()   