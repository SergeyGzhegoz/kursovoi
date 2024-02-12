from django.contrib import admin
from .models import Fuel, DriveType, Orders, Status, Cars, Brands


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'status', 'car', 'description')
    list_display_links = ('id', 'created', 'status', 'car', 'description')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(DriveType)
class DriveTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'engine_capacity', 'engine_power', 'fuel', 'drive_type')
    list_display_links = ('brand', 'model', 'engine_capacity', 'engine_power', 'fuel', 'drive_type')
