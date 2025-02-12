from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('offline.html', views.offline, name='offline'),
]
