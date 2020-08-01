from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'bootstrap/home.html')

def contact(request):
    return render(request, 'bootstrap/contact.html')

def grocery_list(request):
    return render(request, 'bootstrap/grocery_list.html')

