from django.urls import path, include, re_path
from Media import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_results, name = 'search_results'),
]
