from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def reset_password(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'app/reset_password.html')
        
        try:
            user = User.objects.get(username=username, email=email)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your password has been reset successfully')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or email')
    return render(request, 'app/reset_password.html')
def detail(request):
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
        user_not_login="hidden"
        user_login="show"
    else:
        items=[]
        order={'order.get_cart_items':0,'order.get_cart_total':0}
        cartItems=order['order.get_cart_items']
        user_not_login="show"
        user_login="hidden"
    id=request.GET.get('id','')
    products=Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub=False)
    context={'items':items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login,'categories':categories,'products':products}
    return render(request, 'app/detail.html',context)
def category(request):
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')
    products = []  # Khởi tạo biến products với giá trị mặc định
    if active_category:
        products = Product.objects.filter(category__slug=active_category)
    context = {'categories': categories, 'products': products, 'active_category': active_category}
    return render(request, 'app/category.html', context)
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched','')
        keys = Product.objects.filter(name__contains=searched)
        return render(request, 'app/search.html', {'searched':searched, 'keys':keys})
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems=order['get_cart_items']
    products=Product.objects.all()
    return render(request, 'app/search.html', {searched:'searched', 'keys':keys, 'products':products, 'cartItems':cartItems})
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'app/register.html', context)    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')
    context={}
    return render(request, 'app/login.html',context)   
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
        user_not_login="hidden"
        user_login="show"
    else:
        items=[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems=order['get_cart_items']
        user_not_login="show"
        user_login="hidden"
    categories=Category.objects.filter(is_sub=False)
    active_category=request.GET.get('category','')
    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login,'categories':categories} 
    return render(request, 'app/home.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
        user_not_login="hidden"
        user_login="show"
    else:
        items=[]
        order={'order.get_cart_items':0,'order.get_cart_total':0}
        cartItems=order['order.get_cart_items']
        user_not_login="show"
        user_login="hidden"
    context={'items':items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request, 'app/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
        user_not_login="hidden"
        user_login="show"
    else:
        items=[]
        order={'order.get_cart_items':0,'order.get_cart_total':0}
        cartItems=order['order.get_cart_items']
        user_not_login="show"
        user_login="hidden"
    context={'items':items,'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request, 'app/checkout.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_items':0,'get_cart_total':0}
    context={'items':items,'order':order}
    return render(request, 'app/checkout.html',context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)