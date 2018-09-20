from django.db import models

# Create your models here.
class Puzzle(models.Model):
    title = models.CharField(max_length=50, unique=True)
    creationDate = models.DateTimeField('date created')
    length = models.IntegerField(default=10)

    def getWordList(self):
        return self.word_set.all()

    def getMatrix(self):
        matrix = []
        rows = self.row_set.all()
        for row in rows:
            matrix.append(row.getCells())
        return matrix

    def __str__(self):
        return self.title


class Word(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    def __str__(self):
        return self.word



class Row(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    def getCells(self):
        return self.cell_set.all()
    
    def __str__(self):
        return "Row of %s" % self.puzzle

class Cell(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    value = models.CharField(max_length=1)
    def __str__(self):
        return self.value


'''
python3 manage.py shell

from word_search.models import Puzzle, Word, Row, Cell
from django.utils import timezone
p = Puzzle(title="First Puzzle", creationDate=timezone.now())
p.save()
Puzzle.objects.all()    <-- array of the Puzzle Objects
Puzzle.objects.get(pk=1)   <---- returns single Puzzle Object

puzzle1 = Puzzle.objects.all()[0]
w = WordList(puzzle=puzzle1)
w.save()
^^^shortcut for this -->  WordList.objects.create(puzzle=puzzle1)

wordList = WordList.objects.all()[0]
Word(wordList=wordList1, word="first").save()
Word(wordList=wordList1, word="second").save()
Word(wordList=wordList1, word="third").save()
Word(wordList=wordList1, word="fourth").save()
Word(wordList=wordList1, word="fifth").save()
Word.objects.filter(wordList=wordList1)

Word.objects.filter(puzzle=1)
Word.objects.filter(puzzle=2)


p2 = Puzzle.objects.filter(id=2)

p2.word_set.create(word="contemplative")
^^^shortcut for creating words that reference a certain puzzle

p2.word_set.all()
^^^will recall all of the words that are related to the given puzzle

Puzzle.objects.all().order_by('-creationDate')
^^^will recall all puzzles, sorted by date (most recent first)

Puzzles.objects.filter(pk=2).delete()   <-- how to Delete Puzzles


Cell.objects.create(row=Row.objects.get(pk=2), value='J')  <--create will return the new object


for i in range(len(mat)):
    dbRow = Row.objects.filter(puzzle=3)[i]
    for letter in mat[i]:
        Cell.objects.create(row=dbRow, value=letter)


mat = [['u', 'y', 'g', 'z', 'z', 'z', 'z', 'z'],
 ['s', 'g', 'a', 'o', 'l', 'm', 'p', 'y'],
 ['u', 'c', 'y', 'o', 'd', 't', 'm', 'b'],
 ['c', 'i', 'b', 'f', 'e', 'r', 'i', 'f'],
 ['b', 'p', 'y', 'r', 'r', 'a', 'h', 'b'],
 ['c', 'k', 'v', 'c', 'f', 'e', 'c', 'o'],
 ['r', 'h', 'u', 'k', 'l', 'h', 'y', 's'],
 ['t', 's', 'r', 'x', 'a', 'b', 'a', 'h']]

newWordList = ['chimp', 'harry', 'alfred', 'heart', 'dog', 'zzzzz']
'''

