from django.shortcuts import render, redirect
from .models import Skills, Social
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


# импортируем класс UserCreationForm для создания формы
# регистрации

def index(request):
    projects = Skills.objects.all()
    social = Social.objects.all()
    return render(request, 'skills/index.html', {'projects': projects, 'social': social})


def signupuser(request):
    if request.method == 'GET':
        social = Social.objects.all()
        return render(request, 'skills/signup.html', {'form': UserCreationForm(), 'social': social})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)  # авторизация пользователя
                return redirect('index')
            except IntegrityError:
                social = Social.objects.all()
                return render(request, 'skills/signupuser.html', {'form': UserCreationForm(),
                                                                  'error': 'Имя пользователя не существует','social': social})
        else:
            social = Social.objects.all()
            return render(request, 'skills/signupuser.html', {'form': UserCreationForm(),
                                                              'error': 'Пароли не совпадают','social': social})


def loginuser(request):
    if request.method == 'GET':
        social = Social.objects.all()
        return render(request, 'skills/login.html', {'form': AuthenticationForm(),'social': social})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            social = Social.objects.all()
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Неверные данные для входа','social': social})
        else:
            login(request, user)
            return redirect('index')