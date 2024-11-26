"""
проверяет, существует ли уже корзина в текущей сессии пользователя, тут есть ключ session key!
также создается нвый пустой словарик для данных об альбомах
"""

from catalogue.models import VinylRecord
class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart

    def add(self, vinyl):
        vinyl_id = str(vinyl.id)
        if vinyl_id in self.cart:
            pass
        else:
            self.cart[vinyl_id] = {'price': str(vinyl.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        vinyl_ids = self.cart.keys()
        vinyls = VinylRecord.objects.filter(id__in=vinyl_ids)
        return vinyls

    def delete(self, vinyl):
        vinyl_id = str(vinyl)
        if vinyl_id in self.cart:
            del self.cart[vinyl_id]
        self.session.modified = True