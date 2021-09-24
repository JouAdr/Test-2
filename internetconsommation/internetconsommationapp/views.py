from django.shortcuts import render
from .models import InternetConsumption
from django.contrib.auth.models import User

# Create your views here.

def search(request):
    consommations = InternetConsumption.objects.all()
    consommations_totals_sorted = []
    consommations_total = []
    consommations_user_name = []

    for consommation in consommations: 
        consommations_total.append([consommation.user.username, (round(((consommation.upload + consommation.download)*0.000001), 2))])
        consommations_user_name.append(consommation.user.username)

    consommations_user = list(set(consommations_user_name))

    #defines what happens when there is a GET request
    if request.method == "GET":
        username = request.GET.get("q")
        result = 0
        for user, consommation in consommations_total:
            if user == username:
                result = round((result + consommation ),2) 
                consommations_totals_sorted.append([user, result])
            else:
                consommations_totals_sorted.append([user, consommation])
        return render(request,'home.html', { 'username' : username ,'consommations_totals_sorted':consommations_totals_sorted, 'consommations_user':consommations_user})

    #defines what happens when there is a POST request
    else:   
        return render(request,'home.html')