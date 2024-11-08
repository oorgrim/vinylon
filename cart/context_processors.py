from .cart import Cart
"""создание экземпляра корзины  для  запроса и возвращщает его в словарике"""
def cart(request):
    return {'cart': Cart(request)}