import requests
from .forms import ReviewForm, ProfileUserForm, UserForm, ListOfWorksForm
from django.contrib.auth.models import User
from .models import PricingAndSummWorks, SummOfWorks, ListOfWorks, ContactOfOrganization, ProfileUser


def send_message(message):  # функция отправки расчёта заказчику
    TOKEN = ""  # @zakaz_cena_bot
    CHAT_ID = ''
    # message = 'Отправка сообщения'
    # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates" запрос всех данных
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url).json()  # chat_id 899584907


def personal_view(request, pk):  # функция отображения данных профиля
    custom = request.user
    if custom.pricingandsummworks_set.filter(owner=custom).exists():
        prof = request.user.profileuser  # извлекаем данные профиля
        review = ReviewForm()  # форма отправки отзыва об услугах
        image = prof.image
        phone = prof.phone_number
        contact_org = ContactOfOrganization.objects.all()
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
            'contact': contact_org
        }
        return context
    else:
        contact_org = ContactOfOrganization.objects.all()
        prof = request.user.profileuser  # извлекаем фотографию профиля
        review = ReviewForm()  # форма отправки отзыва об услугах
        phone = prof.phone_number
        image = prof.image
        form_profile = ProfileUserForm(instance=prof)  # поле для изменения данных
        # message_view = custom.pricingandsummworks_set.get(owner=pk)
        summ_personal = custom.summofworks_set.all()
        count_summ = custom.summofworks_set.all()
        count = len(count_summ)  # количество расчётов в у пользователя
        form = UserForm(instance=custom)# заполняем поля формы редактирования, данными из БД User
        print(form)
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
            'contact': contact_org
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
    text_send_telegram = 'От:' + ' ' + str(custom) + '\n' + ''.join(description_works) \
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
