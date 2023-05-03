from django.shortcuts import render
from .forms import StudentForm, Student


def home(request):
    form = StudentForm
    mydict = {
        'form': form
    }
    return render(request, 'index.html', context=mydict)
