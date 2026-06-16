from django.shortcuts import render, get_object_or_404
from .models import Game, Category

def home(request):
    # Počítadlo pro hlavní stránku
    total_games = Game.objects.count()
    return render(request, 'catalogue/home.html', {'total_games': total_games})

def game_detail(request, pk):
    # Načtení konkrétní hry nebo chyba 404
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'catalogue/game_detail.html', {'game': game})

def game_list(request):
    # Získání filtru z URL
    category_name = request.GET.get('category')
    
    # Filtrování nebo zobrazení všeho
    if category_name:
        games = Game.objects.filter(categories__name=category_name)
    else:
        games = Game.objects.all()
    
    categories = Category.objects.all()
    
    # Správné uzavření renderu
    return render(request, 'catalogue/game_list.html', {
        'games': games,
        'categories': categories,
        'selected_category': category_name
    })