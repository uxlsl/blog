from django.shortcuts import render


def index(request):
    content = {'object_list': [{
        'name': 'lsl',
        'source': 'abc',
        'url': 'www.qq.com',
        'down_urls': [1, 2, 3, 4, 5]
    }]}
    return render(request, 'movie_list.html', content)
