from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'bootstrap/home.html')

def contact(request):
    return HttpResponse('contact')

def grocery_list(request):
    return HttpResponse('grocery_list')

