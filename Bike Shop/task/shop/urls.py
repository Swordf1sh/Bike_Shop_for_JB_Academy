from django.urls import path
from .views import BikeShopView, BikeDetailView, OrderDetailView

urlpatterns = [
    path('bikes/', BikeShopView.as_view(), name='bike_shop'),
    path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bike_details'),
    path('order/<int:order_id>/', OrderDetailView.as_view(), name='order_create'),
]
