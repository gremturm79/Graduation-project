from django.contrib import admin
from .models import Todo


# отображение поля из БД в админ странице
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)  # поле created с методом 'auto_now_add=True'


admin.site.register(Todo, TodoAdmin)
