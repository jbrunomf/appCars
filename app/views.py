from django.shortcuts import render

from models import Car


def cars_view(request):
    cars = Car.objects.all()

    return render(request, 'app/list.html', context={"cars": cars, "title": "Carros"})
