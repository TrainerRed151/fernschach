from django.urls import path

from spiel.views import home, game

urlpatterns = [
    path('', home, name='home'),
    path('spiel/<int:game_id>/', game, name='game'),
]
