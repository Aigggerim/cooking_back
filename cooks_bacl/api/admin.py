from django.contrib import admin

# Register your models here.
from api.models import Recipe, Cook
admin.site.register(Recipe)
admin.site.register(Cook)
