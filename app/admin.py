from django.contrib import admin
from .models import Car, Brand


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'brand', 'factory_year', 'model_year', 'value']
    search_fields = ['model', 'brand', 'factory_year', 'model_year', 'value']
    list_filter = ['brand']
    list_per_page = 10
    list_max_show_all = 20
    sortable_by = ['model', 'brand', 'factory_year', 'model_year', 'value']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']