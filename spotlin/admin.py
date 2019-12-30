from django.contrib import admin
from .models import Gosc, Branza, Spotkanie, Specjalizacja, TypSpotkania
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class GoscInline(admin.TabularInline):
    model = Gosc
    max_num = 1
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = [GoscInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Gosc)
admin.site.register(Branza)
admin.site.register(Spotkanie)
admin.site.register(Specjalizacja)
admin.site.register(TypSpotkania)