from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.meaurements_view, name='measurements_view'),    
    path('<int:id>', views.measurement_view, name='measurement_view'),
]