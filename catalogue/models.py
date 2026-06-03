from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator

# Funkce pro vlastní validaci roku (např. aby nebyl záporný a nebyl z budoucnosti)
def validate_year(value):
    if value < 1900 or value > 2026:
        raise ValidationError(f'{value} není platný rok vydání (zadej 1900-2026).')

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): return self.name

class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název hry")
    description = models.TextField(
        verbose_name="Popis",
        validators=[MinLengthValidator(10, message="Popis musí mít alespoň 10 znaků.")]
    )
    release_year = models.IntegerField(
        verbose_name="Rok vydání",
        validators=[validate_year] # Tady používáme náš vlastní validátor
    )
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='game_covers/', blank=True, null=True)

    def __str__(self): return self.title