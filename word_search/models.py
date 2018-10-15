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



