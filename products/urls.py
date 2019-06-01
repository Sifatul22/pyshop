from django.urls import path
from . import views  # period means current folder


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]
