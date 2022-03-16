from django.shortcuts import render
from .models import Item, Order
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        # Collect personal information for order
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        address = request.POST['address']
        zip = request.POST['zip']
        city = request.POST['city']
        state = request.POST['state']
        phonenumber = request.POST['phone']

        # Create order
        order = Order(email=email, first=firstName, last=lastName,
                address=address, postalcode=zip, city=city, state=state, phonenumber=phonenumber)
        order.save()

        for item in cart:
            Item.objects.create(order=order, clothing=item['clothing'],
                    price=item['price'])

        cart.clear()
        return render(request, 'orders/order/ordered.html')

    else:
        return render(request, 'orders/order/personalDetails.html', {
            'cart': cart
        })

    return render(request, 'orders/order/personalDetails.html', {
            'cart': cart
    })
