from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name= 'Home'),
    path('about/', views.about, name= 'About'),
    path('contact/', views.contact, name= 'Contact'),
]
