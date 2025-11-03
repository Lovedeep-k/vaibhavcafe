from django.shortcuts import render,HttpResponse,redirect
from .models import*
# from django.contrib.auth.decorators import login_required
# # from django.contrib.auth import authenticate, login
# from django.contrib.auth import authenticate, login 

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
# from django.urls import reverse





from django.contrib.auth.models import User
from django.contrib import messages



@login_required(login_url='/accounts/login/')

# Create your views here.
def index(request):
    dd=products.objects.all()
    return render(request,'index.html',{'dd':dd})
def aa(request):
    return render(request,'404.html')
def about(request):
    return render(request,'about.html')
def cart(request):
    cart_items=CartItem.objects.filter(user=request.user)
    total_price=sum(item.product.price * item.quantity for item in cart_items)
    return render(request,'cart.html',{'cart_items':cart_items,'total_price':total_price})
def checkouts(request):
    print('I am here ---------========================')
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        city = request.POST.get("city")  # 👈 You MUST include this

        # Save Order
        order_instance = Order.objects.create(
            user=request.user,
            name=name,
            email=email,
            address=address,
            phone=phone,
            city=city,
            total_price=total_price  # ✅ You missed this earlier
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order_instance,
                product=item.product,  # ✅ Fix typo: should be `product`, not `products`
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()
        return redirect(thankyou)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        subject=request.POST["name"]
        ob=student(NAME=name,EMAIL=email,PHONE=phone,SUBJECT=subject)
        ob.save()
        return HttpResponse("submitted form")
    return render(request,'contact.html')
def indexs(request):
    return render(request,'index_2.html')
def news(request):
    return render(request,'news.html')
def shop(request):
    aa=shopp.objects.all()
    return render(request,'shop.html',{'aa':aa})
def singlenews(request):
    return render(request,'single-news.html')

def singleproduct(request,id):
    d=products.objects.get(id=id)
    if request.method=='POST':
        qty=int(request.POST['qty'])
        x=CartItem(product=d,quantity=qty,user=request.user)
        x.save()
        return redirect(cart)
    return render(request,'single-product.html' ,{'d':d})

def remove(request,id):
    dd=CartItem.objects.get(id=id,user=request.user)
    dd.delete()
    return redirect(cart)


def thankyou(request):
    return render(request,'thankyou.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'accounts/register.html')






# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')  # redirect to home or wherever you want
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect('login')
#     return render(request, 'accounts/login.html')


# def logout_view(request):
#     logout(request)
#     return redirect('index')



# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect('login')
#     return render(request, 'login.html')


# # def logout_view(request):
# #     # logout(request)
# #     return redirect('index')
# #  from django.contrib.auth import login

# def login(request):
#     return login(request,login)


# @login_required(login_url='/login/')
# def cart(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            # After successful login, respect next parameter if present
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')




def register(request):
    if request.method=="POST":
        name=request.POST['Username']
        email=request.POST['email']
        phn=request.POST['phn']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            User.objects.create_user(username=name,email=email,password=password).save()
            return redirect(login)
        else:
            return HttpResponse("Password should be same")

    return render(request,'register.html')

def logout(request):
    auth_logout(request)
    return redirect('index')















