from django.contrib import admin
from .models import Game, Playing, Toy 

# Register your models here 
admin.site.register(Game)
admin.site.register(Playing)
admin.site.register(Toy)