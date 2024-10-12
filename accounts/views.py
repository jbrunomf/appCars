from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()

            return redirect('accounts_register')
        else:
            messages.add_message(request, messages.INFO, 'Erro ao cadastrar usuário')
            return redirect('accounts_register')
    else:
        user_form = UserCreationForm()
        return render(request, 'accounts/register.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('car_list')
        else:
            messages.add_message(request, messages.INFO, 'Erro ao logar. Verifique os dados informados')
            return redirect('accounts_login')
    else:
        login_form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect(
        'accounts_login'
    )