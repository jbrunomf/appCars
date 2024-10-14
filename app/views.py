from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from app.models import Car

from .forms import CarModelForm

from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView


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


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class CarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'app/newcar.html'
    success_url = '/cars/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'app/detail.html'
    context_object_name = 'car'


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'app/update.html'
    success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'app/delete.html'
    success_url = '/cars/'
