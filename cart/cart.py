from decimal import Decimal
from django.conf import settings
from myapp.models import Clothing

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        clothing_ids = self.cart.keys()
        clothes = Clothing.objects.filter(id__in=clothing_ids)
        cart = self.cart.copy()
        for clothing in clothes:
            cart[str(clothing.id)]['clothing'] = clothing
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, clothing, quantity, size, new_quantity=False):
        # Add product to cart
        clothing_id = str(clothing.id)
        if clothing_id not in self.cart:
            self.cart[clothing_id] = {"quantity": 0, "price": str(clothing.price), "size": size}
        if new_quantity:
            self.cart[clothing_id]['quantity'] = quantity
        else:
            self.cart[clothing_id]['quantity'] += quantity
        self.save()

    def remove(self, clothing):
        # Remove product from cart
        clothing_id = str(clothing.id)
        if clothing_id in self.cart:
            del self.cart[clothing_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
