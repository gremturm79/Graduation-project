from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    url_menu = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PhotoOfWorks(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='gallery/')  # в корневой директории создастся папка media в ней создастся
    # папка gallery, в которой будут храниться загруженные админом фотографии
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.time}'
