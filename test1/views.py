from multiprocessing import context
from unicodedata import name

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render
from .models import Quote
from django.db.models import Q


def index(request):
    return render(request, 'home.html', {'objects': Quote.objects.all()})


def SearchResult(request):
    query = request.GET.get('q')
    search_vector = SearchVector('author', weight='B') + SearchVector('quote', weight='A')
    search_query = SearchQuery(query)
    data = Quote.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)).filter(
        search=search_query).order_by('-rank')
    return render(request, 'search.html', {'objects': data})
