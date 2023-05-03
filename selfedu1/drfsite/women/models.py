from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=250)  # заголовок
    content = models.TextField(blank=True)  # описание
    time_create = models.DateTimeField(auto_now_add=True)  # создаёт метку при создании строки в базе
    time_update = models.DateTimeField(auto_now=True)  # обновляет метку при каждом обращении, изменение строки
    is_published = models.BooleanField(default=True)  # публикация
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # связь с моделью Category

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)

    def __str__(self):
        return self.name
