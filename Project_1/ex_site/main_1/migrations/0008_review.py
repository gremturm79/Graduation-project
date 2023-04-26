# Generated by Django 4.1.7 on 2023-04-26 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_1', '0007_profileuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='reviews/default_review.png', upload_to='reviews/')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1 - плохо'), (2, '2 - удовлетворительно'), (3, '3 - хорошо'), (4, '4 - очень хорошо'), (5, '5 - отлично')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
