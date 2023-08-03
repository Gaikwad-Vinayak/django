from django.shortcuts import render
from .models import student,teacher
# Create your views here.
def home(request):

    #dic=student.objects.all()
    #dic=student.objects.filter(roll=104)
    #dic=student.objects.exclude(roll=104)
    #dic=student.objects.order_by('id')
    #dic=student.objects.order_by('id').reverse
    #dic=student.objects.values('name','roll')
    #dic=student.objects.values_list('name','roll','marks',named=True)
    #dic=student.objects.dates('pass_date',kind='day')

    # union----

    #q1=student.objects.values_list('name','city',named=True)
    #q2=teacher.objects.values_list('name','city',named=True)
    #dic=q2.union(q1)

    # difference----

    #q1=student.objects.values_list('name','city',named=True)
    #q2=teacher.objects.values_list('name','city',named=True)
    #dic=q2.difference(q1)
    
    #opraters
    #dic=student.objects.filter(id=1)& student.objects.filter(name='vinayak')
    from django.db.models import Q
    #dic=student.objects.filter(Q(id=1) | Q(name='vinayak'))
    dic=student.objects.filter(Q(id=1) & Q(name='vinayak'))


    return render(request,'core/home.html',{'data':dic})