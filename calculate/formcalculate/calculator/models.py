from django.db import models


class ListOfWorks(models.Model):
    title = models.TextField(max_length=100)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.title
