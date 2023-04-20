from django.shortcuts import render
from .models import Apartments, ApartmentType


def repair_of_apartments(request):
    apartment = Apartments.objects.all()[0:3]
    works = ApartmentType.objects.all()
    context = {
        'apartment': apartment,
        'works': works
    }
    return render(request, 'repair_of_apartments/index.html', context)


def apartment_gallery(request):
    apartment_photo = Apartments.objects.all()
    context = {
        'images': apartment_photo
    }
    return render(request, 'repair_of_apartments/apartment_gallery.html', context)
