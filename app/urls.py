from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path("",views.index,name='home'),
    path("contact",views.contact,name='contact'),
    path("services",views.services,name='services'),
    path("home",views.home,name='home'),
    path("about",views.about, name='about'), 
    path("pricing",views.pricing,name='pricing'),
]
