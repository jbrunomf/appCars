from django.shortcuts import render

from app.models import Car


def cars_view(request):
    cars = Car.objects.all()

    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)


    return render(request, 'app/list.html', context={"cars": cars, "title": "Carros"})
