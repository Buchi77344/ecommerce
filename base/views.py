from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Category, Product
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required



def index(request):
    product = Product.objects.all()
    context = {
        'product':product
    }
    return render(request, 'index.html',context)

def contact(request):
    return render ( request, 'contact.html')
def product_de(request, slug):
    prod = get_object_or_404(Product, slug=slug, instock =True)
    context = {
        'prod': prod
    }
    return render (request, 'product_de.html', context)
def cap(request):
    cart = Product.objects.all()
    context = {
        'cart':cart
    }
    return render (request, 'cap.html',context)
@login_required(login_url='login')
def product (request):
    return render (request, 'product.html')

def cart(request):
    return render (request, 'cart.html')
def test(request):
    pob = Category.objects.all()
    context = {
        'pob':pob
    }
    return render (request,'test.html',context)

def register(request):
    if request.method == 'POST':
        username =request.POST['username']
        email =request.POST['email']
        password =request.POST['password']
        password1 =request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exist')
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return redirect ('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect ('login')
        else:
            messages.error(request, 'password do not match')
            return redirect('register')
    else:
      return render (request, 'register.html')

def login(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password  = request.POST['password']
        user = auth.authenticate(request, username=username ,password =password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
           messages.error(request, 'invalid credentials')
           return redirect ('login')
    else:
      return render(request, 'login.html')