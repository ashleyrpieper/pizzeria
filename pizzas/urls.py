"""Defines URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for Pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for each pizza.
    path('pizzas/<int:pizzas_id>/', views.pizzas, name='pizza'),
    # Page for adding a new comment
    path('new_comment/', views.new_comment, name='new_comment')
]