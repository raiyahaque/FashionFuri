from django.urls import path

from . import views
app_name = 'myapp'

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register, name="register"),
    path('<slug:category_slug>/', views.get_clothes, name="get_clothes"),
    path('<slug:category_slug>/<str:gender>', views.gender_clothes, name="gender_clothes"),
    path('<int:clothing_id>/<slug:slug>/', views.clothing_description, name="clothing_description"),
    path('search', views.search, name="search")
]
