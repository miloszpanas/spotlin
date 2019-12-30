from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Branza(models.Model):

    class Meta:
        verbose_name = "Branża"
        verbose_name_plural = "Branże"

    nazwa_branzy = models.CharField("nazwa branży", max_length=200)
    aktywna = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa_branzy

class Gosc(models.Model):

    class Meta:
        verbose_name = "Gość"
        verbose_name_plural = "Goście"

    imie = models.CharField("imię", max_length=200)
    nazwisko = models.CharField(max_length=200)
    telefon_komorkowy = models.CharField("telefon komórkowy", max_length=20)
    telefon_stacjonarny = models.CharField(max_length=20)
    branza = models.ForeignKey(Branza, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    nazwa_firmy = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa_firmy




class Specjalizacja(models.Model):

    class Meta:
        verbose_name = "Specjalizacja"
        verbose_name_plural = "Specjalizacje"

    nazwa = models.CharField(max_length=100)
    branza = models.ForeignKey(Branza, on_delete=models.CASCADE)
    aktywna = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa

class TypSpotkania(models.Model):

    class Meta:
        verbose_name = "Typ spotkania"
        verbose_name_plural = "Typy spoktania"

    typ_spotkania = models.CharField(max_length=200)

    def __str__(self):
        return self.typ_spotkania

class Spotkanie(models.Model):

    class Meta:
        verbose_name = "Spotkanie"
        verbose_name_plural = "Spotkania"

    data = models.DateTimeField(default=timezone.now)
    obecnosc = models.BooleanField("obecność" ,default=False)
    typ_spotkania = models.ForeignKey(TypSpotkania, on_delete=models.CASCADE)

    def __str__(self):
        return self.typ_spotkania



