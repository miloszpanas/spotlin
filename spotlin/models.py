from django.db import models
from django.utils import timezone


class Gosc(models.Model):

    class Meta:
        verbose_name = "Gość"
        verbose_name_plural = "Goście"

    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    telefon_komorkowy = models.IntegerField()
    telefon_stacjonarny = models.IntegerField()
    branza = models.ForeignKey("spotlin.Branza", on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    nazwa_firmy = models.CharField(max_length=200)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa_firmy


class Branza(models.Model):

    class Meta:
        verbose_name = "Branża"
        verbose_name_plural = "Branże"

    nazwa_branzy = models.CharField(max_length=200)
    aktywna = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa_branzy


class Specjalizacja(models.Model):

    class Meta:
        verbose_name = "Specjalizacja"
        verbose_name_plural = "Specjalizacje"

    nazwa = models.CharField(max_length=100)
    branza = models.ForeignKey("spotlin.Branza", on_delete=models.CASCADE)
    aktywna = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa


class Spotkanie(models.Model):

    class Meta:
        verbose_name = "Spotkanie"
        verbose_name_plural = "Spotkania"

    data = models.DateTimeField(default=timezone.now)
    obecnosc = models.BooleanField(default=False)
    typ_spotkania = models.ForeignKey("spotlin.TypSpotkania", on_delete=models.CASCADE)

    def __str__(self):
        return self.typ_spotkania

class TypSpotkania(models.Model):

    class Meta:
        verbose_name = "Typ spotkania"
        verbose_name_plural = "Typy spoktania"

    typ_spotkania = models.CharField(max_length=200)

    def __str__(self):
        return self.typ_spotkania


