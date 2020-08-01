from django.urls import path

from shortener import views

appname = 'shortener'

urlpatterns = [
    path('', views.submit_url, name='submit_url'),
]