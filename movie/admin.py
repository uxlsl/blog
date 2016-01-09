from django.contrib import admin
from .models import Movie, MovieRes


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'filmtype',
                    'director', 'starring')


class MovieResAdmin(admin.ModelAdmin):
    list_display = ('movie', 'url', 'source', 'down_urls')


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRes, MovieResAdmin)
