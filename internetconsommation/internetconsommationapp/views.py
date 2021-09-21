from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html')


def user_details(request):
    return render (request, 'user_details.html')