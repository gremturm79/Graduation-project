# Generated by Django 4.1.7 on 2023-04-16 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_1', '0005_listofworks'),
        ('renovation_bathroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BathRoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binding', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_1.typeofservices')),
            ],
        ),
    ]
