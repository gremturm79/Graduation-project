from django.shortcuts import render, redirect
from .models import ListOfWorks
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError, models
from django.contrib.auth import login, logout, authenticate, get_user_model


def index(request):
    date = ListOfWorks.objects.all()
    if request.method == 'GET':
        return render(request, 'calculator/index.html', {'date': date})
    else:
        date = ListOfWorks.objects.all()
        check = request.POST.getlist('checks[]')
        square = request.POST.getlist('sq')
        res = round(int(square[0]))
        print(res)
        summ = 0
        for i in check:
            summ += int(i)
        return render(request, 'calculator/index.html', {'date': date, 'summa': summ * res})


def signupuser(request):  # функция для регистрации на сайте
    if request.method == 'GET':  # если метод GET возвращаем страницу регистрации
        return render(request, 'calculator/signup.html', {'form': UserCreationForm()})
    else:  # если метод POST
        username = request.POST.get('username')
        if get_user_model().objects.filter(username=username).exists():  # проверка на существования имени в БД
            return render(request, 'calculator/signup.html', {'form': UserCreationForm(),
                                                              'error': 'Имя пользователя существует, выберите другое имя'})

        elif request.POST['password1'] == request.POST['password2']:  # если пароли совпадают
            try:  # пробуем зарегистрировать нового пользователя, записав его в БД
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()  # сохранение нового пользователя
                login(request, user)  # авторизация пользователя
                return redirect('index')
            except IntegrityError:  # если имя пользователя уже существует, используем ошибку БД IntegrityError
                return render(request, 'calculator/signup.html', {'form': UserCreationForm(),
                                                                  'error': 'Имя пользователя уже существует, выберите другое имя'})

        else:
            return render(request, 'calculator/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def loginuser(request):  # функция авторизации
    if request.method == 'GET':
        return render(request, 'calculator/login.html', {'form': AuthenticationForm()})
    else:
        # проверка учётной записи, регистрации пользователя по имени и паролю
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'calculator/loginuser.html', {'form': AuthenticationForm(),
                                                                 'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')
