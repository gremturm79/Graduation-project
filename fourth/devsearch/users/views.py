from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
#  messages обработка сообщений для посетителей или клиентов сайта при обработке формы
# и других типов пользовательского ввода
from django.contrib import messages
# UserCreationForm класс для создания формы регистрации и записи в БД
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.contrib.auth.decorators import login_required
from .utils import search_profiles


def profiles(request):
    prof, search_query = search_profiles(request)

    context = {'profiles': prof, 'search_query': search_query}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)

    top_skill = prof.skill_set.exclude(description__exact='')  # исключит элементы пустые
    other_skill = prof.skill_set.filter(description='')  # взять все пустые элементы
    context = {'profile': prof, 'top_skill': top_skill, 'other_skill': other_skill}
    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)  # проверка на существование имени
        except ObjectDoesNotExist:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # аутентификация на сайте
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password incorrect')

    return render(request, 'users/login_register.html')


def logout_user(request):
    messages.info(request, 'User was logged out!')
    logout(request)
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()  # получаем доступ к форме UserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # собираем все данные из формы UserCreationForm
        if form.is_valid():
            user = form.save(commit=False)  # сохраняем данные в переменную
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was creator')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')  # переадресация незарегистрированного пользователя
def user_account(request):
    prof = request.user.profile
    skills = prof.skill_set.all()  # доступ к модели Skills через его Foreignkey
    projects = prof.projects_set.all()
    context = {
        'profile': prof,
        'skills': skills,
        'projects': projects
    }

    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile  # данные пользователя из модели Profile
    form = ProfileForm(instance=profile)  # передаём экземпляр класса Profile с его данными, заполненными в form
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {
        'form': form
    }
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)  # берём данные из модели Skill по id
    form = SkillForm(instance=skill)  # заполняем форму по умолчанию этими данными
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)  # берём данные из модели Skill по id
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')
    context = {'object': skill}
    return render(request, 'projects/delete.html', context)
