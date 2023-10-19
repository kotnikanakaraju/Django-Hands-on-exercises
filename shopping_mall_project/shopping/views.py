from django.shortcuts import render

from .models import Cart, CartItem, Product

def product_list(request):
    products=Product.objects.all()
    return render(request,'shopping/product_list.html',{'products':products})

def add_to_cart(request,product_id):
    if 'cart_id' not in request.session:
        cart=Cart.objects.create(user_id=request.session.session_key)
        request.session['cart_id']=cart.user_id
    else:
        cart=Cart.objects.get(id=request.session['cart_id'])

    product=Product.objects.get(id=product_id)
    CartItem, created=CartItem.objects.get_or_create(cart=cart,product=product)
    if not created:
        CartItem.quantity+=1
        CartItem.save()

def view_cart(request):
    if 'cart_id' in request.session:
        cart=Cart.objects.get(id=request.session['cart_id'])
        cart_items=cart.cartitem.set.all()
    else:
        cart_items=[]
    return render(request,'shopping/view_cart.html',{'cart_items':cart_items})
          
