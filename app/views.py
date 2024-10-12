from django.shortcuts import render

from app.models import Car

from .forms import CarForm

def cars_view(request):
    cars = Car.objects.all()

    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)


    return render(request, 'app/list.html', context={"cars": cars, "title": "Carros"})

def new_car(request):
    form = CarForm()
    return render(request, 'app/newcar.html', context={"title": "Novo Carro", 'form': form})