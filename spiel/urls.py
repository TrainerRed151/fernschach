from django.urls import path

from spiel.views import home

urlpatterns = [
    path('', home, name='home'),
]
