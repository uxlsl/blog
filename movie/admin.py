from django.contrib import admin
from .models import Movie, MovieRes, MovieNotify


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'filmtype',
                    'director', 'starring')


class MovieResAdmin(admin.ModelAdmin):
    list_display = ('movie', 'url', 'source', 'down_urls')


class MovieNotifyAdmin(admin.ModelAdmin):
    list_display = ('key', 'email', 'is_notify', 'is_can_notify')


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieRes, MovieResAdmin)
admin.site.register(MovieNotify, MovieNotifyAdmin)
