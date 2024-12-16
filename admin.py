
from django.contrib import admin
from .models import Developer, Game, Member

admin.site.register(Member)
admin.site.register(Game)
admin.site.register(Developer)
