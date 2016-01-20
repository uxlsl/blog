import pytz
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from rest_framework import generics
from django.conf import settings
from .models import MovieRes, MovieUpdate
from .serializers import MovieResSerializer


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
        if MovieUpdate.objects.count():
            messages.add_message(self.request, messages.INFO,
                                 '最后更新时间 {:%Y-%m-%d %H:%M:%S}'
                                 .format(MovieUpdate.objects.first()
                                         .update_at.astimezone(
                                     pytz.timezone(settings.TIME_ZONE))))
        return ret


class MovieResCreate(generics.CreateAPIView):
    queryset = MovieRes.objects.all()
    serializer_class = MovieResSerializer

    def post(self, request, *args, **kwargs):
        MovieUpdate.objects.create()
        return super(MovieResCreate, self).post(request, *args, **kwargs)
