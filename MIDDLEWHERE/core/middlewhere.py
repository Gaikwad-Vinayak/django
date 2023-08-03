from urllib import response
from django.shortcuts import HttpResponse

# function based view

#def Mymiddleware(get_response):
#    print('one time initilize')
#    def my_function(request):
#        print('befour view')
#        res=HttpResponse('undersiteconstruction')
#        print('after view')
#        return res
#    return my_function


# class based view
class Mymiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('one time initilaize')
    def __call__(self,request):
        print('befourview')
        response=HttpResponse('under site consructor')
        print('after view')
        return response


