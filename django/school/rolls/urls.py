from django.urls import path

from . import views


app_name = 'rolls'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('searchresult/', views.searchResult, name='searchResult'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('isActive/', views.active, name='active'),
    path('department/', views.assign, name='assign'),
]
