from django.shortcuts import render
from .models import student
# Create your views here.
def home(request):
    dic=student.students.all()
    return render(request,'core/home.html',{'data':dic})