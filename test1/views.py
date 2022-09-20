import datetime

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import StudentForm
from .models import Quote, Posts
from django.db.models import Q


def search(request):
    posts = Posts.objects.all().order_by('-views')
    min_view = request.GET.get('min_view')
    max_view = request.GET.get('max_view')
    min_date = request.GET.get('min_date')
    max_date = request.GET.get('max_date')
    author = request.GET.get('author')
    title = request.GET.get('title')
    view = request.GET.get('view')
    print(author)
    if is_valid_query(author):
        print('Yeah')
        posts = posts.filter(author_name__search=author)
        print(author)
        print(posts.count())
    if is_valid_query(title):
        print('Yeah')
        posts = posts.filter(title__search=title)
        print(title)
        print(posts.count())
    if is_valid_query(view):
        print('Yeah')
        posts = posts.filter(views__exact=view)
        print(view)
        print(posts.count())
    if is_valid_query(min_view) and is_valid_query(max_view):
        posts = posts.filter(Q(views__gte=min_view) & Q(views__lte=max_view))
    if is_valid_query(min_view):
        posts = posts.filter(views__gt=min_view)
    if is_valid_query(max_view):
        posts = posts.filter(views__lt=max_view)
    if is_valid_query(min_date) and is_valid_query(max_date):
        posts = posts.filter(published_date__range=(min_date, max_date)).order_by('published_date')
    if is_valid_query(min_date):
        posts = posts.filter(published_date__gte=min_date).order_by('-published_date')
    if is_valid_query(max_date):
        posts = posts.filter(Q(published_date__lte=max_date)).order_by('-published_date')

    # if is_valid_query(max_date):
    #     posts=posts.filter(published_date__lte=max_date)

    context = {
        'objects': posts,

    }
    return render(request, 'home.html', context)


def is_valid_query(param):
    return param != "" and param is not None

