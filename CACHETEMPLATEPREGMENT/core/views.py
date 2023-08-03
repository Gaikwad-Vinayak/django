from django.shortcuts import render

# Create your views here.
def cache(request):
    return render(request,'core/cache.html')