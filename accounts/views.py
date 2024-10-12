from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()

            return redirect('car_list')
        else:
            messages.add_message(request, messages.INFO, 'Erro ao cadastrar usuário')
            return redirect('accounts_register')
    else:
        user_form = UserCreationForm()
        return render(request, 'accounts/register.html', {'user_form': user_form})
