from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Validace roku - nechceme nesmysly
def validate_year(value):
    if value < 1900 or value > 2026:
        raise ValidationError(f'{value} není platný rok vydání.')

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Vydavatel"
        verbose_name_plural = "Vydavatelé"

    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorie"

    def __str__(self): return self.name

class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název hry")
    description = models.TextField(
        verbose_name="Popis", 
        validators=[MinLengthValidator(10, message="Popis musí mít alespoň 10 znaků.")]
    )
    release_year = models.IntegerField(verbose_name="Rok vydání", validators=[validate_year])
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='game_covers/', blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name = "Hra"
        verbose_name_plural = "Hry"

    def __str__(self): return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Text recenze")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Recenze"
        verbose_name_plural = "Recenze"

    def __str__(self):
        return f"Recenze na {self.game.title} od {self.author.username}"