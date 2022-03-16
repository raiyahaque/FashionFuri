from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from myapp.models import Clothing
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_POST
@login_required(login_url='/login')
def cart_add(request, clothing_id):
    cart = Cart(request)
    clothing = get_object_or_404(Clothing, id=clothing_id)
    form = CartAddProductForm(request.POST)
    size = request.POST["sizes"]
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(clothing=clothing, quantity=cd['quantity'], size=size, new_quantity=cd['new_quantity'])
    return redirect('cart:details')

@login_required(login_url='/login')
def cart_remove(request, clothing_id):
    cart = Cart(request)
    clothing = get_object_or_404(Clothing, id=clothing_id)
    cart.remove(clothing)
    return redirect('cart:details')

@login_required(login_url='/login')
def details(request):
    # Get cart
    cart = Cart(request)
    return render(request, 'cart/cart_details.html', {'cart':cart})
