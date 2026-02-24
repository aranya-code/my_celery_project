from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name= 'Home'),
    path('about/', views.about, name= 'About'),
    path('contact/', views.contact, name= 'Contact'),
    path('task/<str:task_id>', views.check_result, name= 'check_result'),
]
