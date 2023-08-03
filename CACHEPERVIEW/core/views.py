from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(20)
def cache(request):
    return render(request,'core/cache.html')