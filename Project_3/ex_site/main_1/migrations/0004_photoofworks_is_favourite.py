# Generated by Django 4.1.7 on 2023-05-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_1', '0003_apartmentprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoofworks',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
