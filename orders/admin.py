from django.contrib import admin
from .models import Order, Item

# Register your models here.
class OrderItem(admin.TabularInline):
    model = Item
    raw_id_fields = ['clothing']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first', 'last', 'email', 'address',
                    'postalcode', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItem]
