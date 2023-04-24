from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):  # модель не используется
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    url_menu = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PhotoOfWorks(models.Model):  # модель для хранения фотографий выполненных работ
    '''
    Класс PhotoOfWorks имеет 3 установленных поля: title - определение вида работ, image - фотография выполненных работ,
    time - дата сохранения файла.
    '''
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='gallery/')  # в корневой директории создастся папка media в ней создастся
    # папка gallery, в которой будут храниться загруженные админом фотографии
    time = models.DateTimeField(auto_now_add=True)

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
        return self.title


class CalculateTableEx(models.Model):  # модель для подсчёта стоимости работ
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)  # заголовок таблицы
    dismantling = models.IntegerField()  # название работы
    montage = models.IntegerField()
    plaster = models.IntegerField()
    putty = models.IntegerField()

    def __str__(self):
        return self.title


class ListOfWorks(models.Model):
    title = models.TextField(max_length=100)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.title


class ContactOfOrganization(models.Model):
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)


