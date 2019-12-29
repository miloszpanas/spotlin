from django.contrib import admin
from .models import Gosc, Branza, Spotkanie, Specjalizacja, TypSpotkania

admin.site.register(Gosc)
admin.site.register(Branza)
admin.site.register(Spotkanie)
admin.site.register(Specjalizacja)
admin.site.register(TypSpotkania)