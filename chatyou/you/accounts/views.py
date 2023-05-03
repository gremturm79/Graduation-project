from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
