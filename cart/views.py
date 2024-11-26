from django.shortcuts import render, get_object_or_404
from .cart import Cart
from catalogue.models import VinylRecord
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    cart_vinyls = cart.get_prods
    # cart_vinyls = cart.get_prods()
    return render(request, "cart/cart_summary.html", {"cart_vinyls": cart_vinyls})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        vinyl_id = int(request.POST.get('vinyl_id'))
        #поиск винил в бд
        vinyl = get_object_or_404(VinylRecord, id=vinyl_id)
        #сохранить в сессию
        cart.add(vinyl=vinyl)
        response = JsonResponse({'Vinyl Name: ': vinyl.title})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        vinyl_id = int(request.POST.get('vinyl_id'))
        cart.delete(vinyl=vinyl_id)
        response = JsonResponse({'vinyl': vinyl_id})
        return response


def cart_update(request): # думаю нам это не надо и уже как будто будет лишним
    pass


