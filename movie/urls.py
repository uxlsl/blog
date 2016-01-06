from django.conf.urls import url
from .views import (
    MovieList,
)


urlpatterns = [
    url(r'^$', MovieList.as_view(), name="movie_list")
]
