from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    MovieList,
    MovieResCreate,
    MovieNotifyViewSet,
)


urlpatterns = [
    url(r'^$', MovieList.as_view(), name="movie_list"),
    url(r'^create$', MovieResCreate.as_view(), name="movie_create"),
]

router = DefaultRouter()
router.register(r'movie_notify', MovieNotifyViewSet)

urlpatterns.extend(router.urls)
