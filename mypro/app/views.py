from django.contrib import messages
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.shortcuts import render,redirect
from .models import Watch,CartItem
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'index.html',data)

# @login_required
# def index(request):
#     if request.user.is_authenticated:
#         return render(request,'index.html')

def details(request,id):
    product=Watch.objects.get(pk=id)
    print(product)
    data={
        'data':product
    }
    return render(request,'details.html',data)

# USER AUTHENTICATION PART
def signup(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        if request.method =='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('pass')
            password2=request.POST.get('cpass')
            if password1==password2:
                if User.objects.filter(username=username,email=email).exists():
                    messages.info(request,'username already exists!!!!')
                    print("already have")
                else:
                    new_user=User.objects.create_user(username,email,password1)
                    new_user.save()
                    return redirect(user_login)
            else:
                print('wrong password')
        return render(request,'signup.html')

def user_login(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password1=request.POST.get('pass1')
            user=authenticate(request,username=username,password=password1)
            if user is not None:
                login(request,user)
                return redirect(index)
            else:
                messages.info(request,'user not exists')
                print('user no exist')

        return render(request,'login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return redirect(index)

def support(request):
    return render(request,'support.html')

def mec(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'mec.html',data)
def auto(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'auto.html',data)
def smt(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'smt.html',data)
def qur(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'qur.html',data)
def cro(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'cro.html',data)
def about(request):
    return render(request,'about.html')

# cart

def product_list(request):
    products = Watch.objects.all()
    return render(request, 'index.html', {'products': products})
 
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = Watch.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(view_cart)
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect(view_cart)