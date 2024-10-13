from django.shortcuts import render, redirect

from app.models import Car

from .forms import CarModelForm

from django.views.generic import View, ListView, CreateView


class CarsListView(ListView):
    model = Car
    template_name = 'app/list.html'
    context_object_name = 'cars'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset


class NewCarView(View):
    def get(self, request):
        car_form = CarModelForm()
        return render(request, 'app/newcar.html', context={"title": "Novo Carro", 'form': car_form})

    def post(self, request):
        car_form = CarModelForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            return redirect('car_list')
        return render(request, 'app/newcar.html', context={"title": "Novo Carro", 'form': car_form})


class CarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'app/newcar.html'
    success_url = '/cars/'