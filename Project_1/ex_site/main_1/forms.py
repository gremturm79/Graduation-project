from django import forms
from django.contrib.auth.models import User
from .models import CalculateTableEx, ListOfWorks
from django.forms import ModelForm


# import datetime


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250, label='Ваше имя:')  # disabled=True отключает поле
    email = forms.EmailField(max_length=250, label='Почтовый ящик:')
    content = forms.CharField(widget=forms.Textarea, label='Описание:')  # help_text='текст рядом с полем',
    # strip=True удаление начальных и конечных пробелов
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Загрузка файла:')
    # square = forms.DecimalField(max_value=1000, min_value=2, label='Укажите площадь помещения:')
    # CHOICES = (
    # ('Paris', 'France'),
    # ('Moscow', 'Russia'),
    # )
    # position = forms.ChoiceField(choices=CHOICES) choices именованный параметр для тега select в html

    # day = forms.DateField(initial=datetime.date.today) отдельное поле с датой на сегодня


class CalculateTableExForm(ModelForm):  # из django.forms наследуем родительский класс ModelForm для создания Form class
    class Meta:
        model = CalculateTableEx
        fields = ['dismantling', 'montage', 'plaster', 'putty']
        # labels переопределение названия полей
        labels = {'dismantling': 'Демонтаж', 'montage': 'Монтаж', 'plaster': 'Штукатурка', 'putty': 'Шпаклёвка'}


class ListOfWorksForm(ModelForm):
    square = forms.IntegerField(min_value=0, max_value=1000)

    class Meta:
        model = ListOfWorks
        fields = ['title', 'price']


class SendMessageForm(forms.Form):
    '''
    Класс SendMessageForm создаёт форму для отправки сообщения от клиента на странице contact.html
    '''
    name = forms.CharField(max_length=250, label='Ваше имя:')
    organization = forms.CharField(max_length=250, label='Название организации:')
    email = forms.EmailField(max_length=250, label='Почтовый ящик:')
    content = forms.CharField(widget=forms.Textarea, label='Текст сообщения:')


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']
