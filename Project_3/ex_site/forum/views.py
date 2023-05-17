from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Thread, Reply
from .forms import ThreadForm, ReplyForm
from django.contrib import messages
from .utils import content


def index(request):
    if request.method == 'GET':
        message = Thread.objects.all()
        cat = Category.objects.all()
        context = {
            'category': cat,
            'message': message
        }
        return render(request, 'forum/index.html', context)


def forum(request, pk):
    if request.method == 'GET':
        context = content(request, pk)
        message = Thread.objects.get(id=pk)
        print(message)
        return render(request, 'forum/forum.html', context)
    else:
        custom = request.user
        # thread = get_object_or_404(Thread, pk=pk)
        message = Thread.objects.get(id=pk)
        # category = get_object_or_404(Category, pk=pk)
        context = content(request, pk)
        if request.POST.get('write'):  # открытие нового раздела
            if request.user.is_authenticated:
                form = ThreadForm(request.POST)
                if form.is_valid():
                    thread = form.save(commit=False)
                    # thread.category = category  # сохраняем категорию по pk
                    thread.author = custom  # сохраняем автор по user
                    thread.save()
                    return render(request, 'forum/forum.html', context)
                else:
                    return render(request, 'forum/forum.html', context)
            messages.info(request, 'Только для зарегистрированных пользователей')
            return render(request, 'forum/forum.html', context)
        if request.POST.get('reply'):  # сообщения по разделам
            if request.user.is_authenticated:
                custom = request.user
                form = ReplyForm(request.POST)
                if form.is_valid():
                    reply = form.save(commit=False)
                    reply.tread = message
                    reply.author = custom
                    reply.save()
                    return render(request, 'forum/forum.html', context)
                else:
                    return render(request, 'forum/forum.html', context)
            else:
                messages.info(request, 'Только для зарегистрированных пользователей')
                return render(request, 'forum/forum.html', context)
    return render(request, 'forum/forum.html', context)
