from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    url_menu = models.CharField(max_length=100)

    def __str__(self):
        return self.title

