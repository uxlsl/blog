from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import MovieRes


class MovieList(ListView):
    template_name = "movie_list.html"
    context_object_name = "movie_list"
    paginate_by = 10

    def get_queryset(self):
        if 'q' in self.request.GET:
            queryset = MovieRes.objects.filter(
                Q(movie__name__contains=self.request.GET['q'])
                | Q(movie__starring__contains=self.request.GET['q'])
            ).order_by('-update_at')
        else:
            queryset = MovieRes.objects.order_by('-update_at')
        return queryset

    def get_context_data(self, **kwargs):
        """增加这个目的在于在页码中增加一个参数!
        """
        ret = super(MovieList, self).get_context_data(**kwargs)
        ret['q'] = self.request.GET.get('q', '')
        return ret
