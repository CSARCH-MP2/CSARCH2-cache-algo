from django.urls import path
from .views import *


urlpatterns = [
  path('', index, name='index'),
  path('perform/', perform_bsa_lru, name='perform')
]