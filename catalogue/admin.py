from django.contrib import admin
from .models import Game, Publisher, Category, Review

# Registrace modelů do administrace
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'publisher')
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'author', 'created_at')
    # Redaktor uvidí v adminu jen recenze, které napsal (volitelné)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Publisher)
admin.site.register(Category)