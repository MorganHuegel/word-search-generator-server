from django.urls import path

from . import views

urlpatterns = [
    path('', views.getAllPuzzles, name='getAllPuzzles'),
    path('<int:puzzle_id>', views.getOnePuzzle, name='getOnePuzzle')
]