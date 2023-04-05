from django.shortcuts import render
from .models import Menu


def index(request):
    return render(request, 'main/index.html')


def main(request):
    return render(request, 'main/about.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def calculate(request):
    return render(request, 'main/calculate.html')


def reviews(request):
    return render(request, 'main/reviews.html')


def contact(request):
    return render(request, 'main/contact.html')


def enter(request):
    return render(request, 'main/enter.html')
