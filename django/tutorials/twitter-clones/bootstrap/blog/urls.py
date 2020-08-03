from django.urls import path
from . import views

appname = 'blog'

urlpatterns = [
    path('', views.home, name='blog-home'), # named 'blog-home' prevent naming collision
    path('about/', views.about, name='blog-about'), # trailing slash will get redirected
]
