from django.shortcuts import render
from .models import Skills, Social


def index(request):
    projects = Skills.objects.all()
    social = Social.objects.all()
    return render(request, 'skills/index.html', {'projects': projects, 'social': social})
