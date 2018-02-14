from django.contrib import admin
from .models import Fiche, Client, Format

admin.site.register(Fiche)
admin.site.register(Client)
admin.site.register(Format)