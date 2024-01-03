from django.contrib import admin
from .models import *


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ('color', 'quantity')


@admin.register(Tire)
class TireAdmin(admin.ModelAdmin):
    list_display = ('type', 'quantity')


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('color', 'quantity')


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    ...


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    ...


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...