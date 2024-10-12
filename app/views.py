from django.shortcuts import render, redirect

from app.models import Car

from .forms import CarForm

def cars_view(request):
    cars = Car.objects.all()

    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)


    return render(request, 'app/list.html', context={"cars": cars, "title": "Carros"})

def new_car(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)

        if car_form.is_valid():
            car_form.save()
            return redirect('cars_list')

    else:
        car_form = CarForm()

    return render(request, 'app/newcar.html', context={"title": "Novo Carro", 'form': car_form})
