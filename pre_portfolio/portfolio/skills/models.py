from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skills/images/') # путь загрузки файлов если папки нет то она создастся
    url = models.URLField(blank=True)


class Social(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/images/') # путь загрузки файлов если папки нет то она создастся
    url = models.URLField(blank=True)

