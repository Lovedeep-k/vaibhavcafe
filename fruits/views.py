from django.shortcuts import render,HttpResponse,redirect
from .models import*



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



























