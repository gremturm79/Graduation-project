# Generated by Django 4.1.7 on 2023-04-14 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_1', '0003_typeofservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='BathRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binding', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_1.photoofworks')),
            ],
        ),
    ]
