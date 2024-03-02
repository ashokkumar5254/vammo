from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import category,product,session_model,cartitem
import stripe
from django.conf import settings

YOUR_DOMAIN = 'http://127.0.0.1:8000/'

def product_view(request,id):
    data1=category.objects.get(id=id)
    data2=product.objects.filter(category_product=data1)
    data3=data2.count()
    return render(request,'product.html',{'data2':data2,'data3':data3})

def single_view(request,product_name):
    data1=product.objects.get(product_name=product_name)
    return render(request,'single.html',{'data1':data1})
# Create your views here.
def cart_item(request,id):
    ashok=product.objects.get(id=id)
    def create_session(request):
        a=request.session['name']='ashokkumar'
        return a
    try:
        first=session_model.objects.get(session_id=create_session(request)) 
        print('excute try block')    
    except session_model.DoesNotExist:
        first=session_model.objects.create(session_id=create_session(request))
        print('execute except block')
    first=session_model.objects.get(session_id=create_session(request)) 
    try:
        data1=cartitem.objects.get(cart_session=first,cart_product=ashok)
       
        print(' cartitem data is there')
    except cartitem.DoesNotExist:
        data1=cartitem.objects.create(cart_session=first,cart_product=ashok,quantity=1)
        data1.cart_price=data1.quantity*data1.cart_product.product_price
        data1.save()
        print('cartitem data created')
    return redirect('cart')
def increament(request,id):
   print('increament')
   ashok=cartitem.objects.get(id=id)
   ashok.quantity += 1
   ashok.cart_price=ashok.quantity * ashok.cart_product.product_price
   ashok.save()
   print('completed')
   return redirect('cart')

def decreament(request,id):
    print('decreament')
    data=cartitem.objects.get(id=id)
    if data.quantity != 1:
        data.quantity -= 1
        data.cart_price=data.quantity*data.cart_product.product_price
        data.save()
    else:
        data.delete()
    return redirect('cart',)
def cart(request):
    data=0
    data1=cartitem.objects.all()
    for i in data1:
        data += i.cart_price

    return render(request,'cart.html',{'data1':data1,'data':data})


stripe.api_key =settings.STRIPE_SECRET_KEY
    
def checkout_payment(request,id):
    ashok=cartitem.objects.get(id=id)
    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                    'name': ashok.cart_product.product_name,
                    },
                    'unit_amount': int(ashok.cart_product.product_price * 100),
                },
                'quantity': ashok.quantity,
            }
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + 'product/success',
        cancel_url=YOUR_DOMAIN + 'product/cancel'
        )
    return redirect(checkout_session.url, code=303)

def success(request):
    return HttpResponse('this is success')
def cancel(request):
    return HttpResponse('this is cancel')
    
    