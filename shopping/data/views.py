from django.shortcuts import redirect, render
from .forms import userresi,profiledata,login,mypasswordchange,passwordresetform,passwordresetdoneform
from django.contrib.auth.models import User
from .models import Cart, Customer,Customer,Product,Orderplace
from django.contrib.auth.views import PasswordChangeView,LoginView,LogoutView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.edit import DeleteView,CreateView
from django.views.generic.base import TemplateView,View
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
# Create your views here.
# home 
class home(View):
    def get(self,request):
        mobiles=Product.objects.filter(category='m')
        electronic=Product.objects.filter(category='ele')
        return render(request, 'app/home.html',{'mobiles':mobiles,'electronic':electronic})
# product detail 


def product_detail(request,pk):
    dt=Product.objects.get(pk=pk)
    return render(request, 'app/productdetail.html',{'product':dt})

# add to cart

def add_to_cart(request):
    if request.user.is_authenticated:
        users=request.user
        product_i=request.GET.get('product_id')
        product=Product.objects.get(id=product_i)
        Cart(user=users,product=product).save()
        return redirect('/cart')
    return redirect('/accounts/login')
    
#buy now
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shopping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.selling_price)
                amount +=tempamount
                total_amount=amount+shopping_amount
        return render(request, 'app/addtocart.html',{'cart':cart,'total_amount':total_amount,'amount':amount,'shopping_amount':shopping_amount})
    return redirect('/accounts/login')

def buy_now(request):
 return render(request, 'app/buynow.html')

# user profile

def profile(request):
    if request.method=='POST':
        fm=profiledata(request.POST)
        if fm.is_valid():
            usr=request.user
            nm=fm.cleaned_data['name']
            add1=fm.cleaned_data['address']
            add2=fm.cleaned_data['address_2']
            ct=fm.cleaned_data['city']
            st=fm.cleaned_data['state']
            pin=fm.cleaned_data['pin_code']
            reg=Customer(user=usr,name=nm,address=add1,address_2=add2,city=ct,state=st,pin_code=pin)
            reg.save()
    else:
        fm=profiledata
    return render(request,'app/profile.html',{'form':fm,'active':'btn-primary'})


#profile address

def address(request):
    data=Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',{'data':data,'active':'btn-primary'})

# delete profile address

class deleteordersview(DeleteView):
    model=Customer
    success_url='/address/'
    template_name='app/addressdelete.html'

def orders(request):
 return render(request, 'app/orders.html')

# filter product

def mobile(request):
    dic=Product.objects.filter(category='m')
    return render(request, 'app/mobile.html',{'mobiles':dic})

# login view
class login(LoginView):
    template_name='app/login.html'
    success_url='/'


#custmer registration

class customerregistration(View):
    def get(self,request):
        form=userresi()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=userresi(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated.')
            return render(request, 'app/customerregistration.html',{'form':form})

# chack out 

def checkout(request):
    user=request.user
    address=Customer.objects.filter(user=user)
    cart=Cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user==user]
    if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.selling_price)
                amount +=tempamount
            total_amount=amount+shipping_amount
    return render(request, 'app/checkout.html',{'cart':cart,'add':address,'total_amount':total_amount})

# logout view

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')
#--------------------------------password related-----------------------------------------------------------
# password change 

class change_password(PasswordChangeView):
    form_class = mypasswordchange
    template_name='app/changepassword.html'

# password change done view
class password_changedone_view(PasswordChangeDoneView):
    template_name='app/home.html'

# password reset
class password_reset(PasswordResetView):
    form_class=passwordresetform
    template_name='app/password_reset.html'

# password reset done view
class password_reset_done(PasswordResetDoneView):
    template_name='app/password_reset_done.html'

#password reset confirm
class password_reset_confirm(PasswordResetConfirmView):
    template_name='app/password_token.html'
    form_class=passwordresetdoneform
    success_url='/accounts/login/'

#--------------------------------end password related-----------------------------------------------------------
