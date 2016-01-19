from django.conf.urls import url
from .views import (
    MovieList,
    MovieResCreate
)


urlpatterns = [
    url(r'^$', MovieList.as_view(), name="movie_list"),
    url(r'^create$', MovieResCreate.as_view(), name="movie_create"),
]
