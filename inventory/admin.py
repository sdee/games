from django.contrib import admin

# Register your models here.
from inventory.models import Game
from inventory.models import Genre

admin.site.register(Game)
admin.site.register(Genre) #form not user facing
