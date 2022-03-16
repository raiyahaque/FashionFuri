from django.contrib import admin
from .models import User, Category, Clothing
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'category', 'gender']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
