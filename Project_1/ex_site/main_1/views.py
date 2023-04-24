from django.shortcuts import render, redirect
from .models import PhotoOfWorks, TypeOfServices, CalculateTableEx, ListOfWorks, ContactOfOrganization
# UserCreationForm импорт формы которая создаёт пользователя
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ContactForm, UserForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import CalculateTableExForm, ListOfWorksForm, SendMessageForm
from django.contrib import messages


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


def contact(request):  # функция отправки сообщения для 'админа'
    if request.method == 'GET':
        contact_org = ContactOfOrganization.objects.all()
        form = SendMessageForm()
        context = {'form': form, 'contact': contact_org}
        return render(request, 'main/contact.html', context)
    else:
        contact_org = ContactOfOrganization.objects.all()
        name = request.POST['name']
        organization = request.POST['organization']
        email = request.POST['email']
        content = request.POST['content']
        msg = send_mail(name, content, settings.EMAIL_HOST_USER, [email])
        msg.send()
        context = {'success': 'письмо отравлено', 'contact': contact_org}
        return render(request, 'main/contact.html', context)


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


def logout_user(request):
    logout(request)
    return redirect('login')


def login_user(request):
    if request.method == 'GET':  # авторизация зарегистрированного пользователя
        return render(request, 'main/loginuser.html', {'form': AuthenticationForm()})
    else:  # authenticate метод проверки существующего пользователя
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:  # если user возвращает None, тогда возвращаемся на страницу loginuser.html
            return render(request, 'main/loginuser.html', {'form': AuthenticationForm(), 'error': 'Неверные данные'})
        else:  # иначе, сохраняются данные пользователя в серверной части запроса пока пользователь находится в сессии
            login(request, user)
            return redirect('about')


def calculate_table(request):  # функция калькуляции в виде таблицы checkbox
    if request.method == 'GET':
        summ = 0
        form = ListOfWorksForm()
        obj = ListOfWorks.objects.all()
        return render(request, 'main/calculate_table.html', {'form': form, 'obj': obj, 'summ': summ})
    else:
        obj = ListOfWorks.objects.all()  # данные из модели БД ListOfWorks
        all_square = request.POST.getlist('square')  # получаем список указанных площадей в теге input name="square"
        form = ListOfWorksForm()  # данные полей формы ListOfWorksForm для страницы  calculate_table.html
        summ = 0

        def total_summ(pricing, squares):
            '''
            функция total_summ рассчитывает сумму оплаты всех работ: выбранных клиентом также учитывая квадратные метры
            :param pricing: объект запроса данных из БД модели ListOfWorks
            :type pricing: class 'django.db.models.query.QuerySet'
            :param squares: список с данными из ListOfWorksForm тегов input с аттрибутом name="square"
            :type squares: class 'list'
            :return:
            :rtype:
            '''

            nonlocal summ
            lst_pricing = []
            for i in pricing:
                lst_pricing.append(i.price)  # в пустой список заносим данные поля price
            if squares: # если список
                for j in range(len(squares)): # проходим по его списку
                    if all_square[j].isdigit(): # если это цифры, берём элемент по этому индексу из списка lst_pricing
                        total = int(lst_pricing[j]) * int(squares[j])
                        summ += total
            return summ

        total_summ(obj, all_square)
        context = {
            'form': form,
            'obj': obj,
            'summ': summ
        }
        return render(request, 'main/calculate_table.html', context)


def personal_account(request, pk):  # функция представления личного кабинета если метод GET
    if request.method == 'GET' and request.user.is_authenticated:
        custom = request.user
        form = UserForm(instance=custom)  # заполняем поля формы редактирования, данными из БД User
        date = User.objects.get(id=pk)  # получаем данные из БД User для заполнения карточки пользователя
        context = {
            'user': date,
            'form': form
        }
        return render(request, 'main/personal_account.html', context)
    else:  # если метод POST отрабатывает форма редактирования данных пользователя
        form = UserForm(request.POST, instance=request.user)  # записываем все данные из формы
        if form.is_valid():
            form.save()  # сохраняем изменения в БД User
            messages.success(request, 'Профиль был удачно изменён')
        return redirect('login')


def write_reviews(request):  # метод для отзывов пока не реализован
    if request.method == 'GET' and request.user.is_authenticated:
        u_form = UserForm(instance=request.user)
        return render(request, 'main/personal_account.html', {'form': u_form})
    else:
        messages.error(request, 'Отзыв может написать только зарегистрированный пользователь')
        return redirect('enter')
