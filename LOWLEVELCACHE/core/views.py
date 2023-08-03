from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
def cache(request):
    dic=cache.get_or_set('my_new_key', 'my new value', 100)
    return render(request,'core/cache.html',{'cache':dic})