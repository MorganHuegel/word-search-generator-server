from django.shortcuts import render
from django.http import JsonResponse
from .models import Puzzle

# Create your views here.
def getAllPuzzles(request):
    dummyData = [
        {"title": "Hello World!"}, 
        {"title": "Hello Mars!"}, 
        {"title": "Hello Jupiter!"}, 
    ]
    return JsonResponse(dummyData, safe=False)
    
    
    
def getOnePuzzle(request, puzzle_id):
    puzzle_id = 3 #Take this out once you make Post endpoint
    currentPuzzle = Puzzle.objects.get(pk=3)
    title = currentPuzzle.title

    wordList = []
    for word in currentPuzzle.getWordList():
        wordList.append(word.word)

    matrixObject = currentPuzzle.getMatrix()
    matrix = []
    for row in matrixObject:
        newRow = []
        for cell in row:
            newRow.append(cell.value)
        matrix.append(newRow)
    
    return JsonResponse({
        "title": title,
        "wordList": wordList,
        "matrix": matrix
        }, safe=False)
