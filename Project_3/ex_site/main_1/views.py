from django.shortcuts import render, redirect, reverse
from .models import PhotoOfWorks, TypeOfServices, ListOfWorks, ContactOfOrganization, \
    Review, Company, SummOfWorks, PricingAndSummWorks, ApartmentPrice
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
from .utils import send_message, personal_view, cost_works, search_reviews, paginate_reviews
from forum.models import Thread, Category
from forum.forms import ThreadForm
from django.db.models import Q
from django.http import JsonResponse


def index(request):
    category = Category.objects.all()
    binding = Thread.objects.all()
    contact_org = ContactOfOrganization.objects.all()
    company = Company.objects.all()
    company_services = Company.objects.get(id=1)
    company_all = company_services.typeofservices_set.all()
    context = {
        'company': company,
        'company_all': company_all,
        'contact': contact_org,
        'forum': category,
        'bind': binding
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
    category = Category.objects.all()
    services = TypeOfServices.objects.all()
    contact_org = ContactOfOrganization.objects.all()
    context = {
        'services': services,
        'contact': contact_org,
        'forum': category
    }
    return render(request, 'main/about.html', context)


def gallery(request):
    category = Category.objects.all()
    photo_list = PhotoOfWorks.objects.all()
    contact_org = ContactOfOrganization.objects.all()
    context = {
        'images': photo_list,
        'contact': contact_org,
        'forum': category
    }
    return render(request, 'main/gallery.html', context)


def add_favourite(request):
    if request.method == 'GET':
        image_id = request.GET.get('image_id')
        image = PhotoOfWorks.objects.get(id=image_id)
        if image.is_favourite:
            image.is_favourite = False
        else:
            image.is_favourite = True
        image.save()
        return JsonResponse({'success': True})


def favourite_images(request):
    images = PhotoOfWorks.objects.filter(is_favourite=True)
    context = {
        'images': images
    }
    return render(request, 'main/favourite_images.html', context)


@login_required(login_url='enter')
def calculate(request):
    if request.method == 'POST':
        category = Category.objects.all()
        contact_org = ContactOfOrganization.objects.all()
        # form = ContactForm(request.POST)
        form = ContactForm(request.POST, request.FILES)
        name = request.POST['name']
        content = request.POST['content']
        email = request.POST['email']
        files = request.FILES.getlist('file')
        body = {
            'name': name,
            'email': email,
            'content': content,

        }
        message = '\n'.join(body.values())
        msg = EmailMessage(name, message, settings.EMAIL_HOST_USER, [email])
        for f in files:
            msg.attach(f.name, f.read(), f.content_type)  #
        msg.send()
        context = {
            'form': form,
            'contact': contact_org,
            'forum': category
        }
        messages.success(request, 'Сообщение было отправлено')
        return render(request, 'main/calculate.html', context)

        # else:
        # return render(request, 'main/calculate.html', {'form': form, 'success': 'Повторите отправку'})
    else:
        category = Category.objects.all()
        contact_org = ContactOfOrganization.objects.all()
        form = ContactForm()
        context = {
            'form': form,
            'contact': contact_org,
            'forum': category
        }
        return render(request, 'main/calculate.html', context)


def reviews(request):
    reviews_all, search_query, info = search_reviews(request)
    custom_range, reviews_all = paginate_reviews(request, reviews_all, 3)
    category = Category.objects.all()
    contact_org = ContactOfOrganization.objects.all()
    context = {
        'reviews': reviews_all,
        'contact': contact_org,
        'forum': category,
        'search_query': search_query,
        'custom_range': custom_range,
        'info': info
    }
    return render(request, 'main/reviews.html', context)


def contact(request):  # функция отправки сообщения на почту
    if request.method == 'GET':
        category = Category.objects.all()
        contact_org = ContactOfOrganization.objects.all()
        form = SendMessageForm()
        context = {
            'form': form,
            'contact': contact_org,
            'forum': category,
        }
        return render(request, 'main/contact.html', context)
    else:
        form = SendMessageForm()
        category = Category.objects.all()
        contact_org = ContactOfOrganization.objects.all()
        name = request.POST['name']
        organization = request.POST['organization']
        email_from = settings.EMAIL_HOST_USER
        email = request.POST['email']
        content = request.POST['content']
        msg = EmailMessage(name, content, email, [email_from])  # name,
        msg.send()
        messages.success(request, 'Сообщение было отправлено')
        context = {
            'form': form,
            'contact': contact_org,
            'forum': category,
        }
        return render(request, 'main/contact.html', context)


def enter(request):
    if request.method == 'GET':  # при методе GET возвращаем страницу с формой регистрации
        contact_org = ContactOfOrganization.objects.all()
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
            return redirect('index')


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
    category = Category.objects.all()
    if request.method == 'GET':
        custom = request.user
        if request.user.is_authenticated:
            if custom.pricingandsummworks_set.all().count() < 1:
                form = ListOfWorksForm()
                obj = ListOfWorks.objects.all()
                context = {
                    'form': form,
                    'obj': obj,
                    'contact': contact_org,
                    'forum': category
                }
                return render(request, 'main/calculate_table.html', context)
            else:
                category = Category.objects.all()
                form = ListOfWorksForm()
                obj = ListOfWorks.objects.all()
                context = {
                    'form': form,
                    'obj': obj,
                    'contact': contact_org,
                    'forum': category
                }
                messages.info(request, 'Удалите все расчёты в личном кабинете')
                return render(request, 'main/calculate_table.html', context)
        else:
            messages.info(request, 'форма для незарегистрированных пользователей')
            category = Category.objects.all()
            form = ContactForm()
            obj = ListOfWorks.objects.all()
            context = {
                'form': form,
                'obj': obj,
                'contact': contact_org,
                'forum': category
            }
            return render(request, 'main/calculate.html', context)
    else:
        custom = request.user
        if request.user.is_authenticated and custom.pricingandsummworks_set.all().count() >= 1:
            category = Category.objects.all()
            form = ListOfWorksForm()
            obj = ListOfWorks.objects.all()
            context = {
                'form': form,
                'obj': obj,
                'contact': contact_org,
                'forum': category
            }
            messages.info(request, 'Удалите все расчёты в личном кабинете')
            return render(request, 'main/calculate_table.html', context)
        else:
            cost = cost_works(request)  # функция расчёта стоимости работ находится в utils.py
            category = Category.objects.all()
            obj = ListOfWorks.objects.all()
            form = ContactForm()
            messages.info(request, 'Расчёт был посчитан')
            context = {
                'form': form,
                'obj': obj,
                'contact': contact_org,
                'forum': category
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
                    phone_num = request.user.profileuser.phone_number
                    if phone_num:
                        phone = '\n' + 'Контактный номер: ' + str(phone_num)
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
                        messages.info(request, 'для отправки необходим номер телефона')
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
        elif request.POST.get('forum'):  # создание ветки на форуме
            custom = request.user
            if custom.thread_set.all().count() < 1:
                category = ThreadForm(request.POST)
                if category.is_valid():
                    thread = category.save(commit=False)
                    thread.author = custom
                    thread.save()
                    messages.info(request, 'Раздел был создан можете перейти к обсуждению')
                context = personal_view(request, pk=custom.id)
                return render(request, 'main/personal_account.html', context)
            else:
                messages.info(request, 'Пользователь может создать один форум')
                context = personal_view(request, pk=custom.id)
                return render(request, 'main/personal_account.html', context)
        else:
            form = UserForm(request.POST, instance=request.user)  # записываем все данные из User в форму
            # также поля из БД Profile
            form_profile = ProfileUserForm(request.POST, request.FILES, instance=request.user.profileuser)
            if form.is_valid():
                custom = request.user
                form_profile.save()
                form.save()  # сохраняем изменения в БД User
                messages.success(request, 'Профиль был успешно изменён')
                # остаёмся на той же странице с отредактированным профилем
                context = personal_view(request, pk)
                return render(request, 'main/personal_account.html', context)
            else:
                #  raise ValueError('ошибка ввода номера')
                messages.info(request, 'неправильный формат номера телефона')
                context = personal_view(request, pk)
                return render(request, 'main/personal_account.html', context)

        context = personal_view(request, pk)
        return render(request, 'main/personal_account.html', context)


def write_reviews(request):
    contact_org = ContactOfOrganization.objects.all()
    category = Category.objects.all()
    if request.method == 'GET' and request.user.is_authenticated:
        custom = request.user
        count_reviews = Review.objects.filter(owner=custom).count()
        if count_reviews < 1:
            u_form = ReviewForm()
            context = {
                'form': u_form,
                'count': count_reviews,
                'forum': category
            }
            messages.info(request, 'Оставить отзыв можно только один раз')
            return render(request, 'main/form_reviews.html', context)
        else:
            category = Category.objects.all()
            u_form = ReviewForm()
            context = {
                'form': u_form,
                'count': count_reviews,
                'contact': contact_org,
                'forum': category
            }
            messages.info(request, 'Вы оставили отзыв, эта форма заполнения вам недоступна')
            return render(request, 'main/form_reviews.html', context)
    else:
        if request.user.is_authenticated:
            category = Category.objects.all()
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
                context = {
                    'form': u_form,
                    'contact': contact_org,
                    'forum': category
                }
                return render(request, 'main/form_reviews.html', context)


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


def price_list(request):
    dismantling = ApartmentPrice.objects.filter(Q(title__startswith='Стен') | Q(title__icontains='демонтаж'))
    putty = ApartmentPrice.objects.filter(title__startswith='Штукатурка')
    context = {
        'dismantling': dismantling,
        'putty': putty
    }
    return render(request, 'main/prise_list.html', context)
