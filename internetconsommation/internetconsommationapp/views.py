from django.shortcuts import render
from .models import InternetConsumption

# Create your views here.

def search(request):
    consommations = InternetConsumption.objects.all()
    consommations_totals_sorted = list()
    consommations_total = list()

    for consommation in consommations: 
        consommations_total.append([consommation.user.username, (round(((consommation.upload + consommation.download)*0.000001), 2))])

    # for user, consommation in consommations_total:
    #     if consommations_total.count(user) > 1:
    #         consommations_totals_sorted.append([user, sum(consommation)])
    #     else:
    #         consommations_totals_sorted.append([user, consommation])


    for i in range(len(consommations_total)):
        if consommations_total[i-1][0] == consommations_total[i][0]:
            consommations_totals_sorted.append([consommations_total[i][0], (consommations_total[i][1] + consommations_total[i+1][1])])
        else:
            consommations_totals_sorted.append([consommations_total[i][0], consommations_total[i][1]])

            
    #defines what happens when there is a GET request
    if request.method == "GET":
        username = request.GET.get("q")
        return render(request,'home.html', { 'username' : username ,'consommations_totals_sorted':consommations_totals_sorted})

    #defines what happens when there is a POST request
    else:   
        return render(request,'home.html')