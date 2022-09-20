from django.urls import path
from .views import search

app_name = 'test'

urlpatterns = [
    path('', search, name='home'),

]
