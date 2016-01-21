from django.conf.urls import url
from .views import (
    MovieList,
    MovieResCreate,
    MovieNotifyList,
)


urlpatterns = [
    url(r'^$', MovieList.as_view(), name="movie_list"),
    url(r'^create$', MovieResCreate.as_view(), name="movie_create"),
    url(r'^movie_notify$', MovieNotifyList.as_view(), name="movie_notify")
]
