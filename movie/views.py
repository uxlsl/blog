from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie


class MovieList(ListView):
    template_name = "movie_list.html"
    context_object_name = "movie_list"
    queryset = Movie.objects.all()
    paginate_by = 10
    # def get_queryset(self):
    #     if 'q' in self.request.GET:
    #         queryset = Movie.objects.filter(
    #             name__in=self.request.GET['q']).order_by('-update_at')
    #     else:
    #         queryset = Movie.objects.order_by('-update_at')
    #     return queryset
