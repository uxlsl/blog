from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'source')


admin.site.register(Movie, MovieAdmin)
