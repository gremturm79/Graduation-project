from django.forms import ModelForm
from .models import Projects
from django import forms  # импортируем модуль forms для изменения типа данных поля tags


class ProjectForm(ModelForm):
    class Meta:
        model = Projects # model, fields служебные переменные
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        widgets = {'tags': forms.CheckboxSelectMultiple()}  # меняем тип данных

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'input'})

#  self.fields['description'].widget.attrs.update({'class': 'input'})  # обновление и добавления аттрибутам
