from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='site-home'),
    path('dinner/', views.dinner, name='site-dinner'),
    path('snack/', views.snack, name='site-snack'),
    path('dessert/', views.dessert, name='site-dessert'),
    path('about/', views.about, name='site-about'),
    path('wine/', views.wine, name='site-wine'),
]