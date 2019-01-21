from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt
  
def index(request):
    # request.session.clear()
    # if 'user' not in request.session:
    #     request.session['user'] = None
    return render(request,"ecommerce/front.html")

def home(request):
    return render(request,"ecommerce/home.html")

def menu(request):
    return render(request,'ecommerce/menu.html')

def product_detail(request):
    return render(request, 'ecommerce/product.html')

def shopping(request):
    return render(request,'ecommerce/shopping_cart.html')

def signIn(request):
    return render(request,'ecommerce/sign_in.html')

def signUp(request):
    return render(request,'ecommerce/sign_up.html')

def user(request):
  
    return render(request,'ecommerce/user.html')

def edit(request):
    return render(request,'ecommerce/edit.html')
def order(request):
    return render(request,'ecommerce/order.html')

def order_detail(request):
    return render(request,'ecommerce/order_detail.html')

def register(request):
    # request.session.clear()
    # errors = User.objects.basic_validator(request.POST)
    
    # if len(errors):
    #     for key,value in errors.items():
    #         messages.error(request,value, extra_tags="register_error:"+str(key))
    #     return redirect("/signUp")

    # else:
    #     user = User.objects.create()
    #     user.first_name = request.POST['first_name']
    #     user.last_name= request.POST['last_name']
    #     user.email = request.POST['email']
    #     hash1 = bcrypt.hashpw(request.POST['code'].encode(), bcrypt.gensalt())
    #     user.password = hash1
        
    #     user.save()
    #     request.session['user'] = user.first_name
    #     request.session['id']= user.id
        return redirect("/user")

def login(request):
    # request.session.clear()
    # if len(request.POST['email2']) < 1:
    #     messages.error(request, "Email cannot be blank.", extra_tags='suggest_email')
    # if len(request.POST['code2']) < 1:
    #     messages.error(request,"Password cannot be blank", extra_tags="suggest_pw")
    # if len(request.POST['email2']) > 1 and len(request.POST['code2']) > 0:

    #     if User.objects.filter(email=request.POST['email2']):
    #         user = User.objects.filter(email=request.POST['email2'])
            
    #         if bcrypt.checkpw(request.POST['code2'].encode(), user[0].password.encode()):
    #             request.session['user'] = user[0].first_name
    #             request.session['id'] = user[0].id
    #             return redirect("/user")
    #         else:
    #             messages.error(request,'Wrong Password', extra_tags='suggest_pw')
    #             return redirect("/sign_in")
    #     else:
    #         messages.error(request,'User does not exist, please register', extra_tags='suggest_email')
    #         return redirect("/sign_in")
    return redirect("/sign_in")