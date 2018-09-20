from django.contrib import admin

# Register your models here.
from .models import Puzzle, Word, Row, Cell
admin.site.register(Puzzle)
admin.site.register(Word)
admin.site.register(Row)
admin.site.register(Cell)
