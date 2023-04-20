from django.shortcuts import render, redirect
from .models import PhotoOfWorks, TypeOfServices, CalculateTableEx, ListOfWorks, ContactOfOrganization
# UserCreationForm импорт формы которая создаёт пользователя
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from .forms import CalculateTableExForm, ListOfWorksForm, SendMessageForm


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


def contact(request):
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


def calculate_table(request):  # функция калькуляции в виде таблицы checkbox
    if request.method == 'GET':
        summ = 0
        form = ListOfWorksForm()
        obj = ListOfWorks.objects.all()
        return render(request, 'main/calculate_table.html', {'form': form, 'obj': obj, 'summ': summ})
    else:
        obj = ListOfWorks.objects.all()
        form = ListOfWorksForm()
        all_square = request.POST.getlist('square')  # получаем список указанных площадей в теге input name="square"
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
                lst_pricing.append(i.price)
            if squares:
                for j in range(len(squares)):
                    if all_square[j].isdigit():
                        total = int(lst_pricing[j]) * int(squares[j])
                        summ += total
            return summ

        total_summ(obj, all_square)
        return render(request, 'main/calculate_table.html', {'form': form, 'obj': obj, 'summ': summ})
