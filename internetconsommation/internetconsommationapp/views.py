from django.shortcuts import render
from .models import InternetConsumption

# Create your views here.
def home(request):
    consommations = InternetConsumption.objects.all()
    consommations_total = list()

    for consommation in consommations:
        consommations_total.append([consommation.user.username, ((consommation.upload + consommation.download)*0.000001)])

    return render(request, 'home.html', {'consommations_total':consommations_total, 'consommations':consommations})