from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def getAllPuzzles(request):
    dummyData = [
        {"title": "Hello World!"}, 
        {"title": "Hello Mars!"}, 
        {"title": "Hello Jupiter!"}, 
    ]
    return JsonResponse(dummyData, safe=False)
    
    
    
def getOnePuzzle(request, puzzle_id):
    return JsonResponse({"title": "Hello World!"})

