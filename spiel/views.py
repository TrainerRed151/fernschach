import json

from django.shortcuts import render, redirect
from spiel.models import Game, Player

# Create your views here.
def home(request):
    if request.method == 'POST':
        if not Game.objects.all().exists():
            white, _ = Player.objects.get_or_create(username='white', password='', salt='')
            black, _ = Player.objects.get_or_create(username='black', password='', salt='')
            Game.objects.create(white=white, black=black)

        game_id = Game.objects.all().last().id
        return redirect('game', game_id=game_id)

    return render(request, 'home.html', {})

def game(request, game_id):
    game = Game.objects.get(id=game_id)
    submitted = False

    if request.method == 'POST':
        game.history = f'{game.history},{request.POST["move"]}'
        game.save()
        submitted = True

    ctx = {
        'move_list': json.dumps(game.history.split(',')),
        'submitted': submitted,
    }

    return render(request, 'game.html', ctx)
