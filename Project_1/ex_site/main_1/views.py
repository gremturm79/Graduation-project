from django.shortcuts import render, redirect
from .models import PhotoOfWorks, TypeOfServices, CalculateTableEx, ListOfWorks
# UserCreationForm импорт формы которая создаёт пользователя
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from .forms import CalculateTableExForm, ListOfWorksForm


def index(request):
    return render(request, 'main/index.html')


def main(request):
    services = TypeOfServices.objects.all()
    context = {
        'services': services
    }
    return render(request, 'main/about.html', context)


def gallery(request):
    photo_list = PhotoOfWorks.objects.all()
    context = {
        'images': photo_list
    }
    return render(request, 'main/gallery.html', context)


def calculate(request):
    if request.method == 'POST':
        # form = ContactForm(request.POST)
        form = ContactForm(request.POST, request.FILES)
        # if form.is_valid():
        name = request.POST['name']
        content = request.POST['content']
        email = request.POST['email']

        files = request.FILES.getlist('file')
        # print('file', files)
        # square = request.FILES['square']
        msg = EmailMessage(name, content, settings.EMAIL_HOST_USER, [email])
        for f in files:
            msg.attach(f.name, f.read(), f.content_type)
        msg.send()
        return redirect('about')
        # else:
        # return render(request, 'main/calculate.html', {'form': form, 'success': 'Повторите отправку'})
    else:
        form = ContactForm()
        return render(request, 'main/calculate.html', {'form': form})


def reviews(request):
    return render(request, 'main/reviews.html')


def contact(request):
    return render(request, 'main/contact.html')


def enter(request):
    if request.method == 'GET':  # при методе GET возвращаем страницу формой регистрации Django
        return render(request, 'main/enter.html', {'form': UserCreationForm()})
    else:  # при методе POST регистрируем пользователя со своей проверкой на соответствие паролей и проверкой Django
        # на наличие имени пользователя
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'main/enter.html', {'form': UserCreationForm(),
                                                           'error': 'Такое имя пользователя существует выберите другое'})
        else:
            return render(request, 'main/enter.html', {'form': UserCreationForm(),
                                                       'error': 'Пароли не совпадают'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('about')


def loginuser(request):
    if request.method == 'GET':  # авторизация зарегистрированного пользователя
        return render(request, 'main/loginuser.html', {'form': AuthenticationForm()})
    else:  # authenticate метод проверки существующего пользователя
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:  # если user возвращает None, тогда возвращаемся на страницу loginuser.html
            return render(request, 'main/loginuser.html', {'form': AuthenticationForm(), 'error': 'Неверные данные'})
        else:  # иначе, сохраняются данные пользователя в серверной части запроса пока пользователь находится в сессии
            login(request, user)
            return redirect('about')


def calculate_table(request):
    if request.method == 'GET':
        form = ListOfWorksForm()
        obj = ListOfWorks.objects.all()
        return render(request, 'main/calculate_table.html', {'form': form, 'obj': obj})
    else:
        form = ListOfWorksForm()
        obj = ListOfWorks.objects.all()
        lst = []
        for i in obj:
            lst.append(i.price)  # добавляем в список значения с полями price из БД ListOfWorks
            print(i.price)  # получаем все значения из БД ListOfWorks в поле price
        # check = request.POST.getlist('checks[]')  получаем список отмеченных полей для дальнейшей проверки
        square = request.POST.getlist('square')  # получаем список указанных площадей в теге input name="square"

        summ = 0
        if square:
            for i in range(len(square)):
                if square[i].isdigit():  # делая проверку на цифровое значении тем самым получаем индекс соответствующий
                    # индексации нашего списка lst с ценами на работы, которые мы взяли из БД ListOfWorks
                    total = int(lst[i]) * int(square[i])
                    summ += total

        return render(request, 'main/calculate_table.html', {'form': form, 'obj': obj, 'summ': summ})
