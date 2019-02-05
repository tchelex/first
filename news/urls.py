from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news'),
    path('news/', views.home, name='news'),
    path('list/', views.list, name='list')
]
