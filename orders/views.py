from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required
def create_order(request):
    cart = Cart(request)
    if not len(cart):
        return redirect('cart:cart_summary')

    order = Order.objects.create(user=request.user)
    
    for item in cart.get_prods():
        OrderItem.objects.create(
            order=order,
            vinyl=item,
            price=item.price,
        )

    cart.clear()

    # имитация оплату
    order.is_completed = True  
    order.save()

    return redirect('orders:order_list')

@login_required
def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if not order.is_completed:
        order.is_completed = True  
        order.save()
    return HttpResponseRedirect(reverse('orders:order_list'))

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})
