from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Products

def view_cart(request):
    session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    cart_items = CartItem.objects.filter(cart=cart)
    
    total_price = sum(item.sub_total() for item in cart_items)
    tax = total_price * 0.1  
    overall_total = total_price + tax

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'tax': tax, 'overall_total': overall_total})


def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    cart_item.delete()
    return redirect('view_cart')

def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')
