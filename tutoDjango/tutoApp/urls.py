from django.urls import path
from . import views

urlpatterns = [
    path('Appview', views.index, name='index'),
]
