from django.shortcuts import render, redirect, reverse
from .models import PhotoOfWorks, TypeOfServices, ListOfWorks, ContactOfOrganization, \
    Review, Company, SummOfWorks, PricingAndSummWorks
# UserCreationForm импорт формы которая создаёт пользователя
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ContactForm, UserForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ListOfWorksForm, SendMessageForm, ProfileUserForm, ReviewForm
from django.contrib import messages
from .utils import send_message, personal_view, cost_works


def index(request):
    contact_org = ContactOfOrganization.objects.all()
    company = Company.objects.all()
    company_services = Company.objects.get(id=1)
    company_all = company_services.typeofservices_set.all()
    context = {
        'company': company,
        'company_all': company_all,
        'contact': contact_org
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
            message = request.POST['phone']
            message_text = 'Вас просят перезвонить по номеру ' + '\n' + '+7-' + message
            send_message(message_text)
            return render(request, 'main/index.html', context)
        else:
            messages.info(request, 'Необходимо зарегистрироваться')
            return redirect('enter')
    return render(request, 'main/index.html', context)


def main(request):
    services = TypeOfServices.objects.all()
    contact_org = ContactOfOrganization.objects.all()
    context = {
        'services': services,
        'contact': contact_org
    }
    return render(request, 'main/about.html', context)


def gallery(request):
    photo_list = PhotoOfWorks.objects.all()
    contact_org = ContactOfOrganization.objects.all()
    context = {
        'images': photo_list,
        'contact': contact_org
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
        contact_org = ContactOfOrganization.objects.all()
        form = ContactForm()
        context = {
            'form': form,
            'contact': contact_org
        }
        return render(request, 'main/calculate.html', context)


def reviews(request):
    # author = User.objects.filter(first_name='Grems')[0]
    # review = Review.objects.filter(owner=author)  # находим данные из БД Review по имени автора статьи
    # напоминание о количестве отзывов
    reviews_all = Review.objects.all()
    contact_org = ContactOfOrganization.objects.all()
    context = {
        'reviews': reviews_all,
        'contact': contact_org
    }
    return render(request, 'main/reviews.html', context)


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
    if request.method == 'GET':  # при методе GET возвращаем страницу с формой регистрации
        contact_org = ContactOfOrganization.objects.all()
        messages.info(request, 'Пройдите регистрацию для доступа к дополнительному функционалу')
        return render(request, 'main/enter.html',
                      {'form': UserCreationForm(), 'contact': contact_org})  # модель Form импорт из
        # django.contrib
    else:  # при методе POST регистрируем пользователя со своей проверкой на соответствие паролей и проверкой Django
        # на наличие имени пользователя
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                messages.info(request, 'Вы успешно зарегистрировались')
                return redirect('index')
            except IntegrityError:
                contact_org = ContactOfOrganization.objects.all()
                context = {
                    'form': UserCreationForm(),
                    'error': 'Такое имя пользователя существует выберите другое',
                    'contact': contact_org
                }
                return render(request, 'main/enter.html', context)

        else:
            return render(request, 'main/enter.html', {'form': UserCreationForm(),
                                                       'error': 'Пароли не совпадают'})


def logout_user(request):
    logout(request)
    messages.info(request, 'Вы вышли из сессии')
    return redirect('login')


def login_user(request):
    contact_org = ContactOfOrganization.objects.all()
    if request.method == 'GET':  # авторизация зарегистрированного пользователя
        return render(request, 'main/loginuser.html', {'form': AuthenticationForm(), 'contact': contact_org})
    else:  # authenticate метод проверки существующего пользователя
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:  # если user возвращает None, тогда возвращаемся на страницу loginuser.html
            context = {
                'form': AuthenticationForm(),
                'contact': contact_org
            }
            messages.info(request, 'Пользователя с таким именем не существует')
            return render(request, 'main/loginuser.html', context)
        else:  # иначе, сохраняются данные пользователя в серверной части запроса пока пользователь находится в сессии

            login(request, user)
            return redirect('about')


@login_required()
def delete_user(request):
    custom = request.user
    if request.method == 'GET':
        return render(request, 'main/delete.html')
    else:
        custom.delete()
        messages.info(request, 'Аккаунт был успешно удалён')
        return redirect('about')


# @login_required(login_url='enter')
def calculate_table(request):  # функция калькуляции в виде таблицы checkbox
    contact_org = ContactOfOrganization.objects.all()
    if request.method == 'GET':
        custom = request.user
        if request.user.is_authenticated:
            if custom.pricingandsummworks_set.all().count() < 1:
                form = ListOfWorksForm()
                obj = ListOfWorks.objects.all()
                context = {
                    'form': form,
                    'obj': obj,
                    'contact': contact_org
                }
                return render(request, 'main/calculate_table.html', context)
            else:
                form = ListOfWorksForm()
                obj = ListOfWorks.objects.all()
                context = {
                    'form': form,
                    'obj': obj,
                    'contact': contact_org
                }
                messages.info(request, 'Удалите все расчёты в личном кабинете')
                return render(request, 'main/calculate_table.html', context)
        else:
            messages.info(request, 'форма для незарегистрированных пользователей')
            form = ContactForm()
            obj = ListOfWorks.objects.all()
            context = {
                'form': form,
                'obj': obj,
                'contact': contact_org
            }
            return render(request, 'main/calculate.html', context)
    else:
        custom = request.user
        if request.user.is_authenticated and custom.pricingandsummworks_set.all().count() >= 1:
            form = ListOfWorksForm()
            obj = ListOfWorks.objects.all()
            context = {
                'form': form,
                'obj': obj,
                'contact': contact_org
            }
            messages.info(request, 'Удалите все расчёты в личном кабинете')
            return render(request, 'main/calculate_table.html', context)
        else:
            cost = cost_works(request)  # функция расчёта стоимости работ находится в utils.py
            obj = ListOfWorks.objects.all()
            form = ContactForm()
            messages.info(request, 'Расчёт был посчитан')
            context = {
                'form': form,
                'obj': obj,
                'contact': contact_org
            }
            return render(request, 'main/calculate_table.html', context)


def personal_account(request, pk):  # функция представления личного кабинета
    if request.method == 'GET':
        if request.user.is_authenticated:  # если зарегистрирован пользователь
            context = personal_view(request, pk)
            return render(request, 'main/personal_account.html', context)
        else:  # иначе переход на страницу авторизации
            messages.warning(request, 'Необходимо авторизация или регистрация')
            return redirect('login')

    else:
        if request.POST.get('form_send'):
            custom = request.user
            if custom.pricingandsummworks_set.filter(owner=custom).exists():  # проверка на существование объекта
                if custom.pricingandsummworks_set.all().count() == 1:
                    message_text = custom.pricingandsummworks_set.all()
                    phone = '\n' + 'Контактный номер: ' + request.POST['phone']
                    # message_view = custom.pricingandsummworks_set.get(owner=custom)
                    #  get(owner=custom) берёт один элемент последний
                    #  print(message_view)
                    for i in range(len(message_text)):
                        send_message(message_text[i].estimate + phone)
                    # message = message_text[0].estimate + phone
                    # send_message(message)
                    messages.info(request, 'сообщение было отправлено')
                    context = personal_view(request, pk)
                    return render(request, 'main/personal_account.html', context)
                else:
                    messages.warning(request, 'Отправить можно только один расчёт')
                    context = personal_view(request, pk)
                    return render(request, 'main/personal_account.html', context)
            else:
                messages.info(request, 'У Вас отсутствуют расчёты')
                context = personal_view(request, pk)
                return render(request, 'main/personal_account.html', context)

        elif request.POST.get('delete_pricing'):  # удаление расчёта стоимости работ
            if request.user.is_authenticated:
                custom = request.user
                message_view = custom.pricingandsummworks_set.get(owner=custom)
                pricing = SummOfWorks.objects.filter(owner=custom)
                pricing_all_text = PricingAndSummWorks.objects.filter(owner=custom)
                pricing_all_text.delete()
                pricing.delete()
                messages.success(request, 'Все расчёты были удалены !')
                context = personal_view(request, pk=custom.id)
                return render(request, 'main/personal_account.html', context)
        else:
            form = UserForm(request.POST, instance=request.user)  # записываем все данные из User в форму
            form_profile = ProfileUserForm(request.POST, request.FILES, instance=request.user.profileuser)
            # также одно поле с фотографией из БД Profile
            if form.is_valid():
                custom = request.user
                form_profile.save()
                form.save()  # сохраняем изменения в БД User
                messages.success(request, 'Профиль был успешно изменён')
                # остаёмся на той же странице с отредактированным профилем
                context = personal_view(request, pk)
                return render(request, 'main/personal_account.html', context)


def write_reviews(request):
    contact_org = ContactOfOrganization.objects.all()
    if request.method == 'GET' and request.user.is_authenticated:
        custom = request.user
        count_reviews = Review.objects.filter(owner=custom).count()
        if count_reviews < 1:
            u_form = ReviewForm()
            context = {
                'form': u_form,
                'count': count_reviews
            }
            messages.info(request, 'Оставить отзыв можно только один раз')
            return render(request, 'main/form_reviews.html', context)
        else:
            u_form = ReviewForm()
            context = {
                'form': u_form,
                'count': count_reviews,
                'contact': contact_org
            }
            messages.info(request, 'Вы оставили отзыв, эта форма заполнения вам недоступна')
            return render(request, 'main/form_reviews.html', context)
    else:
        if request.user.is_authenticated:
            custom = request.user
            count_reviews = Review.objects.filter(owner=custom).count()
            review_date = ReviewForm(request.POST, request.FILES)
            if review_date.is_valid() and count_reviews < 1:
                res = review_date.save(commit=False)
                # привязываем пользователя написавшего отзыв к самому отзыву, через связь Foreignkey
                res.owner = request.user
                res.save()
                messages.success(request, 'Отзыв был успешно добавлен')
                return redirect('reviews')
            else:
                u_form = ReviewForm()
                messages.error(request, 'Вы пытаетесь заполнить форму дважды')
                return render(request, 'main/form_reviews.html', {'form': u_form, 'contact': contact_org})


def delete_pricing(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            custom = request.user
            pricing = SummOfWorks.objects.filter(owner=custom)
            pricing.delete()
            context = personal_view(request, pk=custom.id)
            return render(request, 'main/personal_account.html', context)
    else:
        return redirect(request, 'personal_account')
