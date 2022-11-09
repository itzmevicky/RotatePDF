from django.urls import path
from .views import *
urlpatterns = [
    path('',PDF.as_view())
]