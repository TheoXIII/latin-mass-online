from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('church', views.church, name='church'),
]
