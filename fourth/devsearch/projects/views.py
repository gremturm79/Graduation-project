from django.shortcuts import render, redirect
from .models import Projects
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from .utils import search_projects


def projects(request):
    pr, search_query = search_projects(request)
    context = {
        'projects': pr,
        'search_query': search_query
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Projects.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': project_obj})


@login_required(login_url='login')  # запрет входа на страницу для незарегистрированных пользователей
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # request.FILES для получения медиа файлов
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'projects/form-template.html', context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # new_tags = request.POST.get('tags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()

        return redirect('account')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    if request.method == 'POST':
        project.delete()  # удаление объекта
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete.html', context)
