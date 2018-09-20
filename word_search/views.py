import json
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from .models import Puzzle, Word, Row, Cell
from .algorithm import generateWordSearchHard

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
    try:
        currentPuzzle = Puzzle.objects.get(pk=puzzle_id)
    except:
        res = HttpResponse()
        res.status_code = 404
        return res

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
    bodyUnicode = request.body.decode('utf-8') #decodes bytes into string
    bodyData = json.loads(bodyUnicode) #decodes string into dictionary

    # {title: 'TITLE HERE', words: ['', '', ''], length: 5}   <-- incoming request body formatted like this

    newPuzzle = Puzzle.objects.create(
        title=bodyData['title'], 
        creationDate=timezone.now(), 
        length=bodyData['length']
    )
    for word in bodyData['words']:
        Word.objects.create(puzzle=newPuzzle, word=word)
    
    newMatrix = generateWordSearchHard(bodyData['words'], bodyData['length'])
    for row in newMatrix:
        r = Row.objects.create(puzzle=newPuzzle)
        for letter in row:
            Cell.objects.create(row=r, value=letter)

    return JsonResponse({
        "id": newPuzzle.id
        }, safe=False)



def editPuzzle(request, puzzle_id):
    bodyUnicode = request.body.decode('utf-8') #decodes bytes into string
    bodyData = json.loads(bodyUnicode) #decodes string into dictionary

    try:
        p = Puzzle.objects.get(pk=puzzle_id)
        p.title = bodyData['title']
        p.save()
    except:
        res = HttpResponse()
        res.ok = False
        res.status_code = 404
        return res

    return JsonResponse(bodyData, safe=False)


def deletePuzzle(request, puzzle_id):
    try:
        Puzzle.objects.get(pk=puzzle_id).delete()
    except:
        res = HttpResponse()
        res.ok = False
        res.status_code = 404
        return res

    res = HttpResponse()
    res.status_code = 204
    return res