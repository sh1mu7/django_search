from django.urls import path
from .views import SearchResult, index

app_name='test'

urlpatterns = [
    path('',index,name='home'),
    path('result',SearchResult,name='search')
]
