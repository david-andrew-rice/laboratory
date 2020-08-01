from django.shortcuts import render
from django.http import HttpResponseRedirect

def submit_url(request):
    return render(request, 'shortener/index.html')

# def redirect_user(request):
#     return render(request, 'shortener/redirect.html')
