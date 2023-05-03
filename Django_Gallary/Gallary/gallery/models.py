from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField()

    def __str__(self):
        return self.title
