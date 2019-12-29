from django.db import models

class Gosc(models.Model):

    class Meta:
        verbose_name = "Gość"
        verbose_name_plural = "Goście"

    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    telefon_komorkowy = models.IntegerField()
    telefon_stacjonarny = models.IntegerField()
    branza = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    nazwa_firmy = models.CharField(max_length=200)

    def __str__(self):
        return self.nazwa_firmy




