from django.shortcuts import render
from main_1.models import PhotoOfWorks, TypeOfServices
from .models import BathRoom, BathRoomType


def renovation_bathroom(request):
    photo = PhotoOfWorks.objects.all()
    bathroom = BathRoom.objects.all()[:3]
    works = BathRoomType.objects.all()
    context = {
        'bathroom': bathroom,
        'works': works,
        'photo': photo
    }
    return render(request, 'renovation_bathroom/index.html', context)


def gallery(request):
    bath_images = BathRoom.objects.all()  # получаем поле binding с модели BathRoom, которое имеет связь через ForeignKey
    # с классом PhotoOfWorks и в bathroom_gallery.html выводим фотографии из этого класса
    context = {
        'images': bath_images
    }
    return render(request, 'renovation_bathroom/bathroom_gallery.html', context)
