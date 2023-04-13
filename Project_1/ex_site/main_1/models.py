from django.db import models


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
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=3000)
    services_image = models.ForeignKey(PhotoOfWorks, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
