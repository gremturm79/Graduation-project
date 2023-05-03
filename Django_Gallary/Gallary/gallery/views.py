from django.shortcuts import render
from .models import Gallery


def index(request):
    images = Gallery.objects.all()
    context = {
        'images': images
    }
    return render(request, 'index.html', context)


def base(request):
    images = Gallery.objects.all()
    context = {
        'images': images
    }
    return render(request, 'base.html', context)
