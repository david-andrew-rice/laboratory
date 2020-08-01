from django.urls import path
from . import views

appname='blog'

urlpatterns = [
    path('', views.home, name='blog-home'), # used 'blog-home' for more descriptive naming 
]

