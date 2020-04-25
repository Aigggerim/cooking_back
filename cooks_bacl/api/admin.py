from django.contrib import admin

# Register your models here.
from api.models import Recipe, Cook, Comment
admin.site.register(Recipe)
admin.site.register(Cook)
admin.site.register(Comment)

