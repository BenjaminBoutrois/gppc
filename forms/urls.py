from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gppc', views.gppc, name='gppc'),
    path('history_gppc', views.history_gppc, name='history_gppc'),
]