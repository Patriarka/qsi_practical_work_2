from django.urls import path
from . import views

urlpatterns = [
    path('', views.operacao, name='operacao'),
]