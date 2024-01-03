from django.views import View
from django.shortcuts import render, redirect
from .models import Bike
from .forms import OrderForm


# Create your views here.
class BikeShopView(View):

    def get(self, request, *args, **kwargs):
        context = {'bikes': Bike.objects.all()}
        return render(request, 'shop/bike_shop.html', context=context)


class BikeDetailView(View):

    def get(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        bike = Bike.objects.filter(id=kwargs['pk']).first()
        context = {
            'bike': bike,
            'form': form,
            'available': bike.is_available()
        }
        return render(request, 'shop/bike_details.html', context=context)

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            order = form.save(commit=False)
            order.bike = Bike.objects.filter(id=kwargs['pk']).first()
            order.bike.decrease_quantity()
            order.save()
            return redirect(f'/order/{order.pk}')
        return redirect('/bikes/')


class OrderDetailView(View):

    def get(self, request, *args, **kwargs):
        order_id = kwargs['order_id']
        context = {
            'order_id': order_id
        }
        return render(request, 'shop/order_details.html', context)
