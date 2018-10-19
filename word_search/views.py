import json
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from .models import Puzzle, Word, Row, Cell
from .algorithm import generateWordSearchHard
from .solving_algorithm import solver

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

    newPuzzle = Puzzle.objects.create(
        title=bodyData['title'], 
        creationDate=timezone.now(), 
        length=bodyData['length']
    )
    for word in bodyData['words']:
        Word.objects.create(puzzle=newPuzzle, word=word)
    
    try:
        #Try to generate puzzle 3 times before concluding that it must be impossible
        for i in range(3):
            newMatrix = generateWordSearchHard(bodyData['words'], bodyData['length'])
            if newMatrix:
                break
            elif i == 2:
                raise ValueError
    except ValueError:
        res = HttpResponse()
        res.status_code = 400
        res.reason_phrase = 'NOT CREATED. Try shorter words or a larger puzzle size.'
        Puzzle.objects.get(pk=newPuzzle.id).delete()
        return res

    for row in newMatrix:
        r = Row.objects.create(puzzle=newPuzzle)
        for letter in row:
            Cell.objects.create(row=r, value=letter)

    return JsonResponse({
        "id": newPuzzle.id
        }, safe=False)





def findWord(request):
    bodyUnicode = request.body.decode('utf-8') #decodes bytes into string
    bodyData = json.loads(bodyUnicode) #decodes string into dictionary

    positions = solver(bodyData['word'], bodyData['puzzle'])
    if positions == False:
      res = HttpResponse('That word is not in this puzzle.')
      res.ok = False
      res.status_code = 404
      return res
    return JsonResponse(positions, safe=False)





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