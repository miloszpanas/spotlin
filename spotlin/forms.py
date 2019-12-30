from django.forms import ModelForm
from .models import Specjalizacja

class SpecjalizacjaForm(ModelForm):
    class Meta:
        model = Specjalizacja
        fields = "__all__"