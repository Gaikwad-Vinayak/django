from datetime import datetime
from django.shortcuts import render
from .models import student
from django.db.models import Aggregate,Avg,Max,Min,Sum,StdDev,Variance
# Create your views here.
def home(request):
    #dic=student.objects.get(pk=8)
    #dic=student.objects.first()
    #dic=student.objects.last()
    #dic=student.objects.latest('pass_date')
    #dic=student.objects.earliest('pass_date')
    #dic=student.objects.create(name='popat',roll=108,city='nimgaon',marks=99,pass_date='2020-1-1')
    #dic=student.objects.update(name='popat',roll=108,city='nimgaon',marks=10,pass_date='2020-1-1')
    #dic=student.objects.delete(name='popat',roll=108,city='nimgaon',marks=10,pass_date='2020-1-1')
    #dic=student.objects.filter(marks=10).count()

# field lookups.........
    
    #dic=student.objects.filter(name__exact='vinayak')
    #dic=student.objects.filter(name__contains='vinayak')
    #dic=student.objects.filter(id__in=[1,2,3])
    #dic=student.objects.filter(marks__gt=77)
    #dic=student.objects.filter(marks__lt=77)
    #dic=student.objects.filter(marks__lte=77)
    #dic=student.objects.filter(name__startswith='vi')
    #dic=student.objects.filter(name__endswith='ak')

# aggregation.............

    dic=student.objects.all()
    avg=dic.aggregate(Avg('marks'))
    #avg=dic.aggregate(Max('marks'))
    #avg=dic.aggregate(Min('marks'))
    #avg=dic.aggregate(Sum('marks'))
    #avg=dic.aggregate(Variance('marks'))
    #avg=dic.aggregate(StdDev('marks'))
    return render(request,'core/home.html',{'data':dic,'avg':avg})