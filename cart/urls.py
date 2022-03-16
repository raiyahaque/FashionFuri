from django.urls import path

from . import views
app_name = 'cart'

urlpatterns = [
    path('', views.details, name='details'),
    path('add/<int:clothing_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:clothing_id>/', views.cart_remove, name='cart_remove')
]
