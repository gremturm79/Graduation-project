from django.shortcuts import render, redirect
from .models import PhotoOfWorks, TypeOfServices, ListOfWorks, ContactOfOrganization, SummOfWorks, Review, Company
# UserCreationForm импорт формы которая создаёт пользователя
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ContactForm, UserForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ListOfWorksForm, SendMessageForm, ProfileUserForm, ReviewForm, CalculateTableExForm

from django.contrib import messages


def index(request):
    company = Company.objects.all()
    company_services = Company.objects.get(id=1)
    company_all = company_services.typeofservices_set.all()
    context = {
        'company': company,
        'company_all': company_all
    }
    return render(request, 'main/index.html', context)


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
    # author = User.objects.filter(first_name='Grems')[0]
    # review = Review.objects.filter(owner=author)  # находим данные из БД Review по имени автора статьи
    reviews_all = Review.objects.all()
    context = {
        'reviews': reviews_all,
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
        return render(request, 'main/enter.html', {'form': UserCreationForm()})
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
                return render(request, 'main/enter.html', {'form': UserCreationForm(),
                                                           'error': 'Такое имя пользователя существует выберите другое'})
        else:
            return render(request, 'main/enter.html', {'form': UserCreationForm(),
                                                       'error': 'Пароли не совпадают'})


def logout_user(request):
    logout(request)
    messages.info(request, 'Вы вышли из сессии')
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


@login_required()
def delete_user(request):
    custom = request.user
    if request.method == 'GET':
        return render(request, 'main/delete.html')
    else:
        custom.delete()
        messages.info(request, 'Аккаунт был успешно удалён')
        return redirect('about')


@login_required(login_url='enter')
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
        text_pricing = []

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
            lst_title = []

            for i in pricing:
                lst_pricing.append(i.price)  # в пустой список заносим данные поля price
                lst_title.append(i.title)  # составляем список из названия работ
            if squares:  # если список
                for j in range(len(squares)):  # проходим по его списку
                    if all_square[j].isdigit():  # если это цифры, берём элемент по этому индексу из списка lst_pricing
                        total = int(lst_pricing[j]) * int(squares[j])
                        text_pricing.append(lst_title[j])
                        text_pricing.append(squares[j])
                        summ += total

            return summ

        print(text_pricing)
        summ_works = SummOfWorks(summ=total_summ(obj, all_square))
        # заносим данные в модель SummOfWorks вернувшиеся из функции total_summ, а именно итоговая сумма за работу
        summ_works.owner = request.user  # устанавливаем связь двух БД
        summ_works.save()  # сохраняем в БД экземпляр класса с его данными
        messages.info(request, 'Расчёт произведён можете посмотреть в Личном кабинете')
        context = {
            'form': form,
            'obj': obj,
            'summ': summ
        }

        return render(request, 'main/calculate_table.html', context)


def personal_account(request, pk):  # функция представления личного кабинета
    if request.method == 'GET':

        if request.user.is_authenticated:  # если зарегистрирован пользователь

            images = request.user.profileuser  # извлекаем фотографию профиля
            review = ReviewForm()  # форма отправки отзыва об услугах
            image = images.image
            custom = request.user
            summ_works = custom.summofworks_set.all()
            form_profile = ProfileUserForm()  # поле для изменения фотографии
            form = UserForm(instance=custom)  # заполняем поля формы редактирования, данными из БД User
            date = User.objects.get(id=pk)  # получаем данные из БД User для заполнения карточки пользователя
            context = {
                'user': date,
                'form': form,
                'image': image,
                'profile_image': form_profile,
                'review': review,
                'summa': summ_works
            }
            return render(request, 'main/personal_account.html', context)
        else:  # иначе переход на страницу авторизации
            messages.warning(request, 'Необходимо авторизация или регистрация')
            return redirect('login')

    else:  # если метод POST отрабатывает форма редактирования данных пользователя
        form = UserForm(request.POST, instance=request.user)  # записываем все данные из User в форму
        form_profile = ProfileUserForm(request.POST, request.FILES, instance=request.user.profileuser)
        if form.is_valid():
            form_profile.save()
            form.save()  # сохраняем изменения в БД User
            messages.success(request, 'Профиль был успешно изменён')
            # остаёмся на той же странице с отредактированным профилем
            images = request.user.profileuser
            image = images.image
            custom = request.user
            form = UserForm(instance=custom)  # заполняем поля формы редактирования, данными из БД User
            date = User.objects.get(id=pk)  # получаем данные из БД User для заполнения карточки пользователя
            context = {
                'user': date,
                'form': form,
                'image': image,
                'form_profile': form_profile,
            }
            return render(request, 'main/personal_account.html', context)


def write_reviews(request):  # метод для отзывов пока не реализован
    if request.method == 'GET':
        if request.user.is_authenticated:
            count = request.user.review_set.count()
            messages.info(request, 'Вы уже оставили отзыв, второй раз невозможно это сделать')
            u_form = ReviewForm()
            return render(request, 'main/form_reviews.html', {'form': u_form, 'count': count})
        else:
            messages.error(request, 'Для отзыва необходимо авторизация')
            return redirect('enter')
    else:
        if request.user.is_authenticated:
            count = request.user.review_set.count()
            review_date = ReviewForm(request.POST, request.FILES)
            if review_date.is_valid() and count < 1:
                res = review_date.save(commit=False)
                # привязываем пользователя написавшего отзыв к самому отзыву, через связь Foreignkey
                res.owner = request.user
                res.save()
                messages.success(request, 'Отзыв был успешно добавлен')
                return redirect('reviews')
            else:
                count = request.user.review_set.count()
                u_form = ReviewForm()
                messages.info(request, 'Вы уже оставили отзыв, второй раз невозможно это сделать')
                return render(request, 'main/form_reviews.html', {'form': u_form, 'count': count})


def calculate_personal(request):
    if request.method == 'GET':
        form = CalculateTableExForm()
        context = {
            'form': form
        }
        return render(request, 'main/calculate-personal.html', context)
    else:
        form = CalculateTableExForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.owner = request.user
            res.save()
            custom = request.user
            total = custom.calculatetableex_set.all()[0:2]
            messages.info(request, 'Расчёт произведён можете посмотреть в Личном кабинете')
            context = {
                'form': form,
                'total': total
            }
            return render(request, 'main/calculate-personal.html', context)


def carousel(request):
    photo_list = PhotoOfWorks.objects.all()
    context = {
        'images': photo_list
    }
    return render(request, 'main/carousel.html', context)


def delete_calculate(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated:  # если зарегистрирован пользователь
            images = request.user.profileuser  # извлекаем фотографию профиля
            review = ReviewForm()  # форма отправки отзыва об услугах
            image = images.image
            custom = request.user
            summ_works = custom.summofworks_set.all()
            form_profile = ProfileUserForm()  # поле для изменения фотографии
            form = UserForm(instance=custom)  # заполняем поля формы редактирования, данными из БД User
            date = User.objects.get(id=pk)  # получаем данные из БД User для заполнения карточки пользователя
            context = {
                'user': date,
                'form': form,
                'image': image,
                'profile_image': form_profile,
                'review': review,
                'summa': summ_works
            }
            return render(request, 'main/personal_account.html', context)
        else:  # иначе переход на страницу авторизации
            messages.warning(request, 'Необходимо авторизация или регистрация')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            images = request.user.profileuser  # извлекаем фотографию профиля
            review = ReviewForm()  # форма отправки отзыва об услугах
            image = images.image
            custom = request.user
            summ_works = custom.summofworks_set.all()
            form_profile = ProfileUserForm()  # поле для изменения фотографии
            form = UserForm(instance=custom)  # заполняем поля формы редактирования, данными из БД User
            date = User.objects.get(id=pk)  # получаем данные из БД User для заполнения карточки пользователя
            context = {
                'user': date,
                'form': form,
                'image': image,
                'profile_image': form_profile,
                'review': review,
                'summa': summ_works
            }
            custom = request.user
            del_calculate = SummOfWorks.objects.filter(owner=custom)
            #  удаление всех экземпляров класса у одного пользователя
            del_calculate.delete()
            messages.info(request, 'Расчёт был удалён можете сделать расчёт повторно')
            return render(request, 'main/personal_account.html', context)


