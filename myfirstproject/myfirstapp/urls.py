from django.contrib import admin
from django.urls import path
from myfirstapp import views

urlpatterns = [
    path("", views.index, name='myfirstproject'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("addvehicle", views.addvehicle, name='addvehicle'),
    path("contact", views.contact, name='contact')
    

    
]

