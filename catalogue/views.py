from django.shortcuts import render, get_object_or_404
from .models import Game

def home(request):
    total_games = Game.objects.count()
    return render(request, 'catalogue/home.html', {'total_games': total_games})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'catalogue/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'catalogue/game_detail.html', {'game': game})