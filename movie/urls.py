from django.conf.urls import url
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter
from .views import (
    MovieList,
    MovieResCreate,
    MovieNotifyViewSet,
)


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"),
        name="movie_index"),
    url(r'^search$', MovieList.as_view(), name="movie_list"),
    url(r'^create$', MovieResCreate.as_view(), name="movie_create"),
]

router = DefaultRouter()
router.register(r'movie_notify', MovieNotifyViewSet)

urlpatterns.extend(router.urls)
