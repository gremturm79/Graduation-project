import requests
from .forms import ReviewForm, ProfileUserForm, UserForm, ListOfWorksForm, ApartmentPriceForm
from django.contrib.auth.models import User
from .models import PricingAndSummWorks, SummOfWorks, ListOfWorks, ContactOfOrganization, Review, ImageFavorite, \
    ApartmentPrice
from forum.forms import ThreadForm
from forum.models import Thread, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages


def send_message(message):  # функция отправки расчёта заказчику
    token = ''  # @zakaz_cena_bot
    chat_id = ''
    # message = 'Отправка сообщения'
    # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates" запрос всех данных
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()


def personal_view(request, pk):  # функция отображения данных профиля
    custom = request.user
    if custom.pricingandsummworks_set.filter(owner=custom).exists():
        binding = Thread.objects.all()
        prof = request.user.profileuser  # извлекаем данные профиля
        review = ReviewForm()  # форма отправки отзыва об услугах
        category_thread = ThreadForm()  # импорт из приложения forum формы модели Thread
        category = Category.objects.all()  # Category модель категории форума
        forum_branch = Thread.objects.filter(author=custom)
        forum_count = forum_branch.count()
        display = 'flex'  # избранные фотографии
        image = prof.image
        phone = prof.phone_number
        contact_org = ContactOfOrganization.objects.all()
        images_favorite = ImageFavorite.objects.filter(owner=custom)
        form_profile = ProfileUserForm(instance=prof)  # поле для изменения данных Бд Profile
        message_view = custom.pricingandsummworks_set.get()
        summ_personal = custom.summofworks_set.all()
        count_summ = custom.summofworks_set.all()
        count = len(count_summ)  # количество расчётов в у пользователя
        form = UserForm(instance=custom)  # заполняем поля формы редактирования, данными из БД User
        date = User.objects.get(id=pk)  # получаем данные из БД User для заполнения карточки пользователя
        context = {
            'user': date,
            'form': form,
            'image': image,
            'phone': phone,
            'profile': form_profile,
            'review': review,
            'summa': summ_personal,
            'summ_count': count,
            'message_view': message_view,
            'contact': contact_org,
            'category': category_thread,
            'forum': category,
            'bind': binding,
            'branch': forum_branch,
            'images_favorite': images_favorite,
            'display': display
        }
        return context
    else:
        contact_org = ContactOfOrganization.objects.all()
        prof = request.user.profileuser  # извлекаем фотографию профиля
        binding = Thread.objects.all()
        review = ReviewForm()  # форма отправки отзыва об услугах
        category_thread = ThreadForm()  # импорт из приложения forum формы модели Thread
        forum_branch = Thread.objects.filter(author=custom)
        images_favorite = ImageFavorite.objects.filter(owner=custom)
        forum_count = forum_branch.count()
        display = 'flex'  # избранные фотографии
        phone = prof.phone_number
        image = prof.image
        form_profile = ProfileUserForm(instance=prof)  # поле для изменения данных
        # message_view = custom.pricingandsummworks_set.get(owner=pk)
        summ_personal = custom.summofworks_set.all()
        count_summ = custom.summofworks_set.all()
        count = len(count_summ)  # количество расчётов в у пользователя
        form = UserForm(instance=custom)  # заполняем поля формы редактирования, данными из БД User
        date = User.objects.get(id=pk)  # получаем данные из БД User для заполнения карточки пользователя
        context = {
            'user': date,
            'form': form,
            'image': image,
            'phone': phone,
            'profile': form_profile,
            'review': review,
            'summa': summ_personal,
            'summ_count': count,
            'contact': contact_org,
            'category': category_thread,
            'bind': binding,
            'branch': forum_branch,
            'images_favorite': images_favorite,
            'display': display
        }
        return context


def cost_works(request):
    custom = request.user
    obj = ListOfWorks.objects.all()  # данные из модели БД ListOfWorks
    all_square = request.POST.getlist('square')  # получаем список указанных площадей в теге input name="square"
    form = ListOfWorksForm()  # данные полей формы ListOfWorksForm для страницы  calculate_table.html
    summ = 0
    summ_send_telegram = []

    #  text_send_telegram = ''

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
            lst_title.append(i.title)
        if squares:  # если список
            for j in range(len(squares)):  # проходим по его списку
                if all_square[j].isdigit():  # если это цифры, берём элемент по этому индексу из списка lst_pricing
                    total = int(lst_pricing[j]) * int(squares[j])
                    summ_send_telegram.append(lst_title[j])
                    summ_send_telegram.append(' ' + squares[j] + 'm2')
                    summ_send_telegram.append(' ' + str(lst_pricing[j]) + ' ' + 'рублей' + '\n')
                    summ += total
        return summ, summ_send_telegram  # возвращает сумму и список площадей с ценами

    func_summ, description_works = total_summ(obj, all_square)
    text_send_telegram = 'От:' + ' ' + str(custom.first_name) + '\n' + ''.join(description_works) \
                         + 'Итоговая сумма: ' + str(func_summ) + ' ' + 'рублей'

    estimate_save = PricingAndSummWorks(owner=custom, estimate=text_send_telegram)
    estimate_save.save()
    count = custom.pricingandsummworks_set.all()  # count()  количество расчётов работ
    # пользователя
    for i in range(len(count)):
        print(count[i].estimate)

    summ_pricing = SummOfWorks(owner=custom, summ=func_summ)
    summ_pricing.save()
    context = {
        'form': form,
        'obj': obj,
        'summ': summ
    }
    return context


def paginate_reviews(request, reviews_all, results):
    page = request.GET.get('page', 1)
    # results = 2
    paginator = Paginator(reviews_all, results, allow_empty_first_page=True)
    reviews_all = paginator.get_page(page)
    left_index = int(page) - 2

    if left_index < 1:
        left_index = 1
    right_index = int(page) + 3
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
    custom_range = range(left_index, right_index)
    return custom_range, reviews_all


def search_reviews(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    message = Review.objects.filter(Q(name__iregex=search_query) | Q(description__iregex=search_query) |
                                    Q(rating__contains=search_query) | Q(date__iregex=search_query) |
                                    Q(owner__first_name__regex=search_query))
    info = True
    if not message.exists():
        message = Review.objects.all()
        info = messages.info(request, 'по запросу ничего не найдено')

    return message, search_query, info


def cost_works_apartments(request):
    custom = request.user
    obj = ApartmentPrice.objects.all()  # данные из модели БД ListOfWorks
    all_square = request.POST.getlist('square')  # получаем список указанных площадей в теге input name="square"
    check_all_square = set(all_square)
    if check_all_square == {''}:
        return 'ничего не выбрано'
    form = ApartmentPriceForm()  # данные полей формы ListOfWorksForm для страницы  calculate_table.html
    summ = 0
    summ_send_telegram = []

    #  text_send_telegram = ''

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
            lst_title.append(i.title)
        if squares:  # если список
            for j in range(len(squares)):  # проходим по его списку
                if all_square[j].isdigit():  # если это цифры, берём элемент по этому индексу из списка lst_pricing
                    total = int(lst_pricing[j]) * int(squares[j])
                    summ_send_telegram.append(lst_title[j])
                    summ_send_telegram.append(' ' + squares[j] + 'm2')
                    summ_send_telegram.append(' ' + str(lst_pricing[j]) + ' ' + 'рублей' + '\n')
                    summ += total
        return summ, summ_send_telegram  # возвращает сумму и список площадей с ценами
    # print(summ)
    func_summ, description_works = total_summ(obj, all_square)
    text_send_telegram = 'От:' + ' ' + str(custom.first_name) + '\n' + ''.join(description_works) \
                         + 'Итоговая сумма: ' + str(func_summ) + ' ' + 'рублей'

    estimate_save = PricingAndSummWorks(owner=custom, estimate=text_send_telegram)
    estimate_save.save()
    count = custom.pricingandsummworks_set.all()  # count()  количество расчётов работ
    # пользователя
    for i in range(len(count)):
        print(count[i].estimate)

    summ_pricing = SummOfWorks(owner=custom, summ=func_summ)
    summ_pricing.save()
    context = {
        'form': form,
        'obj': obj,
        'summ': summ
    }
    return context
