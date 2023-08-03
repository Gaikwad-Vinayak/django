from django.shortcuts import render
from .models import student
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    dt=student.objects.all().order_by('id')
    pagei=Paginator(dt,2)
    page_no=request.GET.get('page')
    page_obj=pagei.get_page(page_no)
    return render(request,'core/home.html',{'data':page_obj})