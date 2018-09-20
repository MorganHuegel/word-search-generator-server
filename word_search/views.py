from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from .models import Puzzle

# Create your views here.
def getAllPuzzles(request):
    allPuzzles = Puzzle.objects.all()
    data = []
    for puzzle in allPuzzles:
        onePuzzle = {"id": puzzle.id, "title": puzzle.title, "words": []}
        words = puzzle.getWordList()
        for word in words:
            onePuzzle["words"].append(word.word)
        data.append(onePuzzle)
        
    return JsonResponse(data, safe=False)
    
    
    
def getOnePuzzle(request, puzzle_id):
    currentPuzzle = Puzzle.objects.get(pk=puzzle_id)

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
        "id": currentPuzzle.id,
        "title": currentPuzzle.title,
        "words": wordList,
        "puzzle": matrix
        }, safe=False)

def postPuzzle(request):
    return JsonResponse({"method": "Test Method"})
    # return JsonResponse(HttpRequest.POST['username'])
