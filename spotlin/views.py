from django.shortcuts import render
from .forms import SpecjalizacjaForm
from django.http import HttpResponse
from .models import Branza


def nowa_specjalizacja(request):
    if request.method == "POST":
        form = SpecjalizacjaForm(request.POST)
        if form.is_valid():
            specjalizacja = form.save()
            return HttpResponse('ok')
    else:
        form = SpecjalizacjaForm()
    context = {
      'form': form,
      'branze': Branza.objects.all()
    }
    return render(request, 'spotlin/nowa_specjalizacja.html', context)
