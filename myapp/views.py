from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from werkzeug.security import check_password_hash, generate_password_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



from .models import User, Category, Clothing
from cart.forms import CartAddProductForm

# Create your views here.
def homepage(request):
    return render(request, 'myapp/homepage.html')


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        email = request.POST["email"]
        object = User.objects.get(email=email)
        username = object.username
        #print(username)
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)


        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('myapp:homepage')
        else:
            return render(request, 'myapp/login.html', {
                "message": "Invalid username or password."
            })
    else:
        return render(request, 'myapp/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmed_pass = request.POST["confirm-password"]
        if password == confirmed_pass:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect('myapp:homepage')
    else:
        return render(request, "myapp/register.html")


def get_clothes(request, category_slug=None):
    if category_slug:
        # Get category using category_slug
        category = Category.objects.get(slug=category_slug)
        if category:
            # Get clothes in the category
            clothes = Clothing.objects.filter(category=category)
    else:
        clothes = Clothing.objects.all()

    paginator = Paginator(clothes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'myapp/clothes.html', {
        "page_obj": page_obj
    })

def gender_clothes(request, category_slug=None, gender=None):
    if category_slug:
        try:
            category = Category.objects.get(slug=category_slug)
            if category:
                # Get clothes for a specific gender in a specific category
                clothes = Clothing.objects.filter(category=category, gender=gender)
        except Category.DoesNotExist:
            clothes = Clothing.objects.filter(gender=gender)

    paginator = Paginator(clothes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'myapp/clothes.html', {
        "page_obj": page_obj
    })



def logout_view(request):
    logout(request)
    return redirect('myapp:homepage')


def clothing_description(request, clothing_id, slug):
    clothing = Clothing.objects.get(pk=clothing_id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'myapp/clothing_description.html', {
        "clothing": clothing,
        "cart_product_form": cart_product_form
    })

def search(request):
    if request.method == "POST":
        user_search = request.POST["search"]
        try:
            # Categorical searches
            category = Category.objects.get(slug=user_search)
        except Category.DoesNotExist:
            category = None
        clothes = Clothing.objects.all()
        matches = []
        for clothing in clothes:
            # Matches in clothing name or color
            if user_search in clothing.name.lower() or user_search in clothing.color.lower():
                matches.append(clothing)

        if len(matches) == 0:
            if category:
                searches = Clothing.objects.filter(category=category)
                return render(request, 'myapp/search.html',{
                    "clothes": searches
                })
            else:
                # No searches found
                return render(request, 'myapp/search.html',{
                    "clothes": None,
                    "message": "No searches found."
                })
        else:
            return render(request, 'myapp/search.html',{
                "clothes": matches
            })
