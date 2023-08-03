from django.shortcuts import render,HttpResponse

# Create your views here.
def sets(request):
    request.session['name']='vinayak'
    return render(request,'core/set.html')

def gets(request):
    if 'name' in request.session:
        dic=request.session.get('name','none')
    # dic=request.session['name']
        dtc=request.session.items()
        dt=request.session.keys()
        return render(request,'core/get.html',{'data':dic,'items':dtc,'key':dt})
    return HttpResponse('delete session')

def delete(request):
    del request.session['name']
    dtc=request.session.flush()
    # dtc=request.session.clean()
    return render(request,'core/delete.html',{'clear':dtc})