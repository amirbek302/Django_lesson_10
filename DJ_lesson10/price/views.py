from django.shortcuts import render
from .models import Price_data as Price


def price(request):
    cars = Price.objects.all()

    context = {'cars': cars}
    return render(request, 'price.html', context)