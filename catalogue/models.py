from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Název vydavatele/studia")
    website = models.URLField(blank=True, null=True, verbose_name="Webová stránka")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kategorie/Žánr")

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název hry")
    description = models.TextField(verbose_name="Popis hry")
    release_year = models.IntegerField(verbose_name="Rok vydání", null=True, blank=True)

    # Vztah 1:N (Jedna hra má jednoho vydavatele, vydavatel má více her)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="Vydavatel")

    # Vztah M:N (Hra může mít více žánrů, žánr má více her)
    categories = models.ManyToManyField(Category, verbose_name="Kategorie")

    def __str__(self):
        return self.title
