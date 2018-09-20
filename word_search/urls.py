from django.urls import path

from . import views

urlpatterns = [
    path('', views.getAllPuzzles, name='getAllPuzzles'),
    path('new/', views.postPuzzle, name='postPuzzle'),
    path('<int:puzzle_id>/', views.getOnePuzzle, name='getOnePuzzle'),
    path('<int:puzzle_id>/edit/', views.editPuzzle, name='editPuzzle'),
    path('<int:puzzle_id>/delete/', views.deletePuzzle, name='deletePuzzle')
]