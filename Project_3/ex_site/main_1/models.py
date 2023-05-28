from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class PhotoOfWorks(models.Model):  # модель для хранения фотографий выполненных работ
    '''
    Класс PhotoOfWorks имеет 3 установленных поля: title - определение вида работ, image - фотография выполненных работ,
    time - дата сохранения файла.
    '''
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='gallery/')  # в корневой директории создастся папка media в ней создастся
    # папка gallery, в которой будут храниться загруженные админом фотографии
    time = models.DateTimeField(auto_now_add=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Company(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=4000)

    def __str__(self):
        return f'{self.title}'


class TypeOfServices(models.Model):  # модель видов предоставляемых услуг на сайте
    '''
    Класс TypeOfServices имеет 3 установленных поля: title - тип предоставляемой услуги, description - описание
    предоставляемого типа работ, services_image - внешний ключ типа один ко многим для связи с полями
    класса PhotoOfWorks
    '''
    title = models.CharField(max_length=250)  # название предоставляемых услуг
    description = models.TextField(max_length=3000)  # описание предоставляемых услуг
    services_image = models.ForeignKey(PhotoOfWorks, on_delete=models.CASCADE, null=True, blank=True)  # связь с
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    # фотографиями работ

    def __str__(self):
        return self.title


class CalculateTable(models.Model):  # модель не применяется
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    dismantling = models.IntegerField()  # название работы
    montage = models.IntegerField()
    plaster = models.IntegerField()
    putty = models.IntegerField()

    def __str__(self):
        return f'{self.user}'


class CalculateTableEx(models.Model):  # модель для подсчёта стоимости работ, работает с
    # формой заполняется из админки один раз ???
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # title = models.IntegerField(default=100) # заголовок таблицы
    dismantling = models.IntegerField()  # название работы
    montage = models.IntegerField()
    plaster = models.IntegerField()
    putty = models.IntegerField()

    def __str__(self):
        return f'{self.owner}'


class ListOfWorks(models.Model):
    title = models.TextField(max_length=100)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.title


class ContactOfOrganization(models.Model):
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.address}'


class ProfileUser(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='profile/', default='profile/default.png')
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return f'{self.owner} ProfileUser'  # передаёт username


RATING = [
    (1, '1 - плохо'),
    (2, '2 - удовлетворительно'),
    (3, '3 - хорошо'),
    (4, '4 - очень хорошо'),
    (5, '5 - отлично')

]


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='reviews/', default='reviews/default_review.jpg')
    rating = models.PositiveSmallIntegerField(choices=RATING)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner}'

    def get_rating(self):
        rating = self.rating  # сохраняем в переменную значение рейтинга
        rate = [i for i in range(rating)]  # создаём список с количеством элементов равным рейтингу
        return rate

    class Meta:
        ordering = ['-rating', '-date']


class SummOfWorks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    summ = models.IntegerField(blank=True, null=True)
    # description = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner}'


class PricingAndSummWorks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    estimate = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner}'


class ApartmentPrice(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
